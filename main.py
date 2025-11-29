import discord
from discord.ext import commands
from history import HistoryManager
from tree import ConversationTree
from extra import ExtraFeatures
import os
from dotenv import load_dotenv   #(pour charger le fichier .env)

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")   # ton token sera lu depuis .env

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

                       # Assure que le dossier data existe
os.makedirs("data", exist_ok=True)

                  # Chargement des modules
history = HistoryManager()
tree = ConversationTree()
extras = ExtraFeatures()

                            # Chargement des données sauvegardées
history.load()
tree.load()
extras.load()
                 #commandes : historique

@bot.command()
async def last(ctx):
    history.add(ctx.author.id, "last")
    history.save()
    last = history.get_last(ctx.author.id)
    await ctx.send(f"Dernière commande : **{last}**")

@bot.command()
async def history_cmd(ctx):
    history.add(ctx.author.id, "history")
    history.save()
    h = history.get_all(ctx.author.id)
    await ctx.send("\n".join(h) if h else "Aucune commande enregistrée.")

@bot.command()
async def clear_history(ctx):
    history.add(ctx.author.id, "clear_history")
    history.clear(ctx.author.id)
    history.save()
    await ctx.send("Historique supprimé.")

               # Commandes : conversation via arbre
@bot.command()
async def helpme(ctx):
    history.add(ctx.author.id, "helpme")
    history.save()
    tree.start(ctx.author.id)
    question = tree.get_question(ctx.author.id)
    await ctx.send(question)

@bot.command()
async def answer(ctx, *, user_answer):
    history.add(ctx.author.id, "answer")
    history.save()
    msg = tree.answer(ctx.author.id, user_answer)
    await ctx.send(msg)

@bot.command()
async def reset(ctx):
    history.add(ctx.author.id, "reset")
    history.save()
    tree.reset(ctx.author.id)
    await ctx.send("Discussion réinitialisée.")

@bot.command()
async def speak(ctx, *, subject):
    history.add(ctx.author.id, f"speak {subject}")
    history.save()
    exists = tree.contains(subject)
    await ctx.send("oui" if exists else "non")

# Commandes pour les bonus
@bot.command()
async def ping(ctx):
    history.add(ctx.author.id, "ping")
    history.save()
    await ctx.send(extras.ping(ctx.author.id))

@bot.command()
async def random_number(ctx):
    history.add(ctx.author.id, "random_number")
    history.save()
    n = extras.random_number(ctx.author.id)
    await ctx.send(f"Nombre aléatoire : {n}")

@bot.command()
async def quote(ctx):
    history.add(ctx.author.id, "quote")
    history.save()
    q = extras.random_quote(ctx.author.id)
    await ctx.send(q)

                  # Sauvegarde automatique à la déconnexion
@bot.event
async def on_disconnect():
    history.save()
    tree.save()
    extras.save()
    print("Sauvegarde effectuée à la déconnexion.")

bot.run(TOKEN)
