# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

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
    return render_template('index.html', title='Стартовая', user=user, posts=posts)
    #return "А если по русский написать?"