#!/usr/bin/python3
"""Thii is a a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHBNB():
    """Return text Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return text HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
