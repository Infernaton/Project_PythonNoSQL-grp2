from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return {
            'message': 'Never gonna give you Up !'
           }


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8880,
        debug=True,
    )
