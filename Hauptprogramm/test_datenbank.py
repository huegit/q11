# das SQLite Modul
# http://docs.python.org/library/sqlite3.html

from sqlite3 import *

data = [(1, "Mueahi","Baum","mueahi@baum.de"),
        (2, "Hodor","Hodor","hodor@hodor.hodor")]   # zu speichernde Daten

con = connect("daten.bank")         # alternativ ins RAM: ":memory"/"daten.bank"

# DATEN SCHREIBEN

try:
    con.execute("""
    CREATE TABLE person(
    id INT,
    vorname CHAR(20) NOT NULL,
    nachname CHAR(30) NOT NULL,
    email CHAR(40));
    """)                    # Tabellendefinition
    con.execute("CREATE Primary key pk ON TABLE person keys id")
    
except OperationalError:
    pass
    
con.commit()            # Daten werden geschreiben

con.executemany("INSERT INTO person(id, vorname, nachname, email)VALUES(?,?,?,?)", data)
con.commit()

# DATEN AUSLESEN

for i in con.execute("SELECT * FROM person;"):
    print(i)        # Datensatz einzeln ausgeben

con.close()         # Datenbank schließen

