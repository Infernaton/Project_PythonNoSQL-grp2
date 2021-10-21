import flask
from pymongo.errors import BulkWriteError

from mongo import clients


def get_users(limit):
    uses = []
    for i in range(int(limit)):
        users = clients().PythonProject.firstTest.find()
        uses.append(users[i])
    return flask.jsonify([user for user in uses])


def get_categories(user, limit):
    try:
        uses = []
        users = clients().PythonProject.firstTest.find({"name": user})
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
        categories = clients().PythonProject.category.find({"name": cat})
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
