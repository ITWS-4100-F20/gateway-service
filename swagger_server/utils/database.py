import pymongo
from swagger_server import app_config

client = pymongo.MongoClient(app_config.MONGO_CONNECTION_STRING)

"""
def CreateConnection(uri):
    try:
        client = pymongo.MongoClient(uri)
    except:
        return False
    return True
"""