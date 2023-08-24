from .abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict = {}):
        self.data = data

    def to_dict(self):
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"]
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        raise NotImplementedError
