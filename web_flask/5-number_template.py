#/usr/bin/python3
#script that starts a Flask web application

#from app import app
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    repl = text.replace("_", " ")
    return 'C {}'.format(repl)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    repl = text.replace("_", " ")
    return 'Python {}'.format(repl)


@app.route('/number/<int:n>', strict_slashes=False)
def n_route(n):
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route('/number_template')
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
