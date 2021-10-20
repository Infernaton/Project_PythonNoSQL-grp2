import __main__

import flask

from mongo import clients


def getdatas():
    users = clients().testdb.users.find()
    return flask.jsonify([user for user in users])