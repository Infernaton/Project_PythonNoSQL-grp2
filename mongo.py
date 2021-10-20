"""MongoDB module"""

import pymongo


def main():
    """The main function"""
    password = "user"
    client = pymongo.MongoClient(f"mongodb+srv://user:user@pythonproject.d94wv.mongodb.net/?retryWrites=true&w=majority")
    db = client.testdb
    collection = db.users
    for i in range(1, 11):
        user = {
            "_id": i,
            "first_name": f"First_name {i}",
            "last-name": f"Last_name {i}",
            "age": f"Age {i}",
        }
        user_id = collection.insert_one(user).inserted_id
        print(f"Inserted {user_id}: {user}")


if __name__ == "__main__":
    main()
