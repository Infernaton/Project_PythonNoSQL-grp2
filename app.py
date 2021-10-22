# -* - coding: Utf - 8 -*-

import flask
from flask import Flask, request

from methods import get
from methods import patch
from methods import limit
from methods import paginate
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
    """
    action on a certain id from users:
        POST: create a user with the current id, error if the id is already taken
        DELETE: remove the user by id
        PATCH: modify the user by id
        GET: get data of the user by id
    :param id: user_id
    :return: the result of the request
    """
    if request.method == "POST":
        return add_element(request.json, id)
    elif request.method == "DELETE":
        return delete_element(id)
    elif request.method == "PATCH":
        return patch.patchuser(id)
    elif request.method == "GET":
        return get.get_user(id)


@app.route("/users/limit/<value>", methods=["GET"])
def users_limited(value):
    if request.method == "GET":
        return limit.get_users(value)


@app.route("/<user>/categories/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def category(user, id):
    """
    action on a certain id from categories:
        POST: create a category with the current id in the current user profile, error if the id is already taken
        DELETE: remove the category by id
        PATCH: modify the category by id
        GET: get data of the category by id
    :param user: the user profile where we want to add the category
    :param id: category id
    :return: the result of the request
    """
    if request.method == "POST":
        return add_element(request.json, id, user)
    elif request.method == "DELETE":
        return delete_element(id, user)
    elif request.method == "PATCH":
        return patch.patchcategorie(id)
    elif request.method == "GET":
        return get.get_category(id)


@app.route("/<user>/<category>/objects/<id>", methods=["POST", "DELETE", "PATCH", "GET"])
def object_elt(user, category, id):
    """
    action on a certain id from objects:
        POST: create an object with the current id in the current category associated with the user profile,
            error if the id is already taken
        DELETE: remove the object by id
        PATCH: modify the object by id
        GET: get data of the object by id
    :param user: user profile
    :param category: category where the object is
    :param id: object id
    :return: the result of the request
    """
    if request.method == "POST":
        return add_element(request.json, id, user, category)
    elif request.method == "DELETE":
        return delete_element(id, user)
    elif request.method == "PATCH":
        return patch.patchobjet(id)
    elif request.method == "GET":
        return get.get_object(user, category, id)


@app.route("/users")
def get_users():
    return get.get_users()


@app.route("/users/page/<value>", methods=["GET"])
def page_users(value):
    if request.method == "GET":
        return paginate.get_users(value)


@app.route("/categories/page/<value>", methods=["GET"])
def page_categories(value):
    if request.method == "GET":
        return paginate.get_categories(value)


@app.route("/objets/page/<value>", methods=["GET"])
def page_objets(value):
    if request.method == "GET":
        return paginate.get_objets(value)
    """
    get all users
    :return: the list of all users
    """
    return get.get_users(request.json)


@app.route("/<user>/categories")
def get_categories(user):
    """
    get all categories in the user profile defined
    :param user: user profile
    :return: the list of all categories in the user profile
    """
    return get.get_categories(request.json, user)


@app.route("/<user>/categories/limit/<value>")
def limited_categories(user, value):
    return limit.get_categories(user, value)


@app.route("/<user>/<category>/objects")
def get_objects(user, category):
    """
    get all objects in the current categories with the user profile
    :param user: user profile
    :param category: category of the object
    :return: the list of objects
    """
    return get.get_objects(request.json, user, category)


@app.route("/<user>/<category>/objects/limit/<value>")
def limited_objects(user, category, value):
    return limit.get_objects(user, category, value)


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
