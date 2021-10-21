import flask

from mongo import clients


def get_users(page):
    uses = []
    users = clients().PythonProject.users.find()
    for i in range(int(page), int(page) + 2):
        uses.append(users[i])

    return flask.jsonify([user for user in uses])


def get_categories(page):
    uses = []
    users = clients().PythonProject.categories.find()
    for i in range(int(page), int(page) + 2):
        uses.append(users[i])

    return flask.jsonify([user for user in uses])


def get_objets(page):
    uses = []
    users = clients().PythonProject.objects.find()
    for i in range(int(page), int(page) + 2):
        uses.append(users[i])

    return flask.jsonify([user for user in uses])