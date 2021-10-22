import flask
from pymongo.errors import BulkWriteError

from methods.jsonToReturn import json_return
from methods import filter
from mongo import clients


def get_users(json):
    """
    get all the users
    :return: the list of users
    """
    users = clients().PythonProject.users.find()
    if not json:
        json = {}
    users = clients().PythonProject.users.find(filter.all_filter(json))
    return flask.jsonify([user for user in users])


def get_user(value):
    """
           returns the user whose id is passed in parameter
           :param value: id of user
           :return: user
    """
    try:
        users = clients().PythonProject.users.find({"_id": int(value)})
        if len(([user for user in users])) == 0:
            return json_return(500, "Id doesn't exists in database please find another id", 500)
        users = clients().PythonProject.users.find({"_id": int(value)})
        return flask.jsonify([user for user in users])
    except ValueError:
        return json_return(500, "There is a problem with your id it must be an integer and must exist in database", 500)


def get_categories(json, user):
    """
    get the categorie of the user
    :param json: data to search with
    :param user: name of the user
    :return: list of user's categories
    """
    if not json:
        json = {}
    try:
        users = clients().PythonProject.users.find({"name": user})
        client = ([user["_id"] for user in users])

        json["user_id"] = client[0]
        categories = clients().PythonProject.categories.find(filter.all_filter(json))
    except BulkWriteError as e:

        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])
    return flask.jsonify(([category for category in categories]))


def get_category(id):
    """
    get a category
    :param id: id of category
    :return: category
    """
    try:
        categories = clients().PythonProject.categories.find({"_id": int(id)})
    except BulkWriteError as e:

        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])
    return flask.jsonify(([category for category in categories]))


def get_objects(json, user, cat):
    """
    get the object
    :param json: data to search
    :param user: name of user
    :param cat: name of category
    :return: the  object belonging to a person and a category
    """
    if not json:
        json = {}
    try:
        categories = clients().PythonProject.categories.find({"name": cat})
        category = ([categorie["_id"] for categorie in categories])
        users = clients().PythonProject.users.find({"name": user})
        user = ([i["_id"] for i in users])
        json["user_id"] = user[0]
        json["category_id"] = category[0]
        objets = clients().PythonProject.objects.find(filter.all_filter(json))
    except BulkWriteError as e:

        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])
    return flask.jsonify(([objet for objet in objets]))


def get_object(user, cat, id):
    """
    get the object
    :param user: name of the user
    :param cat: name of the category
    :param id: the id of the object
    :return: the object belonging to a person and a category
    """
    try:
        categories = clients().PythonProject.categories.find({"name": cat})
        category = ([categorie["_id"] for categorie in categories])
        users = clients().PythonProject.users.find({"name": user})
        use = ([i["_id"] for i in users])
        objets = clients().PythonProject.objects.find({"_id": int(id), "category_id": category[0], "user_id": use[0]})
    except BulkWriteError as e:

        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])
    return flask.jsonify(([objet for objet in objets]))
