#!/usr/bin/python3
""" 7. Start flask service that does something. """

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list', strict_slashes=False)
def state_list():
    """  fetching data from the storage engine """
    states = sorted(list(storage.all('State').values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_app(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
