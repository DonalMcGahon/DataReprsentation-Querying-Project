from flask import Flask, render_template, redirect, url_for, request, session, flash # imports
from functools import wraps #imports
import sqlite3 # importing sqlite

# name used to start app
app = Flask(__name__)

#Database for SQLite
DATABASE = "drinks"
def connect_db():
    return sqlite3.connect(DATABASE)

# Protects the session from being accessed
app.secret_key = "secretkey"

# login required decorator
# Reference to login decorator code - https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/
def login_required(f):
    @wraps(f) # wrapping the function f
    def wrap(*args, **kwargs):
        if 'logged_in' in session: # if there is not a KEY called loggin_in (meaning user is logged in) in the session object
            return f(*args, **kwargs) # if KEY is found in sessions, it is going to log you in
        else:
            flash('You need to login first.') # it is going to catch it, display this message
            return redirect(url_for('login')) # and return it to the login page
    return wrap

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None # error is None to start off
    if request.method == 'POST': # if method does = a post method
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': # need to test the data + username & password set to "admin"
            error = 'Invalid credentials. Please try again.' # This error will appear if login is incorrect
        else: # Otherwise
            session['logged_in'] = True # if user credentials are correct, logged in = True
            return redirect(url_for('softDrinks')) # redirect to opening page of web app
    return render_template('login.html', error=error) # if credentials are wrong variable error will be shown


@app.route('/logout')
@login_required # login is required to acces this page
def logout():
    session.pop('logged_in' , None) # setting to none will log user out
    flash('You just logged out!' )
    return redirect(url_for('login')) # redirects user back to login page


@app.route('/softDrinks')
@login_required# login is required to acces this page
def softDrinks():
    return render_template("softDrinks.html")



@app.route("/addInfo")
def addprofile():
    drinkname = request.args.get("drinkname") # drinkname will be used to input name of drinks
    calories = request.args.get("calories") # calories will be used to input the amount of calories

    db = connect_db()
    sql = "insert into people (drinkname, calories) values(?,?)"
    #db.execute(sql, [myname, calories]) --> commented out as was giving me an error
    db.commit()
    db.close()

    return render_template("softDrinks.html", htmlpage_drinkname=drinkname, htmlpage_calories=calories)
 
# starts the app
if __name__ == "__main__":
    app.run(debug=True)