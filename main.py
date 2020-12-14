from flask import Flask, jsonify, request
import names
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"


@app.route("/user")
def user():
    gender = request.args.get("gender")
    if gender == "male":
        first_name = names.get_first_name(gender="male")
    elif gender == "female":
        first_name = names.get_first_name(gender="female")
    else:
        first_name = names.get_first_name()
    age = random.randint(18, 40)
    last_name = names.get_last_name()
    return jsonify(
        {
            "name": f"{first_name} {last_name}",
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=4000, host="localhost")
