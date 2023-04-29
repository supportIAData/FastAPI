from users import users
from AddUser import AddUser
from invoke import task
from dotenv import load_dotenv

# chargement des variables d'environnement
load_dotenv("../.env")

import sys, os

sys.path.insert(0, '..')
from webapp import db, app
from webapp.Models.User import User

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(f"../{os.getenv('DB_NAME')}")

@task
def build(ctx):
    iterUsers = AddUser(users)
    with app.app_context():
        for name, about in iterUsers:
            db.session.add(User(name = name, about = about))
            db.session.commit()
        
        users = User.query.all()
        print(len( users) )

@task
def createTable(ctx):
    with app.app_context():
        db.create_all()
        
