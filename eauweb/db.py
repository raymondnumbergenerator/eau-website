from . import app
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app, Response
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_migrate import Migrate
import os
import os.path as op
import sqlite3
from werkzeug.exceptions import HTTPException

# configuration
# DEBUG = True

app = app
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

class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text())
    image = db.Column(db.String(80))
    website = db.Column(db.String(80))

    def __init__(self, name='', description='', image='', website=''):
        self.name = name
        self.description = description
        self.image = image
        self.website = website

    def __repr__(self):
        return '<Name %r>' % self.name

class ModelView(ModelView):
    def is_accessible(self):
        auth = request.authorization or request.environ.get('REMOTE_USER')  # workaround for Apache
        if not auth or (auth.username, auth.password) != app.config['ADMIN_CREDENTIALS']:
            raise HTTPException('', Response(
                "You are not authorized to view this page.", 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            ))
        return True

admin = Admin(app)
admin.add_view(ModelView(Officer, db.session))
path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/pictures/', name='Picture Files'))
admin.add_view(ModelView(Club, db.session))

