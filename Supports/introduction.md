# Flask

Micro Framework

Installez avant de lancer la virtualisation dotenv pour le fichier de configuration d'environnement.

```python
#
python3 -m venv venv
. venv/bin/activate

pip install Flask
```

Dans l'environnement de développement faites l'inventaire des modules utilisés pour l'application

```bash
pip list > requirements.txt
```

## Création de la table à partir d'un modèle

Connectez vous à la base de données pour vérifier que la table a bien été créée avec la commmande Invoke createTable.

Avant tout installez **invoke** qui permet de lancer des tasks en ligne de commande, un autre module **Fabrick** existe également pour déployer l'application sur un serveur distant (CI). 

```bash
invoke createTable
```

Puis dans la base de données physique (ficher) :

```bash
sqlite3 school.sqlite
sqlite>.table
users
```

## 01 Exercice 

Créez une route users pour afficher les utilisateurs sur une page users.html, utilisez le template "base.html".

```python
users = [
    { "id" : 1, "name" : "Alan", "description" : "Alan: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
    { "id" : 2, "name" : "Alice", "description" : "Alice: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
    { "id" : 3, "name" : "Phil", "description" : "Phil: Lorem ipsum dolor sit amet consectetur adipisicing elit" },
]
```

## 02 Exercice navigation

Faite un menu permettant avec un item hom cliquable pour revenir sur la page d'accueil, depuis n'importe quelle page.

Chaque nom d'user sur la page d'accueil est un lien cliquable qui affiche sa description.


## Installation de SQLITE

Avec conda vous pouvez installer sqlite

```python
pip install sqlite
```

Créez la structure de données, dans la base de données (fichier) sqlite.db

```sql
CREATE TABLE `users` 
(
    `id` INTEGER PRIMARY KEY, 
    `name` VARCHAR(100) NOT NULL, 
    `description` TEXT
);
```

En utilisant le module sqlite déjà installé dans un fichier install.py, exécuté en Python, insérez les données  suivantes dans la table users.

Indications :

```python
import sqlite3

database = './sqlite.db'
db = sqlite3.connect(database) # connection à la base de donnnées

cur = db.execute( query, args )

# vérifiez que les données sont insérées 

print(cur.fetchall())

# fermer la connexion 
cur.close()

```

## 03 Exercice

Pour cet exercice si vous souhaitez découvrir SQLAlchemy vous pouvez l'utiliser, sinon faites une requête simple avec sqlite3 dans le fichier run.py pour afficher les données.

Créez un modèle qui vous permet d'afficher avec **SQLALchemy** les utilisateurs de notre table users.

Indications : aidez-vous de la documentation [alchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#query-the-data)