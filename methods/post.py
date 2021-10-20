from mongo import clients
from methods.jsonToReturn import *
import flask


def addElement(json, id_elt, user="", category=""):
    """
    Add a element to the DB, that can be a user, a categorie or an object
    :param json: the data in json form to add in the DB
    :param id_elt: the current element
    :param user: we need to specified it, if it a category or an object (data from the url)
    :param category:  we need to specified it, if it an object (data from the url)
    :return: a json message which announced the result of the request
    """

    json["_id"] = int(id_elt)
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
            return id_exist(clients().PythonProject.object, id_elt, json)
        else:
            return id_exist(clients().PythonProject.category, id_elt, json)
    else:
        return id_exist(clients().PythonProject.firstTest, id_elt, json)


def find_id_user(name):
    """
    Find a id_user with a given name
    :param name:
    :return: the id if exist
    """
    id = clients().PythonProject.firstTest.find({"name": name}, {"_id": 1})
    id = flask.jsonify([user for user in id]).json
    if len(id) != 0:
        return id[0]["_id"]
    else:
        return False


def find_id_category(category):
    """
    find a id_category with a given category name
    :param category:
    :return: the id if exist
    """
    id = clients().PythonProject.category.find({"name": category}, {"_id": 1})
    id = flask.jsonify([user for user in id]).json
    if len(id) != 0:
        return id[0]["_id"]
    else:
        return False


def id_exist(db_name, id_elt, json):
    """
    Test if the element we try to add have a correct id, test if the place with the id is not already taken
    :param db_name: the db to search with the id
    :param id_elt: the element
    :param json: json to add to the db
    :return: the search
    """
    test_id = db_name.find({"_id": int(id_elt)})
    test_id = flask.jsonify([user for user in test_id]).json
    if len(test_id) == 0:
        db_name.insert_one(json)
        return json_return(0, "Successfully Add !")
    else:
        return json_return(9, "ID already taken")
