# -* - coding: Utf - 8 -*-

import flask
from flask import Flask, request

from methods import get
from methods import patch
import os

from methods.delete import *
from methods.post import *
from methods.jsonToReturn import *

app = Flask(__name__)

"""
User input of any element
{
    "name": element_name,
    "data": {}
}
"""


@app.route("/users/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def user(id):
    if request.method == "POST":
        return addElement(request.json, id)
    elif request.method == "DELETE":
        return deleteElement(id)
    elif request.method == "PATCH":
        return patch.patchuser(id)
    elif request.method == "GET":
        return get.get_user(id)


@app.route("/<user>/categories/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def category(user, id):
    if request.method == "POST":
        return addElement(request.json, id, user)
    elif request.method == "DELETE":
        return deleteElement(id, user)
    elif request.method == "PATCH":
        return patch.patchcategorie(id)
    elif request.method == "GET":
        return get.get_category(id)


@app.route("/<user>/<category>/objects/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def object_elt(user, category, id):
    if request.method == "POST":
        return addElement(request.json, id, user, category)
    elif request.method == "DELETE":
        return deleteElement(id, user)
    elif request.method == "PATCH":
        return patch.patchobjet(id)
    elif request.method == "GET":
        return get.get_object(user, category, id)


@app.route("/users")
def get_users():
    return get.get_users(request.json)


@app.route("/<user>/categories")
def get_categories(user):
    return get.get_categories(request.json, user)


@app.route("/<user>/<category>/objects")
def get_objects(user, category):
    return get.get_objects(request.json, user, category)


@app.errorhandler(404)
def not_found(error):
    return json_return(000, "Page not Found", 404)


@app.errorhandler(500)
def internal_error(error):
    return json_return(000, "Internal Server error", 500)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8880,
        debug=True,
    )
