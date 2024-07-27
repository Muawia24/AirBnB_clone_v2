#!/usr/bin/python3
"""
Hello Flask!
"""


from flask import Flask
from flask import render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def render(n):

    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):

    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
