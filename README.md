# Flask

## Les données pour le TP

```python
users = [
    { "id" : 1, "name" : "Alan", "description" : "Alan: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
    { "id" : 2, "name" : "Alice", "description" : "Alice: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
    { "id" : 3, "name" : "Phil", "description" : "Phil: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
]
```

Micro Framework Flask, il permet de faire des applications sans imposer une strucutre spécifique cependant, plus l'application se complexifiera plus vous devez l'organiser en respectant une architecture MVC.

Structure de l'application **webapp** pour découvrir Flask :

```txt
├── build               
│   ├── AddUser.py      <-- Itérateur 
│   ├── tasks.py        <-- Hydratation/création de la table users
│   └── users.py
├── requirements.txt    <-- dépendances du projet
├── run.py              <-- routing et controller & serveur de développement
├── school.sqlite
├── .env                <-- variable d'environnements de l'application
├── .envfask            <-- variable d'environnements Flask
├── .gitignore
└── webapp              <-- application 
    ├── Models          <-- Model Flask_SQLAlchemy 
    │   └── User.py
    ├── __init__.py     <-- Bootstrap de l'application
    ├── static          <-- Les assets statiques  
    │   └── css
    │       └── styles.css
    └── templates        <-- Moteur de template Jinja 
        ├── base.html
        ├── index.html
        ├── navigation.html
        ├── user.html
        └── users.html
```

Installez, avant de lancer la virtualisation, **dotenv** pour les variables d'environnement.

Nous utiliserons également pour la partie ORM **Flask_SQLAlchemy**

Rappelons que dotenv est un module permettant de définir des variables d'environnement pour votre application. Nous créerons deux fichiers de configuration : .env et .flaskenv

```python
# dotenv
 pip install python-dotenv

# virtualisation
python3 -m venv venv
# le point indique l'endroit où la virtualisation doit s'effectuer
. venv/bin/activate

pip install fastapi

# ORM
pip install alembic
pip install mysqlclient
pip install sqlalchemy

alembic init migrations
```

Dans ce fichier: **alembic.ini** changez la ligne suivante :

```txt

sqlalchemy.url = mysql://root:root@127.0.0.1/covid
```

Création d'une migration 

```bash
alembic revision -m "Create cases table"
```

Puis dans le fichier de migration 

```python 
from alembic import op
import sqlalchemy as sa

# ...

def upgrade():
    op.create_table(
      'cases',
      sa.Column("id", sa.Integer, primary_key=True),
      sa.Column("name", sa.String(200)),
      sa.Column("active", sa.Boolean),
    )

def downgrade():
    op.drop_table('cases')
```

Pour créer les tables en base de données

```bash
alembic upgrade head
```

Une fois les dépendances installées dans votre application, créez/re-créez le fichier requirements.txt, il liste les dépendances de l'application.

```bash
pip list > requirements.txt
```

## Définir des tasks 

Nous allons installer le module **invoke**, il s'utilise avec **Fabrick** un module d'intégration continue. Invoke permet de définir des **tasks** que l'on lancera depuis la console.

```bash
# Intégration continue
pip install fabric

# Tasks
pip install invoke
```

## Fichier bootstrap __init__.py

Ce fichier pemet d'initialiser l'application avec ses différentes dépendances.

```python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv("../.env")

app = Flask(__name__, template_folder='templates')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(os.getenv('DB_NAME'))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)

# Mettre au niveau de webapp le modèle User
from webapp.Models import User
```

### 01 Exercice dans le fichier tasks.py

Définissez les taches pour créez la table users et insérer des données d'exemple. Pour chaque tache on passe le contexte du module Invoke, variable **ctx** en paramètre des fonctions.

Vous utiliserez **Flask_SQLAlchemy** pour la création de la table users. Utilisez le modèle User dans le dossier Model, pensez à importez la base de données db :

```python
from webapp import db 

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False)
    about = db.Column(db.Text)
    
    def __init__(self, name, about):
        self.name = name
        self.about = about
        
    def __repr__(self):
        
        return f"{self.name} {self.about}"
```

Création des taches

```python
from invoke import task

@task
def createTable(ctx):
    pass

@task
def build(ctx):
    pass
```

Exécutez maintenant les tasks 

1. Création de la table

```bash
invoke createTable
```

2. Insertion des données d'exemple

```bash
invoke build
```

Puis dans la base de données physique, ficher school.sqlite, vérifiez que la table existe, ainsi que ses données 

```bash
sqlite3 school.sqlite
sqlite>.table
users

sqlite> select * from users;
```

## 02 Exercice home, users et la page d'un utilisateur

Créez les pages home, user et users. Faites une navigation, dans le fichier navigation.html

Dans le fichier run.py

```python
# Import des dépendance depuis le Bootstrap
from webapp import render_template, db, app, request

@app.route("/home")
@app.route("/")
def home():
    pass

@app.route("/users")
def users():
    pass

@app.route("/user/<id>")
def user(id):
    pass

```

Pour récupérez les données avec l'ORM, utilisez les syntaxes suivantes:

```python
# Récupère l'users dont l'id vaut 1
db.session.query(User).filter(User.id == 1)

# Tous les users
db.session.query(User).all()
```

La méthode **render_template** permet de retourner une vue en lui passant de la données, dans le fichier run.py

```python

@app.route("/users")
def users():
    users = db.session.query(User).all()
    
    return render_template("users.html", title="All users", users = users)
```