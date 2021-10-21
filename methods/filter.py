def all_filter(json):
    if 'name' in json:
        json["name"] = {"$regex": u"" + json['name'] + ""}
    return json
