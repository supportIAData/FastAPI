from webapp import render_template, db, app, request
from webapp.Models.User import User
from random import randint

@app.route("/home")
@app.route("/")
def home():
    user = db.session.query(User).filter(User.id == randint(1, 6))
    
    return render_template("index.html", title="School DIA 02", user = user[0] )

@app.route("/users")
def users():
    users = db.session.query(User).all()
    
    return render_template("users.html", title="All users", users = users)

@app.route("/user/<id>")
def user(id):
    # Exception si pas de user

    user = db.session.query(User).filter(User.id == id )
    user = user[0] if user else None 

    return render_template("user.html", user=user )

if __name__ == "__main__":
    app.run()