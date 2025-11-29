Bot Discord B2 – Projet de rattrapage par NJUNDOM STELLA

        Description

Ce projet est un bot Dicord réalisé en Python dans le cadre du rattrapage.Il contient les fonctionnalités demandées dans l’énoncé c'est-à-dire : historique, arbre de discussion, sauvegarde persistante, ainsi que les 3 commandes bonus.

        Fonctionnalités
    *Historique

!last → affiche la dernière commande envoyée.

!history_cmd → affiche toutes les commandes depuis la première connexion.

!clear_history → vide l’historique. Sauvegarde dans data/history.json.

    *Arbre de discussion

!helpme → lance la conversation.

!answer oui/non → permet de suivre le chemin dans l’arbre.

!reset → recommence depuis la racine.

!speak <ici tu met ton sujet souhaaité> → mais vérifie bien si le sujet existe dans l’arbre.

    *Sauvegarde persistante

Les données sont enregistrées dans des fichiers JSON (history.json, users.json).

Sauvegarde automatique à chaque commande.

    *Commandes bonus

!ping → Pong !

!random_number → nombre aléatoire entre 1 et 100.

!quote → citation inspirante. Stats utilisateurs enregistrées dans data/users.json.

        Utilisation

Installer les dépendances : pip install -r requirements.txt

Créer un fichier .env avec votre token Discord : DISCORD_TOKEN=VOTRE TOKEN

Lancer le bot : python main.py

        Organisation

main.py → point d’entrée du bot.

history.py → gestion de l’historique (liste chaînée).

tree.py → arbre de discussion.

extra.py → commandes bonus et stats utilisateurs.

data/ → fichiers JSON pour la sauvegarde.

        Checklist de test

requirements.txt installe toutes les dépendances (discord.py, python-dotenv)

Le fichier .env est requis pour lancer le bot :
DISCORD_TOKEN=VOTRE_TOKEN_ICI

Le bot démarre sans erreur (audioop résolu avec Python 3.11)

Les commande fonctionnent sur Discord

Les fichiers JSON (history.json, users.json) se mettent à jour automatiquemet
