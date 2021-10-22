from mongo import clients
from methods.jsonToReturn import *
from methods.gestionDB import *


def delete_element(id, user="", category=""):
    """
    Delete function for a given id, user or a category.
    :param id: the current element
    :param user: we need to specified it, if it a category or an object (data from the url)
    :param category: we need to specified it, if it an object (data from the url)
    :return: element deleted
    """
    json = {"_id": int(id)}
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
            clients().PythonProject.objects.delete_many({"category_id": int(id)})
            return id_exist(clients().PythonProject.categories, id, json)
    else:
        clients().PythonProject.objects.delete_many({"user_id": int(id)})
        clients().PythonProject.categories.delete_many({"user_id": int(id)})
        return id_exist(clients().PythonProject.users, id, json)


def id_exist(db_name, id, json):
    """
    Test if the element we try to delete have a correct id, test if the place with the id is not already taken
    :param db_name: the db to search with the id
    :param id: the element
    :param json: json to add to the db
    :return: the search
    """
    test_id = db_name.find({"_id": int(id)})
    test_id = flask.jsonify([user for user in test_id]).json
    if len(test_id) != 0:
        db_name.delete_one(json)
        return json_return(0, "Successfully remove !")
    else:
        return json_return(9, "ID doesn't exist")
