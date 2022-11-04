from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    data = request.get_json()

    operation_type = data.get('operation_type')
    x_value = data.get('x')
    y_value = data.get('y')

    if operation_type == 'addition':
        result = x_value + y_value
    if operation_type == 'subtraction':
        result = x_value - y_value
    if operation_type == 'multiplication':
        result = x_value * y_value

    details = {
        "slackUsername": 'Just_Kayfz',
        "result": result,
        "operation_type": operation_type,
    }

    return jsonify(details)


if __name__ == '__main__':
    app.run(debug=True)
