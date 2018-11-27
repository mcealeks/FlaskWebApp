from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    #Tak sie nie robi ale jakos trza zaczac
    animals = [
        'kotek',
        'piesek',
        'tomek'
    ]
    return render_template('galeria.html', animals=animals)


