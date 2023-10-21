from flask import Blueprint, render_template, request, flash

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
           flash('Error', category='error')
           
    return render_template("signup.html")