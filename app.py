from flask import Flask, render_template
from data import title, departures, tours
from data import subtitle, description
import random
app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html',
                           title=title,
                           subtitle=subtitle,
                           description=description,
                           tours=tours,
                           departures=departures)


@app.route('/departures/<departure_tag>/')
def render_depature(departure_tag):
    tours_set = {}
    for key, tour in tours.items():
        if tour["departure"] == departure_tag:
            tours_set[key] = tour
    return render_template('departure.html',
                           title=title,
                           tours=tours_set,
                           departure_tag=departure_tag,
                           departures=departures)


@app.route('/tours/<int:id>/')
def render_tour(id):
    return render_template('tour.html',
                           title=title,
                           id=id,
                           tours=tours,
                           departures=departures)


if __name__ == '__main__':
    app.run()
