# -* - coding: Utf - 8 -*-
from flask import Flask, render_template, request

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


@app.route("/users/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def user(id):
    if request.method == "POST":
        return "POST"
    elif request.method == "DELETE":
        return "DELETE"
    elif request.method == "PATCH":
        return "PATCH"
    elif request.method == "GET":
        todos = db.todos.find()
        return flask.jsonify([todo for todo in todos])
        return "GET"


@app.route("/users")
def get_users():
    return "GET USERS"


@app.route("/<user>/categories/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def categorie(user, id):
    if request.method == "POST":
        return "POST"
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
        return "POST"
    elif request.method == "DELETE":
        return "DELETE"
    elif request.method == "PATCH":
        return "PATCH"
    elif request.method == "GET":
        return "GET"


@app.route("/<user>/<categorie>/objects")
def get_objects(user, categorie):
    return "GET USERS"


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8880,
        debug=True,
    )
