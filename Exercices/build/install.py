import sqlite3

from users import users
from AddUser import AddUser

database = '../sqlite.db'
db = sqlite3.connect(database)

cur = db.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE IF NOT EXISTS `users`  \
( \
    `id` INTEGER PRIMARY KEY,  \
    `name` VARCHAR(100) NOT NULL,  \
    `description` TEXT \
); \
")

add = AddUser(users)
cur.executemany("INSERT INTO users( name, description) VALUES ( ?, ?)", add)

cur.execute("select id, name from users")
print(cur.fetchall())

cur.close()

# Lorsqu'on execute directement le script depuis la console 
if __name__ == "__main__":
    print('build data')