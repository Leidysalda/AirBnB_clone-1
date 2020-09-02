#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    """close"""
    storage.close()


@app.route('/cities_by_states')
def state_list():
    """list"""
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
