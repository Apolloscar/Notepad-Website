from flask import Blueprint

views = Blueprint('views', __name__)

# when the root is reached, it will call the proceeding function
@views.route('/')
def home():
    return "<h1>Test</h1>"