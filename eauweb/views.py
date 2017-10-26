from flask import render_template
from flask import url_for

from . import app

@app.route('/')
def index():
   return render_template('index.html')
