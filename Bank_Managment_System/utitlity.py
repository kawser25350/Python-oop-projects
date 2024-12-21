from abc import ABC, abstractmethod
from random import randint

class Utility:
    used_ids = set()

    @staticmethod
    def generate_id():
        id = randint(1000, 9999)
        while id in Utility.used_ids:
            id = randint(1000, 9999)
        Utility.used_ids.add(id)
        return id

    # Removed hash_password method


