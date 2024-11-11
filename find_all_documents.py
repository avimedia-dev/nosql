from mongo_connection import connect

client = connect()
if client is not None:
    db = client["sample_mflix"]
    collection = db["users"]

    cursor = collection.find()
    for document in cursor:
        print(document)

client.close()