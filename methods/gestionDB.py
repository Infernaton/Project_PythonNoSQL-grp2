from mongo import clients
import flask


def find_id_user(name):
    """
    Find a id_user with a given name
    :param name:
    :return: the id if exist
    """
    id = clients().PythonProject.users.find({"name": name}, {"_id": 1})
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
    id = clients().PythonProject.categories.find({"name": category}, {"_id": 1})
    id = flask.jsonify([user for user in id]).json
    if len(id) != 0:
        return id[0]["_id"]
    else:
        return False


def find_existed_name(db, name_elt):
    """
    find in the db an element by name
    :param db: the db to search
    :param name_elt: the name element
    :return: the data if it found one, or false
    """
    datas = db.find({"name": name_elt})
    datas = flask.jsonify([data for data in datas]).json
    if len(datas) != 0:
        return datas
    else:
        return False

