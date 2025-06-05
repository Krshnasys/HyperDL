from typing import Dict
from pyrogram import Client

class ClientManager:
    def __init__(self, helper_bots: Dict[str, Client]):
        self.clients = helper_bots
        self.loads = {k: 0 for k in self.clients}

    def get_least_loaded(self):
        return min(self.loads, key=self.loads.get)

    def increase_load(self, key):
        self.loads[key] += 1

    def decrease_load(self, key):
        self.loads[key] -= 1
