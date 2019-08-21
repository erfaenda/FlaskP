# -*- coding: utf-8 -*-
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Alex'}
    return render_template('index.html', title='Home', user=user)
    #return "А если по русский написать?"