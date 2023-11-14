from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLALchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/orderAhead.html")
def orderAhead():
    return render_template("orderAhead.html")


#@app.route("/admin")
#def admin():
#    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)