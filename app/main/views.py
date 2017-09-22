from flask import render_template, session, redirect, url_for, current_app, request
from flask import flash
from .. import db
from ..models import User
from . import main
from .forms import NameForm
from datetime import datetime


@main.route('/welcome')
def welcome():
    return render_template('welcome.html')


@main.route('/register')
def register():
    return render_template('register.html')


@main.route('/acm')
def acm():
    return render_template('acm.html')


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit:
        user = form.username.data
        usersex = form.sex.data
        tel = form.telnumber.data
        maj = form.major.data
        email = form.mail.data
        about_me = form.about.data
        if user:
            newuser = User(username=user, telnumber=tel,
                           sex=usersex, major=maj, mail=email, about=about_me)
            db.session.add(newuser)
            session['known'] = False
            return render_template('welcome.html', user=user, current_time=datetime.utcnow())
    return render_template('index.html', user=user, form=form)
