from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'yan'}
    return render_template('index.html', title='2K League 2019 Player Modeling', user=user)

