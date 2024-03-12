import pymongo
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def list_rows(database_name, collection_name):
    # Connect to MongoDB
    client = pymongo.MongoClient(os.getenv("MONGO_URI"))

    # Select database
    db = client[database_name]

    # Select collection
    collection = db[collection_name]

    # List all documents in the collection
    for document in collection.find():
        print(document)

# Example usage
if __name__ == "__main__":
    database_name = "db"
    collection_name = "collection"
    list_rows(database_name, collection_name)
