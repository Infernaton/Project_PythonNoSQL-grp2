# -* - coding: Utf - 8 -*-

import flask
from flask import Flask,  request, make_response

import get
import os
from methods.post import *
from methods.jsonToReturn import *


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
        return "PATCH"
    elif request.method == "GET":
        return get.getuser(id)


@app.route("/users")
def get_users():
    return get.getusers()


@app.route("/<user>/categories/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def categorie(user, id):
    if request.method == "POST":
        return addElement(request.json, id, user)
    elif request.method == "DELETE":
        return "DELETE"
    elif request.method == "PATCH":
        return "PATCH"
    elif request.method == "GET":
        return "GET"


@app.route("/<user>/categories")
def get_categories(user):
    return "GET USERS"


@app.route("/<user>/<categorie>/objects/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def object(user, categorie, id):
    if request.method == "POST":
        return addElement(request.json, id, user)
    elif request.method == "DELETE":
        return "DELETE"
    elif request.method == "PATCH":
        return "PATCH"
    elif request.method == "GET":
        return "GET"


@app.route("/<user>/<categorie>/objects")
def get_objects(user, categorie):
    return "GET USERS"


@app.route("/users")
def getDatas():
    liste = []
    listem = []
    for parent, dnames, fnames in os.walk("users"):
        for fname in fnames:
            filename = os.path.join(parent, fname)
            liste.append(filename)
            listem = liste[0:int(request.args.get('limit'))]

    arguments = request.args
    if 'limit' in arguments:
        return flask.jsonify(listem)
    elif int(request.args.get('limit') > len(liste)):
        return {
            'error': 'The limit can not be higher than' + len(liste),
            'err_code': 500
        }
    return {
        'error': 'you need to specify limit',
        'err_code': 500
    }


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
