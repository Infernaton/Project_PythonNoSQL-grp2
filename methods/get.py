import __main__

import flask

from mongo import clients
from bson.objectid import ObjectId


def getusers():
    """
    get all the users
    :return: the list of users
    """
    users = clients().PythonProject.firstTest.find()
    return flask.jsonify([user for user in users])


def getuser(value):
    users = clients().PythonProject.firstTest.find({"_id": int(value)})
    return flask.jsonify([user for user in users])
