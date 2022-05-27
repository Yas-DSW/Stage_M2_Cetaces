#!/usr/bin/env python3

# Ce programme a été créer par Yascim Kamel dans le cadre de son stage de Master 2 au cours du projet ANR DICWOC porté 
# par Aurélie Célérier et Sylvia Campagna. Il permet de lancer les programmes d'implémentation de la base de données associée au projet.

### Pour faire fonctionner ce programme plusieurs arguments sont nécessaires :
	# 1) Le nom de l'assemblage
	# 2) Le nom de la base de données sur laquelle a été trouvé l'assemblage
	# 3) le score busco
	# 4) Le chemin vers le multifastas contenant les génes à tester 


import sys
import psycopg2 ## Permet l'interaction avec la base de données PostgreSQL. 
import multifasta_to_bd, OA_to_BD

nom_complet=sys.argv[1] ### Récupération du nom de l'assemblage

BD=sys.argv[2] ## Récupération de la base de données sur laquelle les données ont été trouvées
esp_genre=nom_complet.split("_")

espece=esp_genre[1]
genre=esp_genre[0]

assemblie= nom_complet +'_'+ BD

score_busco=sys.argv[3]
multi_fasta=sys.argv[4]

### Connexion à la base de données

connection=psycopg2.connect("dbname=groc user=yascim")

#### Remplissage de la base de données avec les résultats obtenus

print("\nInsertion des résultats obtenue sur " + nom_complet +" par le Pipeline de Yascim" )

### Lancement des programmes
OA_to_BD.OAE_to_BD(espece,genre,assemblie,BD,score_busco, connection) ### implémentation des tables organisme, assemblie et experience
multifasta_to_bd.multi_fasta_to_bd(multi_fasta,connection, espece,assemblie) ### implémentation des tables genes et link.
