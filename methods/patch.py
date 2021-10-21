import flask
from pymongo.errors import BulkWriteError

from methods.jsonToReturn import json_return
from mongo import clients
from flask import request


def patchuser(value):
    """
    update name, firstname and age of a user
    :param value: id of user
    :return: the user updated
    """
    try:
        result = clients().PythonProject.users.update_one(
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
    except TypeError:
        return json_return(500, "there is a problem with your input it must be a json object", 500)
    except KeyError:
        return json_return(500, "your datas must be like : {'name':'<your name>','data':'{}'", 500)

    return "updated"


def patchcategorie(id):
    try:

        result = clients().PythonProject.categories.update_one(
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

        result = clients().PythonProject.objects.update_one(
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
