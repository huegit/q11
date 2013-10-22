from sqlite3 import *

riskdb = connect("risk.datenbank")

for i in riskdb.execute("SELECT * FROM armeen;"):
    print(i)

for i in riskdb.execute("SELECT * FROM karten;"):
    print(i)

for i in riskdb.execute("SELECT * FROM kontinente;"):
    print(i)
