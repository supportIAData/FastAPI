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
python -m venv venv
# le point indique l'endroit où la virtualisation doit s'effectuer
. venv/bin/activate

pip install fastapi

# dependency
pip install alembic
pip install mysqlclient
pip install sqlalchemy
pip install jinja2 
pip install python-dotenv 
pip install uvicorn

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

## Lancer le serveur

```bash
uvicorn app.main:app --reload
 ```

 ## ORM

 ### One to Many

 L'inverse d'une relation one to many est la relation many to one.

 Un parent a plusieurs enfants, la clé secondaire se trouve dans le modèle enfant. Le relation simple one to many, noté que dans cette relation on utilisera la strucutre de List, Set ou tout autre type collection.

 ```python
from typing import List

from sqlalchemy import 
Mapped, 
mapped_column, 
relationship,
ForeignKey,
DeclarativeBase

class Base(DeclarativeBase):
    pass

class Parent(Base):
__tablename__ = "parents"

id: Mapped[int] = mapped_column(primary_key=True)
children: Mapped[List["Child"]] = relationship(back_populates="parent")

class Child(Base):
__tablename__ = "childs"

id: Mapped[int] = mapped_column(primary_key=True)
# clé secondaire
parent_id: Mapped[int] = mapped_column(ForeignKey("parents.id"))
```

Si on souhaite codé la relation inverse alors il faut ajouté à la classe qui possède la clé secondaire le code suivant :

```python 
class Child(Base):
    __tablename__ = "childs"

    id: Mapped[int] = mapped_column(primary_key=True)
    # clé secondaire
    parent_id: Mapped[int] = mapped_column(ForeignKey("parents.id"))
    parent: Mapped["Parent"] = relationship(back_populates="children")
```

### Many to one

Dans le cas où l'entité Child aurait plus d'un parents, dans l'exemple ci-dessous chaque parent à au moins un enfant, voyez ci-après pour coder l'option moins restrictive (nullable) :

```python 
class Parent(Base):
    __tablename__ = "parents"

    id: Mapped[int] = mapped_column(primary_key=True)
    child_id: Mapped[int] = mapped_column(ForeignKey("childs.id"))
    child: Mapped["Child"] = relationship()

class Child(Base):
    __tablename__ = "childs"
    id: Mapped[int] = mapped_column(primary_key=True)
    parents: Mapped[List["Parent"]] = relationship(back_populates="child")
```

Moins restrictif avec une option nullable sur la relation :

```python 
class Parent(Base):
    __tablename__ = "parents"

    id: Mapped[int] = mapped_column(primary_key=True)
    child_id: Mapped[int] = mapped_column(ForeignKey("childs.id"))
    child: Mapped[Optional["Child"]] = relationship(back_populates="parents")

class Child(Base):
    __tablename__ = "childs"
    id: Mapped[int] = mapped_column(primary_key=True)
    parents: Mapped[List["Parent"]] = relationship(back_populates="child")
```

### One to one

Aucun mapping entre les deux entitées, on utilisera la syntaxe suivante pour coder cette relation :

```python 
class Parent(Base):
    __tablename__ = "parents"

    id = mapped_column(Integer, primary_key=True)
    child = relationship("Child", uselist=False, back_populates="parent")


class Child(Base):
    __tablename__ = "childs"

    id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(ForeignKey("parents.id"))
    parent = relationship("Parent", back_populates="child")
```

### Many to many

Dans cette relation il faudra créer également la table d'association, ici un parent pourra avoir plus d'un enfant et un enfant plus d'un parent.

```python 

# classe d'association 
child_parent = Table(
    "child_parent",
    Base.metadata,
    Column("parent_id", ForeignKey("parents.id")),
    Column("child_id", ForeignKey("childs.id")),
)

class Parent(Base):
    __tablename__ = "parents"

    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List[Child]] = relationship(secondary=child_parent)


class Child(Base):
    __tablename__ = "childs"

    id: Mapped[int] = mapped_column(primary_key=True)

``` 

### Proposition de relation 

Un individu possède de 0-N pays et inversement un pays a de 0-N individus.

Un individu peut avoir été infecté par le virus de 0-N fois.
