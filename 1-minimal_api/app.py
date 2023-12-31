#!/usr/bin/python3
'''
A minimal flask app
'''
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Default route
    """
    return "Hello World!"
