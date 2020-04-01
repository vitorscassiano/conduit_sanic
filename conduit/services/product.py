from random import randint
from uuid import uuid4
from datetime import datetime


class Product():
    def __init__(self, database={}):
        super().__init__()
        self.database = database

    def find(self, id=None):
        if id:
            return self.database.get(id)
        else:
            return self.database

    def create(self, payload):
        id = str(uuid4())
        createdAt = datetime.now().isoformat()
        self.database[id] = {"id": id, "createdAt": createdAt, **payload}

        return self.database[id]

    def delete(self, id):
        del self.database[id]
        if self.database.get(id):
            return False
        else:
            return True
