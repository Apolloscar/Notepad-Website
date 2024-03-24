from flask import Blueprint,render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

# can recieve get and post requests
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # filter out users that have corresponding email
        user = User.query.filter_by(email =email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category="success")
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password", category='error')
        else:
            flash('Email not exist', category='error')
    
    return render_template("login.html", boolean = True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    # if request is a post request
    if request.method =='POST':
        # get elements of request
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email =email).first()
        if user:
            flash("Email already exists", category='error')

        elif len(email) < 4:
            # email should be at least 4 characters long to be valid
            flash("Email must be at least 4 characters", category="error")
        elif len(first_name) <2:
            
            flash("Name should be more than 1 character", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7:
            flash("Password should be at least 7 characters", category="error")
        else:
            # add valid user to database
            new_user = User(email=email,first_name= first_name, password = generate_password_hash(password1, method='pbkdf2:sha1'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created", category="success")
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")