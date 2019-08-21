# -*- coding: utf-8 -*-
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Alex'}
    posts = [
        {
            'author': {'username': 'Alex'},
            'body': 'Круто я учу фласк!'
        },
        {
            'author': {'username': 'Миша'},
            'body': 'Какой прекрасный денек!'
        },
        {
            'author': {'username': 'Валера'},
            'body': 'Опять хуйню какую то программируешь?'
        },
        {
            'author': {'username': 'Тень прогера'},
            'body': 'Круто! Стоит на основе этого простого примера сделать что то типо примитивного хтмл чата!'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    #return "А если по русский написать?"