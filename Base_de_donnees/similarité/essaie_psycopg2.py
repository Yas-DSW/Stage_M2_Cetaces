#!/usr/bin/env python3
import psycopg2

#Connexion à la base de données
connection=psycopg2.connect("dbname=groc user=yascim")

## Ouverture d'un curseur
cur=connection.cursor()

#Execution d'une requête
cur.execute("SELECT * FROM organisme ")

### Récupération sous forme de liste

records=cur.fetchall()

cur.execute("SELECT * FROM assemblie")

records=cur.fetchall()
print(records)