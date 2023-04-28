from flask import Flask, render_template

app = Flask(__name__, template_folder='webapp/templates')

users = [
    { "id" : 1, "name" : "Alan", "description" : "Alan: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
    { "id" : 2, "name" : "Alice", "description" : "Alice: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
    { "id" : 3, "name" : "Phil", "description" : "Phil: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
]

@app.route("/home")
@app.route("/")
def hello():

    return render_template("index.html", title="Hello DIA 02", users = users )

@app.route("/category")
def category():
    return "<p>Hello Category</p>"

@app.route("/user/<id>")
def user(id):
    return f"<p>User{id}</p>"