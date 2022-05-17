from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        if len(email) < 4:
            flash('Email is invalid!', category='error')
        elif len(nickname) < 3:
            flash('Nickname is too short!', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match!', category='error')
        elif len(password1) < 7:
            flash('Passwords is too short!', category='error')
        else:
            new_user = User(email=email, nickname=nickname, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')
            return redirect(url_for('views.home'))
            
    return render_template("sign_up.html")