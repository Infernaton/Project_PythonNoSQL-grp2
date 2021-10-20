def addElement(json, id, user="", category=""):
    """
    Add a element to the DB, that can be a user, a categorie or an object
    :param json: the data in json form to add in the DB
    :param id: the current element
    :param user: we need to specified it if it a category or an object (data from the url)
    :param category:  we need to specified it if it an object (data from the url)
    :return: a json message which announced the result of the request
    """
    return "POST " + id + user + category
