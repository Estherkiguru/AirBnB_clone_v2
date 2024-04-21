#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays "HBNB" """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Displays 'C' followed by the value of text"""
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    """Starts the web development server"""
    app.run(host='0.0.0.0', port=5000)
