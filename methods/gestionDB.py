from mongo import clients
import flask


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
