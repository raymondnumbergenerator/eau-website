from . import app
from flask import render_template
from flask import url_for

from db import get_db

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/nightmarket')
def nightmarket():
    return render_template('nightmarket.html')

@app.route('/officers')
def officers():
    dtb = get_db()
    cur = dtb.execute('select * from officer')
    officers = cur.fetchall()
    return render_template('officers.html', officers=officers)

@app.route('/photos')
def photos():
    return render_template('photos.html')
