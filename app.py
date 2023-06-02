from flask import Flask, flash, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "goo"

db = SQLAlchemy()

# Making Permanent Sessions. Also we will have to do session.permanent = True,
# to actually enable permanent session
app.permanent_session_lifetime = timedelta(days=30)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///budgetscan.db"

db.init_app(app)

USER = []



@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form.get("username")
        if username not in USER:
            USER.append(username)
            session['user'] = username
            flash("user added")
            return render_template("index.html", name=session['user'])
        else:
            flash("user already exists")
            # return render_template("index.html")
    else:
        return render_template("index.html")
    flash("This is a flashed message", "warning")
    return render_template("index.html")

