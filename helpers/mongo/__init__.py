import motor.motor_asyncio
from config import MONGO_DB
import json
import threading
import dns.resolver
import pymongo

mongo_dbb = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
SPAMBOT = "ZAIDUSERBOT"
cli = mongo_dbb["ZAIDUSERBOT"]

class Database:
    def get(self, module: str, variable: str, default=None):
        """Get value from database"""
        raise NotImplementedError

    def set(self, module: str, variable: str, value):
        """Set key in database"""
        raise NotImplementedError

    def remove(self, module: str, variable: str):
        """Remove key from database"""
        raise NotImplementedError

    def get_collection(self, module: str) -> dict:
        """Get database for selected module"""
        raise NotImplementedError

    def close(self):
        """Close the database"""
        raise NotImplementedError

class MongoDatabase(Database):
    def __init__(self, url, name):
        self._client = pymongo.MongoClient(url)
        self._database = self._client[name]

    def set(self, module: str, variable: str, value):
        self._database[module].replace_one(
            {"var": variable}, {"var": variable, "val": value}, upsert=True
        )

    def get(self, module: str, variable: str, expected_value=None):
        doc = self._database[module].find_one({"var": variable})
        return expected_value if doc is None else doc["val"]

    def get_collection(self, module: str):
        return {item["var"]: item["val"] for item in self._database[module].find()}

    def remove(self, module: str, variable: str):
        self._database[module].delete_one({"var": variable})

    def close(self):
        self._client.close()

db = MongoDatabase(MONGO_DB, SPAMBOT)
