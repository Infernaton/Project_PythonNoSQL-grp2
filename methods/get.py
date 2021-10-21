import __main__

import flask
from pymongo.errors import BulkWriteError

from mongo import clients


def getusers():
    """
    get all the users
    :return: the list of users
    """
    users = clients().PythonProject.firstTest.find()
    return flask.jsonify([user for user in users])


def getuser(value):
    """
    returns the user whose id is passed in parameter
    :param value: id of user
    :return: user
    """
    users = clients().PythonProject.firstTest.find({"_id": int(value)})
    return flask.jsonify([user for user in users])


def getcategories(value):
    """
    get the categorie of the user
    :param value: name of the user
    :return: list of user's categories
    """
    try:
        users = clients().PythonProject.firstTest.find({"name": value})
        client = ([user["_id"] for user in users])
        categories = clients().PythonProject.category.find({"user_id": client[0]})
    except BulkWriteError as e:

        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])
    return flask.jsonify(([categorie for categorie in categories]))


def getcategorie(value):
    """
    get a categorie
    :param value: id of categorie
    :return: categorie
    """
    try:
        categories = clients().PythonProject.category.find({"_id": int(value)})
    except BulkWriteError as e:

        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])
    return flask.jsonify(([categorie for categorie in categories]))


def getobject(user, cat):
    """
    get the object
    :param user: name of user
    :param cat: name of categorie
    :return: the  object belonging to a person and a category
    """
    try:
        categories = clients().PythonProject.category.find({"name": cat})
        category = ([categorie["_id"] for categorie in categories])
        users = clients().PythonProject.firstTest.find({"name": user})
        use = ([i["_id"] for i in users])
        objets = clients().PythonProject.object.find({"category_id": category[0], "user_id": use[0]})
    except BulkWriteError as e:

        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])
    return flask.jsonify(([objet for objet in objets]))


def getobjet(user, cat, id):
    """
    get the object
    :param id: the id of ccategorie
    :return: the  object belonging to a person and a category
    """
    try:
        categories = clients().PythonProject.category.find({"name": cat})
        category = ([categorie["_id"] for categorie in categories])
        users = clients().PythonProject.firstTest.find({"name": user})
        use = ([i["_id"] for i in users])
        objets = clients().PythonProject.object.find({"_id": int(id), "category_id": category[0], "user_id": use[0]})
    except BulkWriteError as e:

        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])
    return flask.jsonify(([objet for objet in objets]))
