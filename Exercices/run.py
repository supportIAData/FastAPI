from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from webapp.Model.User import User


app = Flask(__name__, template_folder='webapp/templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
db.init_app(app)

@app.route("/home")
@app.route("/")
def hello():

    return render_template("index.html", title="Hello DIA 02", users = users )

@app.route("/category")
def category():
    return "<p>Hello Category</p>"

@app.route("/user/<id>")
def user(id):
    # Exception si pas de user

    user = list( filter( lambda u: u['id'] == id, users) ) 
    user = user[0] if user else None 

    return render_template("user.html", user= list( filter( lambda u: u['id'] == id, users) ) )

