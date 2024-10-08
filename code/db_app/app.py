from pymongo import MongoClient
import os


def connect_and_test_db():
    try:
        # Connection settings from environment variables
        mongo_host = os.getenv("MONGO_HOST", "localhost")
        print(f"mongo_host: {mongo_host}")
        mongo_port = int(os.getenv("MONGO_PORT", 27017))
        mongo_db = os.getenv("MONGO_DB", "test_db")

        # Create a connection to the MongoDB server
        client = MongoClient(host=mongo_host, port=mongo_port)

        # Get a reference to the test database
        db = client[mongo_db]

        # Get a reference to a collection
        collection = db.test_collection

        # Insert a test document
        test_document = {"name": "test_name"}
        result = collection.insert_one(test_document)

        # Retrieve the inserted document
        retrieved_document = collection.find_one({"_id": result.inserted_id})

        print(f"Document inserted and queried: {retrieved_document}")

        # Close the MongoDB connection
        client.close()

    except Exception as e:
        print(f"Error: {e}")
        return False

    return True


if __name__ == "__main__":
    if connect_and_test_db():
        print("MongoDB test succeeded")
    else:
        print("MongoDB test failed")