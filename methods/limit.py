import flask
from pymongo.errors import BulkWriteError

from methods.jsonToReturn import json_return
from mongo import clients


def get_users(limit):
    """
    get the limited list of elements
    :param limit: number of elements to print
    :return: limited list of user's list
    """
    try:
        uses = []
        users = clients().PythonProject.users.find()
        for i in range(int(limit)):
            uses.append(users[i])
        return flask.jsonify([user for user in uses])
    except IndexError:
        return json_return(000, "Please verify your limit. Maybe the limit is hihger than the number of items", 500)
    except ValueError:
        return json_return(000, "please verify your limit it must be a number", 500)


def get_categories(user, limit):
    try:
        uses = []
        users = clients().PythonProject.categories.find({"name": user})
        client = ([user["_id"] for user in users])
        for i in range(int(limit)):
            categories = clients().PythonProject.category.find({"user_id": client[0]})
            uses.append(categories[i])
    except BulkWriteError as e:

        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])
    return flask.jsonify(([t for t in uses]))


def get_objects(user, cat, value):
    """
    get the object
    :param json: data to search
    :param user: name of user
    :param cat: name of category
    :return: the  object belonging to a person and a category
    """
    try:
        uses = []
        categories = clients().PythonProject.objects.find({"name": cat})
        category = ([categorie["_id"] for categorie in categories])
        users = clients().PythonProject.firstTest.find({"name": user})
        use = ([i["_id"] for i in users])
        for i in range(int(value)):
            objets = clients().PythonProject.object.find({"category_id": category[0], "user_id": use[0]})
            uses.append(objets[i])
    except BulkWriteError as e:

        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])
    return flask.jsonify(([o for o in uses]))
