from .abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict = {}):
        self.data = data

    # Req. 2
    def to_dict(self):
        raise NotImplementedError

    # Req. 3
    @classmethod
    def list_dicts(cls):
        raise NotImplementedError
