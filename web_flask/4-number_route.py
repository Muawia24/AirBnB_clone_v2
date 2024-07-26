#!/usr/bin/python3
"""
Hello Flask!
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):

    url_txt = text.replace("_", " ")
    return f'C {url_txt}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text='is cool'):

    url_txt = text.replace("_", " ")
    return f'Python {url_txt}'


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):

    return f'{n} is a number'


if __name__ == '__main__':
    app.run()
