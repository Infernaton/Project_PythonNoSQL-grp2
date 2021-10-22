from flask import url_for
from werkzeug.utils import redirect

from methods.jsonToReturn import *
from methods.gestionDB import *


def add_element(json, id, user="", category=""):
    """
    Add a element to the DB, that can be a user, a categorie or an object
    :param json: the data in json form to add in the DB
    :param id: the current element
    :param user: we need to specified it, if it a category or an object (data from the url)
    :param category:  we need to specified it, if it an object (data from the url)
    :return: a json message which announced the result of the request
    """

    json["_id"] = int(id)
    if user != "":
        user_id = find_id_user(user)
        if not user_id:
            return json_return(10, "User can't be found")
        else:
            json["user_id"] = user_id
        if category != "":
            category_id = find_id_category(category)
            if not category_id:
                return json_return(11, "Category can't be found")
            else:
                json["category_id"] = category_id
            return id_exist(clients().PythonProject.objects, id, json)
        else:
            return id_exist(clients().PythonProject.categories, id, json)
    else:
        return id_exist(clients().PythonProject.users, id, json)


def id_exist(db_name, id, json):
    """
    Test if the element we try to add have a correct id, test if the place with the id is not already taken
    :param db_name: the db to search with the id
    :param id: the element
    :param json: json to add to the db
    :return: the search
    """
    if not find_existed_name(db_name, json['name']):
        return json_return(9, "Name Already in use")

    test_id = db_name.find({"_id": int(id)})
    test_id = flask.jsonify([user for user in test_id]).json
    if len(test_id) == 0:
        db_name.insert_one(json)
        return json_return(0, "Successfully add !")
    else:
        return json_return(8, "ID already taken")
