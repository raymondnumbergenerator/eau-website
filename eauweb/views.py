from . import app
from . import db
from . import helper
from flask import render_template
from flask import url_for

@app.route('/')
def index():
   return render_template('index.html', helper=helper)

@app.route('/nightmarket')
def nightmarket():
    return render_template('nightmarket.html')

@app.route('/officers')
def officers():
    dtb = db.get_db()
    cur = dtb.execute('select * from officer')
    officers = cur.fetchall()
    return render_template('officers.html', officers=officers, helper=helper)

@app.route('/photos')
def photos():
    return render_template('photos.html')
