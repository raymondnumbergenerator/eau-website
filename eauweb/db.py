from . import app
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_migrate import Migrate
import os
import os.path as op
import sqlite3

# configuration
# DEBUG = False

app = app
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'eau.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config['ADMIN_CREDENTIALS'] = ('eau', 'werewolves')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eau.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

class Officer(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	major = db.Column(db.String(80))
	position = db.Column(db.String(80))
	year = db.Column(db.String(80))
	image = db.Column(db.String(80))
	quote = db.Column(db.Text())
	contact = db.Column(db.String(80))

	def __init__(self, name='', position='', major='', year='', image='', quote='', contact=''):
		self.name = name
		self.position = position
		self.major = major
		self.year = year
		self.image = image
		self.position = position
		self.quote = quote
		self.contact = contact

	def __repr__(self):
		return '<Name %r>' % self.name

#admin = Admin(app)
#admin.add_view(ModelView(Officer, db.session))
#path = op.join(op.dirname(__file__), 'static')
#admin.add_view(FileAdmin(path, '/static/pictures/', name='Picture Files'))
