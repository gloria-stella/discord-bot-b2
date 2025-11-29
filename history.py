import json
import os

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class HistoryManager:

    def __init__(self):
        self.histories = {} 
        self.path = "data/history.json"

    def add(self, user_id, command):
        user_id = str(user_id)
        new = Node(command)

        if user_id not in self.histories:
            self.histories[user_id] = new
            return

        new.next = self.histories[user_id]
        self.histories[user_id] = new

    def get_last(self, user_id):
        user_id = str(user_id)
        head = self.histories.get(user_id)
        return head.value if head else None

    def get_all(self, user_id):
        user_id = str(user_id)
        res = []
        head = self.histories.get(user_id)
        while head:
            res.append(head.value)
            head = head.next
        return res

    def clear(self, user_id):
        user_id = str(user_id)
        self.histories[user_id] = None

    # --- Sauvegarde ---
    def save(self):
        data = {uid: self.get_all(uid) for uid in self.histories}
        with open(self.path, "w") as f:
            json.dump(data, f)

    def load(self):
        if not os.path.exists(self.path):
            return
        with open(self.path, "r") as f:
            data = json.load(f)
        for uid, commands in data.items():
            prev = None
            for cmd in commands:
                node = Node(cmd)
                node.next = prev
                prev = node
            self.histories[uid] = prev
