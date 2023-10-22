from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template("login.html", text="Test")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
       email = request.form.get('email')
       firstName = request.form.get('firstName')
       password1 = request.form.get('password1')
       password2 = request.form.get('password2')

       if len(email) < 4:
           flash('Email invalid', category='error')
       elif len(firstName) < 2:
           flash('Name is too short', category='error')
       elif password1 != password2:
           flash('Passwords do not match', category='error')
       elif len(password1) < 7:
           flash('Password is too short!', category='error')
       else:
           new_user = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='sha256'))
           db.session.add(new_user)
           db.session.commit()
           flash('Account created!', category='success')
           return redirect(url_for('views.home'))
           
    return render_template("signup.html")