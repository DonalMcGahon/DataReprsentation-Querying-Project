from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
import sqlite3

app = Flask(__name__)


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
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': # need to test the data
            error = 'Invalid credentials. Please try again.' # This error will appear if login is incorrect
        else: # Otherwise
            session['logged_in'] = True # if user credentials are correct, logged in = Ture
            #flash('You are logged in1! ') # flash message to say you are logged in
            return redirect(url_for('softDrinks')) # redirect to opening page of web app
    return render_template('login.html', error=error) # if credentials are wrong variable error will be shown


@app.route('/logout')
@login_required # login is required to acces this page
def logout():
    session.pop('logged_in' , None)
    flash('You just logged out!' )
    return redirect(url_for('login'))


@app.route('/softDrinks')
@login_required# login is required to acces this page
def softDrinks():
    return render_template("softDrinks.html")


        # create a mapping for /addprofile
@app.route("/addInfo")
def addprofile():
    drinkname = request.args.get("drinkname")
    calories = request.args.get("calories")

    db = connect_db()
    sql = "insert into people (drinkname, calories) values(?,?)"
    #db.execute(sql, [myname, calories])
    db.commit()
    db.close()

    return render_template("softDrinks.html", htmlpage_drinkname=drinkname, htmlpage_calories=calories)
 

if __name__ == "__main__":
    app.run(debug=True)