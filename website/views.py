from flask import Blueprint, render_template
from flask_login import  login_required, current_user

views = Blueprint('views', __name__)

# when the root is reached, it will call the proceeding function
@views.route('/')
@login_required
def home():
    
    return render_template("home.html", user = current_user)