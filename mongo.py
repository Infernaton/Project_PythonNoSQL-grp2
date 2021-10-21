"""MongoDB module"""

import pymongo


def main():
    """The main function"""

    password = "user"
    user = "user"
    client = pymongo.MongoClient(
        f"mongodb+srv://{user}:{password}@pythonproject.d94wv.mongodb.net/?retryWrites=true&w=majority")


if __name__ == "__main__":
    main()


def clients():
    return pymongo.MongoClient(f"mongodb+srv://user:user@pythonproject.d94wv.mongodb.net/?retryWrites=true&w=majority")
