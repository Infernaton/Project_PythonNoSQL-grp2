# -* - coding: Utf - 8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    # dictionnaire de données
    data = [
        {
            'name': 'yann',
            'surname': 'macOS',
            'age': 64
        },
        {
            'name': 'yann',
            'surname': 'macOS',
            'age': 64
        },
        {
            'name': 'yann',
            'surname': 'macOS',
            'age': 64
        },
    ]

    # affichage
    return render_template('index.html', title='home', data=data)


@app.route("/users/<id>", methods=["PATCH", "DELETE", "POST"])
def modify_user(id):
    error_code = "000"
    error_message = "Success !"
    if request.method == "PATCH":
        json_data = request.json["modify"]
        with open(f"users/{id}.txt", "r+") as f:
            content = f.read().split("\n")
            if json_data["firstname"] != "":
                content[0] = json_data["firstname"]
            if json_data["name"] != "":
                content[1] = json_data["name"]
            if json_data["age"] != "":
                content[2] = json_data["age"]
            f.seek(0)
            f.write('\n'.join(content))

    return {
        "status": 200,
        "error_code": error_code,
        "error_message": error_message
    }


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8880,
        debug=True,
    )
