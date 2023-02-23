from pymongo import MongoClient
from bson.objectid import ObjectId


# Connect to the MongoDB instance
client = MongoClient("mongodb://mongo:Blp3BrAbO656LVNgk2B1@containers-us-west-166.railway.app:6395")

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
