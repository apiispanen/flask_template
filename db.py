from pymongo import MongoClient
from bson.objectid import ObjectId

MONGO_CLIENT = os.getenv('MONGO_CLIENT')

if MONGO_CLIENT is not None:
    # RUNNING ON RAILWAY
    MONGO_CLIENT = os.getenv('MONGO_CLIENT')
else:
    from creds import MONGO_CLIENT     
# Connect to the MongoDB instance
client = MongoClient(MONGO_CLIENT)

# Get a list of all the collections in the database
db = client.test
collections = db.list_collection_names()
print(collections)
# Iterate over each collection
for collection_name in collections:
    collection = db[collection_name]
    document = collection.find_one({"_id": ObjectId("63f783cb16dd59001cb54c12")})
    print(document)
    # for key in document:
    #     value = document[key]
    #     print(key, value)
    # Iterate over each document in the collection and print it
    # for document in collection.find():
        




# document = {"key": "value"}
# collection.insert_one(document)
