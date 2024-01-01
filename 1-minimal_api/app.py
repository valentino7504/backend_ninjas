#!/usr/bin/python3
'''
A minimal flask app
'''
from flask import Flask, jsonify, abort
from __init__ import user_1

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Default route
    """
    return "Hello World!"


@app.route("/api/user", strict_slashes=False, methods=["GET"])
@app.route("/api/user/<value>", methods=["GET"], strict_slashes=False)
def return_details(value=None):
    """
    returns the user details
    """
    if value is None:
        return jsonify(user_1.to_dict())
    if value not in user_1.to_dict().keys():
        abort(404)
    return jsonify({value: user_1.to_dict()[value]})


if __name__ == "__main__":
    app.run(debug=True)
