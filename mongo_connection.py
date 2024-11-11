#pip install "pymongo[srv]"
# .env
# DBUSERNAME=...
# DBPASSWORD=...
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
load_dotenv()

def connect():

    uri = f"mongodb+srv://{os.getenv("DBUSERNAME")}:{os.getenv("DBPASSWORD")}@cluster0.m52g8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    print(uri)
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)

# conn = connect()
# conn.close()
# print(conn)

