from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def getGallery():
    osoby = [
        'Piotrek', 
        'Szymon',
        'Tomek noob',
        'Olga'
    ]
    user = {
        "zalogowany": False,
        'nick': 'Owca :)'
    }
    return render_template('galeria.html',osoby=osoby, user=user)




