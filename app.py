# -* - coding: Utf - 8 -*-

import flask
from flask import Flask, request

from methods import get
from methods import patch
import os

from methods.delete import *
from methods.post import *

app = Flask(__name__)

"""
User input of any element
{
    "name": element_name,
    "data": {}
}
"""


@app.route("/users/<id_elt>", methods=["POST", "DELETE", "PATCH", "GET"])
def user(id_elt):
    if request.method == "POST":
        return addElement(request.json, id_elt)
    elif request.method == "DELETE":
        return deleteElement(id)
    elif request.method == "PATCH":
        return patch.patchuser(id)
    elif request.method == "GET":
        return get.getuser(id_elt)


@app.route("/users")
def get_users():
    return get.getusers()


@app.route("/<user>/categories/<id_elt>", methods=["POST", "DELETE", "PATCH", "GET"])
def category(user, id_elt):
    if request.method == "POST":
        return addElement(request.json, id_elt, user)
    elif request.method == "DELETE":
        return deleteElement(id, user)
    elif request.method == "PATCH":
        return patch.patchcategorie(id)
    elif request.method == "GET":
        return get.getcategorie(id)


@app.route("/<user>/categorie", methods=["GET", "PATCH"])
def categorie_elt(user):
    if request.method == "GET":
        return get.getcategories(user)
    elif request.method == "PATCH":
        return patch.patchcategorie(user)


@app.route("/<user>/<category>/objects/<id_elt>", methods=["POST", "DELETE", "PATCH", "GET"])
def object_elt(user, category, id_elt):
    if request.method == "POST":
        return addElement(request.json, id_elt, user, category)
    elif request.method == "DELETE":
        return deleteElement(id, user)
    elif request.method == "PATCH":
        return patch.patchobjet(id)
    elif request.method == "GET":
        return get.getobjet(user, category, id)


@app.route("/<user>/<category>/objects")
def get_objects(user, category):
    return get.getobject(user, category)


@app.errorhandler(404)
def not_found(error):
    return error


@app.errorhandler(500)
def internal_error(error):
    return error


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8880,
        debug=True,
    )
