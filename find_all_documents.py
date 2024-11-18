from mongo_connection import connect

client = connect()
if client is not None:
    db = client["sample_mflix"]
    collection = db["users"]

    cursor = collection.find().limit(5)
    for document in cursor:
        print(document['name'])

client.close()