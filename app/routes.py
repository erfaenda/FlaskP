# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

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
    return render_template('index.html', title='Стартовая', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Логин введен и оправлен {}, значение запомнить в положении={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))
    return render_template('login.html', title='Вход', form=form)