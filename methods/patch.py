import flask
from pymongo.errors import BulkWriteError

from mongo import clients
from flask import request


def patchuser(value):
    """
    update name, firstname and age of a user
    :param value: id of user
    :return: the user updated
    """
    try:
        result = clients().PythonProject.firstTest.update_one(
            {
                '_id': int(value)
            },
            {"$set":
                {
                    "name": request.get_json()["name"],
                    "data":
                        {
                            "lastname": request.get_json()["data"]["lastname"],
                            "age": request.get_json()["data"]["age"]
                        }
                },
            }
        )
    except BulkWriteError as e:
        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])

    return "updated"


def patchcategorie(id):
    try:

        result = clients().PythonProject.category.update_one(
            {
                '_id': int(id)
            },
            {"$set":
                {
                    "name": request.get_json()["name"],
                    "data":
                        {
                            "lastname": request.get_json()["data"]["lastname"],
                            "age": request.get_json()["data"]["age"],
                            "country": request.get_json()["data"]["country"],
                            "numTel": request.get_json()["data"]["numTel"]
                        }
                }
            }
        )
    except BulkWriteError as e:
        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])

    return "UPDATED"


def patchobjet(id):
    try:

        result = clients().PythonProject.object.update_one(
            {
                '_id': int(id)
            },
            {"$set":
                {
                    "name": request.get_json()["name"],
                    "data":
                        {
                            "lastname": request.get_json()["data"]["lastname"],
                            "age": request.get_json()["data"]["age"],
                            "country": request.get_json()["data"]["country"],
                            "numTel": request.get_json()["data"]["numTel"]
                        }
                }
            }
        )
    except BulkWriteError as e:
        return flask.jsonify(message="error",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])

    return "UPDATED"
