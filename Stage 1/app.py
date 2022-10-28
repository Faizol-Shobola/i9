from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():

    details = {
        "slackUsername": 'Just_Kayfz',
        "backend": True,
        "age": 20,
        "bio": 'I am a Backend Developer'
    }

    return details


if __name__ == '__main__':
    app.run(debug=True)