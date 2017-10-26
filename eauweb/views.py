from flask import render_template
from flask import url_for

from . import app

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/officers')
def officers():
    return render_template('officers.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')
