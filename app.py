from flask import Flask, redirect, url_for, render_template

from flask_sqlalchemy import SQLAlchemy
from __init__ import app,db

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/orderAhead")
def orderAhead():
    return render_template("orderAhead.html")

#add admin blueprint with routes that display products and registered users with query and have the admin blueprint only accessible on priviledged login


#@app.route("/admin")
#def admin():
#    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)