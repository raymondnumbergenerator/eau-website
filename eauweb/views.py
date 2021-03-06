from . import app
from . import db
from . import helper
from flask import render_template
from flask import url_for
from flask import redirect

@app.route('/')
def index():
    dtb = db.get_db()
    cur = dtb.execute('select * from club order by name')
    clubs = cur.fetchall()
    return render_template('index.html', clubs=clubs, helper=helper)

@app.route('/market')
def nightmarket():
    return render_template('nightmarket.html')

@app.route('/officers')
def officers():
    dtb = db.get_db()
    cur = dtb.execute('select * from officer')
    officers = cur.fetchall()
    officers = sorted(officers, key = lambda o: helper.officer_sort_order(o['position']))
    return render_template('officers.html', officers=officers, helper=helper)

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/<string:url>')
def shorturl(url):
    dtb = db.get_db()
    cur = dtb.execute('select * from short_url')
    longurl = '/'
    for row in cur:
        if row['short'] == url:
            longurl = row['long']
    return redirect(longurl, code=302)
