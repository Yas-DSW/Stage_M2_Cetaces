#!/usr/bin/env python3

import psycopg2 ## Permet d'intéragir avec la base de données

####################### Complétion de la table organisme ###############

def completion_organisme(espece,genre,connection):

	## Récupération des espèces existantes dans la table organisme
	print("\nVérification des données existantes dans la table organisme ...")
	cur=connection.cursor()
	cur.execute("SELECT espece FROM organisme;")
	BD_specie=cur.fetchall()


	###Création de la liste des espèces déja existante sous forme de liste (plus simple à manipuler)
	liste_espece=[]
	for row in BD_specie:
		liste_espece.append(row[0])

	#complétion
	if len(BD_specie)==0:#### Liste vide = initialisation de la table 
		specie_row='('+ '\''+espece+'\''+ ',' + '\''+genre+'\''+ ',NULL ,NULL ,NULL ,NULL , NULL ,NULL)'
		requete="INSERT INTO organisme VALUES "+ specie_row
		cur.execute(requete)
		print("\n Nouvelle espèce ajoutée !")
		connection.commit() ### Ajout des modifications sur la base
	else:
		if espece not in liste_espece :
			# print("\nnot in list")
			specie_row='('+ '\''+espece+'\'' + ',' + '\''+genre+'\''+ ',NULL ,NULL ,NULL ,NULL , NULL ,NULL)'
			requete="INSERT INTO organisme VALUES "+ specie_row
			cur.execute(requete)
			print("\n Nouvelle espèce ajoutée !")
			connection.commit() ### Ajout des modifications sur la base
		else : 
			print("\n Espèce déja enregistrée.")

##################### Complétion de la table assemblie ############

def completion_assemblie(espece, genre, assemblie, BD, score_busco,connection):

	print("\nVérification des données de la table assemblie ...")
	## Récupération des assemblages déja rentrés
	cur=connection.cursor()
	cur.execute("SELECT identifiant FROM assemblie")
	BD_assemblies=cur.fetchall()

	## Création d'une liste contenant tous les assemblages déja rentrés
	liste_assemblage=[]
	for row in BD_assemblies:
		liste_assemblage.append(row[0])

	#Complétion
	if len(BD_assemblies)==0:
		specie_row='('+ '\''+assemblie+'\''+ ',' + '\'' +espece+'\'' + ',' + '\''+genre+'\''+',\''+ BD + '\',NULL ,NULL,'+'\''+score_busco+'\')'
		requete="INSERT INTO assemblie VALUES "+ specie_row
		cur.execute(requete)
		print("\n Nouvel assemblage ajouté !")
		connection.commit() ### Ajout des modifications sur la base
	else:
		if assemblie not in liste_assemblage :
			# print("\nnot in list")
			specie_row='('+ '\''+assemblie+'\''+ ',' + '\'' +espece+'\'' + ',' + '\''+genre+'\''+',\''+ BD + '\',NULL ,NULL,'+'\''+score_busco+'\')'
			requete="INSERT INTO assemblie VALUES "+ specie_row
			cur.execute(requete)
			print("\n Nouvel assemblage ajouté !")
			connection.commit() ### Ajout des modifications sur la base


###################### Complétion de la table experience ###########################
def completion_experience(connection):
	print("\nAjout de l'expérience dans la table experience")
	cur=connection.cursor()
	cur.execute("INSERT INTO experience (pipeline) VALUES ('Pipeline de Yascim');")
	connection.commit()


################### Définition de la fonction de complétion de la table ###################"

def OAE_to_BD(espece, genre , assemblie,BD,score_busco,connection):
	completion_organisme(espece, genre,connection)
	completion_assemblie(espece,genre,assemblie, BD, score_busco,connection)
	completion_experience(connection)
