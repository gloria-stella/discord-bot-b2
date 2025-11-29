import json
import os

class TreeNode:
    def __init__(self, question=None, yes=None, no=None, result=None):
        self.question = question
        self.yes = yes
        self.no = no
        self.result = result

class ConversationTree:

    def __init__(self):
        self.path = "data/tree.json"
        self.users = {}  # user_id → current node

                    # Arbre par défaut :
        self.root = TreeNode(
            question="Aimes-tu le sport ?",
            yes=TreeNode(
                question="Tu préfères le foot ?",
                yes=TreeNode(result="Tu es sportif !"),
                no=TreeNode(result="Tu es plutôt polyvalent !")
            ),
            no=TreeNode(
                question="Tu préfères les jeux vidéo ?",
                yes=TreeNode(result="Tu es gamer !"),
                no=TreeNode(result="Tu es créatif !")
            )
        )

    def start(self, user_id):
        self.users[user_id] = self.root

    def get_question(self, user_id):
        return self.users[user_id].question

    def answer(self, user_id, response):
        node = self.users[user_id]
        response = response.lower()

        if response == "oui":
            next_node = node.yes
        else:
            next_node = node.no

        if next_node.result:
            self.users[user_id] = self.root
            return f"Résultat : **{next_node.result}**"

        self.users[user_id] = next_node
        return next_node.question

    def reset(self, user_id):
        self.users[user_id] = self.root

    def contains(self, subject):
        subject = subject.lower()

        def dfs(node):
            if not node:
                return False
            if node.question and subject in node.question.lower():
                return True
            return dfs(node.yes) or dfs(node.no)

        return dfs(self.root)

    def save(self):
        pass  # Arbre statique donc pas besoin de sauvegarde

    def load(self):
        pass
