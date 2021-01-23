import json
import requests

from config import *
from pymongo import MongoClient


class ApiMetrics:

    def __init__(self):
        """
                Sets up a connection to the MongoDB instance.
                Credentials are set up in config.py
                """
        self.client = MongoClient(
            f"mongodb+srv://{mongo_user}:{mongo_pw}@cluster0.f4iax.mongodb.net/crawler?retryWrites=true&w=majority"
            # "mongodb://127.0.0.1:27017"
        )
        self.db = self.client['crawler']
        self.apimetrics = self.db.apimetrics

    @classmethod
    def make_request(cls, url):
        response = requests.get(url)
        if response.ok:
            data = json.loads(response.text)
            return data
        return None

    def send_to_db(self, data, keyword):
        if data:
            data['keyword'] = keyword
            self.apimetrics.insert(data)
