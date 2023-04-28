from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
db = SQLAlchemy()

app = Flask(__name__, template_folder='webapp/templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"

db.init_app(app)

users = [
    { "id" : 1, "name" : "Alan", "description" : "Alan: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
    { "id" : 2, "name" : "Alice", "description" : "Alice: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
    { "id" : 3, "name" : "Phil", "description" : "Phil: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
]

print(db.Model)

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

    print(user)

    return render_template("user.html", user= list( filter( lambda u: u['id'] == id, users) ) )

print(__name__)
