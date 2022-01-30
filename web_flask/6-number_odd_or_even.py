#!/usr/bin/python3
"""Thii is a a script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHBNB():
    """Return text Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return text HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return the value of the text"""
    txt = text.replace('_', ' ')
    return 'C {}'.format(txt)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Return the text """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return a int"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Return the template"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Return the template"""
    if int(n) % 2 == 0:
        status = '{} is even'.format(n)
    else:
        status = '{} is odd'.format(n)

    return render_template('6-number_odd_or_even.html', num=status)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
