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

Structure de l'application **covid** pour découvrir Fastapi :

```txt
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

Dépendances et environnement

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

Pour accéder à l'ensemble de vos routes et explorer votre API :

http://127.0.0.1:8000/docs