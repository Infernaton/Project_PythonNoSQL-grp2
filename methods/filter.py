def all_filter(json):
    """
    If we research for certain elements in the db,
    here, we transform the json for MongoDB where it can be understand
    :param json: the research
    :return: the transform json
    """
    if 'name' in json:
        json["name"] = {"$regex": u"" + json['name'] + ""}
    return json
