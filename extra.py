import json
import os
import random

class ExtraFeatures:

    def __init__(self):
        self.path = "data/users.json"
        self.quotes = [
            "Le savoir est une arme.",
            "Chaque jour est une opportunité.",
            "La persévérance bat le talent."
        ]
        self.data = {}
        # Création du dossier data si besoin
        os.makedirs("data", exist_ok=True)

    # --- Méthodes utilitaires ---
    def _init_user(self, user_id):
        uid = str(user_id)
        if uid not in self.data:
            self.data[uid] = {
                "ping_count": 0,
                "quote_count": 0,
                "random_number_count": 0,
                "last_quote": None,
                "last_random_number": None,
                "total_commands": 0,
                "preferred_quote_type": "motivation"  # valeur par défaut
            }

    def _update_stats(self, user_id):
        uid = str(user_id)
        self.data[uid]["total_commands"] += 1

    # --- Commandes bonus ---
    def ping(self, user_id):
        self._init_user(user_id)
        self.data[str(user_id)]["ping_count"] += 1
        self._update_stats(user_id)
        self.save()
        return "Pong !"

    def random_number(self, user_id):
        self._init_user(user_id)
        n = random.randint(1, 100)
        self.data[str(user_id)]["random_number_count"] += 1
        self.data[str(user_id)]["last_random_number"] = n
        self._update_stats(user_id)
        self.save()
        return n

    def random_quote(self, user_id):
        self._init_user(user_id)
        q = random.choice(self.quotes)
        self.data[str(user_id)]["quote_count"] += 1
        self.data[str(user_id)]["last_quote"] = q
        self._update_stats(user_id)
        self.save()
        return q

    # --- Préférences utilisateur ---
    def set_preference(self, user_id, preference):
        """Changer la préférence de citation (ex: motivation, humour, etc.)"""
        self._init_user(user_id)
        self.data[str(user_id)]["preferred_quote_type"] = preference
        self.save()

    def get_stats(self, user_id):
        """Retourne toutes les stats d’un utilisateur"""
        self._init_user(user_id)
        return self.data[str(user_id)]

    # --- Sauvegarde ---
    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)

    def load(self):
        if not os.path.exists(self.path):
            return
        with open(self.path, "r") as f:
            self.data = json.load(f)
