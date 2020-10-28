import pymongo

client = None

def CreateConnection(uri):
    try:
        client = pymongo.MongoClient(uri)
    except:
        return False
    return True