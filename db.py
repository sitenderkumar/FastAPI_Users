from configparser import ConfigParser
from pymongo import MongoClient
import os

env = os.getenv("ENV", ".config")
config = {}
if env == ".config":
    config = ConfigParser()
    config.read(".config")
    config = config["DB"]

db_connection = MongoClient(f"mongodb://{config['HOST']}:{config['PORT']}")
db = db_connection.get_database(config['DATABASE_NAME'])
collection = db[config['COLLECTION_NAME']]