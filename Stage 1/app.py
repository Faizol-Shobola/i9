from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():

    details = {
        "slackUsername": 'Just_Kayfz',
        "backend": True,
        "age": 20,
        "bio": 'I am a Full-Stack developer with experience in both frontend and backend technology.'
    }

    return jsonify(details)


if __name__ == '__main__':
    app.run(debug=True)