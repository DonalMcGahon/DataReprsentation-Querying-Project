from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

app = Flask(__name__)

app.secret_key = "secretkey"

@app.route('/index')
#@login_required
def index():
    #return "Hello World"
    return render_template("index.html")

@app.route('/welcome')
def home():
    return render_template("welcome.html")

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in! ')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
#@login_required
def logout():
    session.pop('logged_in' , None)
    flash('You were just logged out!' )
    return redirect(url_for('home'))


@app.route('/beer')
def beer():
    return render_template("beer.html")

@app.route('/softDrinks')
def softDrinks():
    return render_template("softDrinks.html")

@app.route('/wine')
def wine():
    return render_template("wine.html")

@app.route('/shots')
def shots():
    return render_template("shots.html")

if __name__ == "__main__":
    app.run(debug=True)