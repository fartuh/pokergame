"""
Simple chat created using python3. Uses the API of https://fartuh.xyz
Copyright (C) 2020 Nikita Pavlov
This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License along with this program. If not, see http://www.gnu.org/licenses/.
Author's email: nikitafartuh@ukr.net 
"""

import sqlite3

db = sqlite3.connect('cards.sqlite3')

db.execute("CREATE table cards(id INTEGER PRIMARY KEY, name varchar(3), strength INT, suit INT);")

db.commit()

for i in range(9):
    q = str(i+2) + "♠"
    db.execute("INSERT INTO cards VALUES(null, '" + q + "', '" + str(i+2) + "', 0)")
    db.commit()

for i in range(9):
    q = str(i+2) + "♣"
    db.execute("INSERT INTO cards VALUES(null, '" + q + "', '" + str(i+2) + "', 1)")
    db.commit()

for i in range(9):
    q = str(i+2) + "♥"
    db.execute("INSERT INTO cards VALUES(null, '" + q + "', '" + str(i+2)  + "', 2)")
    db.commit()

for i in range(9):
    q = str(i+2) + "♦"
    db.execute("INSERT INTO cards VALUES(null, '" + q + "', '" + str(i+2) + "', 3)")
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

    i = str(i)
    q = 'J' + s
    db.execute("INSERT INTO cards VALUES(null, '" + q + "', '11', '" + i + "')")
    db.commit()

    q = 'Q' + s
    db.execute("INSERT INTO cards VALUES(null, '" + q + "', '12', '" + i + "')")
    db.commit()

    q = 'K' + s
    db.execute("INSERT INTO cards VALUES(null, '" + q + "', '13', '" + i + "')")
    db.commit()

    q = 'A' + s
    db.execute("INSERT INTO cards VALUES(null, '" + q + "', '14', '" + i + "')")
    db.commit()



db.close()
