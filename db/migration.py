import sqlite3

db = sqlite3.connect('cards.sqlite3')

db.execute("CREATE table cards(id INTEGER PRIMARY KEY, name varchar(3));")

db.commit()

for i in range(9):
    q = str(i+2) + "♠"
    db.execute("INSERT INTO cards VALUES(null, '" + q + "')")
    db.commit()

for i in range(9):
    q = str(i+2) + "♣"
    db.execute("INSERT INTO cards VALUES(null, '" + q + "')")
    db.commit()

for i in range(9):
    q = str(i+2) + "♥"
    db.execute("INSERT INTO cards VALUES(null, '" + q + "')")
    db.commit()

for i in range(9):
    q = str(i+2) + "♦"
    db.execute("INSERT INTO cards VALUES(null, '" + q + "')")
    db.commit()

for i in range(4):
    if i == 0:
        s = "♠"
    elif i == 1:
        s = "♣"
    elif i == 2:
        s = "♥"
    elif i == 3:
        s = "♦"

    q = 'J' + s
    db.execute("INSERT INTO cards VALUES(null, '" + q + "')")
    db.commit()

    q = 'Q' + s
    db.execute("INSERT INTO cards VALUES(null, '" + q + "')")
    db.commit()

    q = 'K' + s
    db.execute("INSERT INTO cards VALUES(null, '" + q + "')")
    db.commit()

    q = 'A' + s
    db.execute("INSERT INTO cards VALUES(null, '" + q + "')")
    db.commit()



db.close()
