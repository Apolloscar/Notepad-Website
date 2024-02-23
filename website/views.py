from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# when the root is reached, it will call the proceeding function
@views.route('/')
def home():
    
    return render_template("home.html")