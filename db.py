from pymongo import MongoClient
from bson.objectid import ObjectId
import os
MONGO_CLIENT = os.getenv('MONGO_CLIENT')

if MONGO_CLIENT is not None:
    # RUNNING ON RAILWAY
    MONGO_CLIENT = os.getenv('MONGO_CLIENT')
else:
    from creds import MONGO_CLIENT     
# Connect to the MongoDB instance
client = MongoClient(MONGO_CLIENT)


def get_people(client=client):
    # Pick out the DB we'd like to use.
    db = client.db
    # GET THE PEOPLE COLLECTION (NOT The Document)
    collection = db['people']
    people = collection.find_one({"_id": ObjectId("63fd0087b9b2b4001ccb7c5f")})
    if people == None:
        print("NO OBJECT FOUND")
    # Returns the JSON string of people, as detailed in our example
    # print(people['People'])
    return people

def delete_person(name, client=client):
    db = client.db
    collection = db['people']
    name = str(name)
    result = collection.update_one({"People": {"$exists": True}}, {"$unset": {"People."+name: ""}})
    if result.modified_count == 1:
        print("Successfully deleted " + name + " from the JSON table.")
    else:
        print(name + " not found in the JSON table.")

def update_person(name, json_input, badname='', client=client):
    db =client.db
    collection = db['people']
    name = str(name)
    for key in json_input:
        collection.update_one({"People": {"$exists": True}}, {"$set": {"People."+name+"."+str(key): str(json_input[key])}})
        print(key +" : "+ json_input[key])

    # If doing user-specific DBs, do:
    # collection.insert({"People": {"$exists": True}}, {"$set": {"People."+name+"."+str(key): str(json_input[key])}}) 
    return name+" Updated"


# conversation_json = """{   "People":{
#             "John Doe": {
#             "School": "Bunker Hill",
#             "Location": "Boston, MA",
#             "Interests":"Painting",
#             "Fun Facts":"Skiied in the alps" }}}"""


# print(update_person("Sam Casey", conversation_json))

