from flask import Blueprint,render_template, request, flash

auth = Blueprint('auth', __name__)

# can recieve get and post requests
@auth.route('/login', methods=['GET','POST'])
def login():
    # request has information about request that was recieved
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    # if request is a post request
    if request.method =='POST':
        # get elements of request
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            # email should be at least 4 characters long to be valid
            flash("Email must be at least 4 characters", category="error")
        elif len(firstName) <2:
            
            flash("Name should be more than 1 character", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7:
            flash("Password should be at least 7 characters", category="error")
        else:
            # add valid user to database
            flash("Account Created", category="success")

    return render_template("sign_up.html")