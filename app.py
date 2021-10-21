# -* - coding: Utf - 8 -*-

import flask
from flask import Flask, request

from methods import get
from methods import patch
import os
from methods.post import *

app = Flask(__name__)

"""
@app.route("/users/<id>", methods=["PATCH", "DELETE", "POST"])
def modify_user(id):
    error_code = "000"
    error_message = "Success !"
    if request.method == "PATCH":
        json_data = request.json["modify"]
        with open(f"users/{id}.txt", "r+") as f:
            content = f.read().split("\n")
            if json_data["firstname"] != "":
                content[0] = json_data["firstname"]
            if json_data["name"] != "":
                content[1] = json_data["name"]
            if json_data["age"] != "":
                content[2] = json_data["age"]
            f.seek(0)
            f.write('\n'.join(content))

    return {
        "status": 200,
        "error_code": error_code,
        "error_message": error_message
    }
"""


@app.route("/user/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def user(id):
    if request.method == "POST":
        return addElement(request.json, id, user)
    elif request.method == "DELETE":
        return "DELETE"
    elif request.method == "PATCH":
        return patch.patchuser(id)
    elif request.method == "GET":
        return get.getuser(id)


@app.route("/users")
def get_users():
    return get.getusers()


@app.route("/<user>/categories/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def category(user, id):
    if request.method == "POST":
        return addElement(request.json, id, user)
    elif request.method == "DELETE":
        return "DELETE"
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


@app.route("/<user>/<category>/objects/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def object_elt(user, category, id):
    if request.method == "POST":
        return addElement(request.json, id, user)
    elif request.method == "DELETE":
        return "DELETE"
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
