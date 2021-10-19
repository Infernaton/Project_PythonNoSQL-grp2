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


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8880,
        debug=True,
    )
