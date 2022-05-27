#!/usr/bin/env python3

from Bio import SeqIO
import re
import sys
import csv
import matrice,backtracking,calcul_similarité

# Ce programme a été créér dans le cadre du projet ANR DICWOC, afin de stocker automatiquement les données généré par le pipelines informatiques mise en place 
# par Yascim Kamel, dans la base de données dédiée au projet.  

#Afin de fonctionner ce programme necessite l'indication des paramètres dans l'ordre qui suit  : 
			# 1) L'identifiant de l'assemblage
			# 2) L'identifiant de l'experience mise en place
			# 3) Le chemin relatif ou absolu du fichier multifasta contenant les données à entrer dans la base de données.
			# 4) Le chemin relatif ou absolu de la table génes au format CSV
			# 5) Le chemin relatif ou absolu de la table link au format CSV
			# 6) Le chemin relatif ou absolu de la table de croisement contenant les génes de références pour une espèce au format CSV

######################################################################### Définition des fonctions ##############################################################################

def table_to_list(table, liste) :
	f=open (table, 'r')
	fichier=csv.reader(f)
	for row in fichier:
		liste.append(row)
	f.close()

def sim(seq1,seq2,match,missmatch,gap_ext,gap_int,id_gene1,id_gene2) : 
	matrice.matrice(seq1,seq2,match,missmatch,gap_ext,gap_int,id_gene1,id_gene2)
	backtracking.backtracking(seq1,seq2,gap_int,gap_ext,match,missmatch,id_gene1,id_gene2)
	pourc=calcul_similarité.similarite(id_gene1,id_gene2)
	return pourc

def list_to_table (liste, table):
	f=open(table, 'w')
	fichier=csv.writer(f)
	for row in liste:
		fichier.writerow(row)
	f.close()



######################################################################### Récupération des données d'entrées ########################################################################################################
assemblie_ID = sys.argv[1]
experience_ID= sys.argv[2]

table_gene=sys.argv[4]
table_link=sys.argv[5]
table_croisement=sys.argv[6]

croisement=[]
tbl_gene=[]
tbl_link=[]

###### Initialisation: conversion des tables en liste de listes ############# 

table_to_list(table_croisement, croisement)
table_to_list(table_gene, tbl_gene)
table_to_list(table_link,tbl_link)



########## Extraction des gènes contenue dans le fichier multi fasta sous forme de tableau à deux dimension (liste de liste) ###########

multi_fasta=sys.argv[3] 
tableau_gene=[]

if len(tbl_gene)==1: ## Si seulement le header est renseigner alors l'id du premier gène de la base de donénes sera 1. 
	id_gene=0
else :
	id_gene=int(tbl_gene[-1][0]) # Sinon id_gene = id max du csv +1

for record in SeqIO.parse(multi_fasta,"fasta"):### Utilisation de SeqIO de Biopython pour parcourir les séquences contenues dans les multifasta
	id_gene += 1
	header=str(record.id)# Récupération du header en chaîne de caractères.  
	split_header=header.split('|')### Récupération des informations contenue dans le header
	nom=split_header[0]
	famille=split_header[1]
	if len(split_header)==3 :
		etat="pseudogéne"
	else:
		etat="fonctionnel"
	position= nom.split(':')
	liste_position= position[1].split("-")
	start=liste_position[0]
	end=liste_position[1]


	gene=[id_gene,nom,'géne OR',famille,etat,int(start),int(end),str(record.seq),"" ]
	tableau_gene.append(gene) ## stockage des différents génes dans un tableau à deux dimension


######################################################################### Définition des paramètres d'alignement (calcul de similarité) #############################################################
match=2
missmatch=-2
gap_int=-1
gap_ext=0
  
######################################################################### Début de l'algorithme d'implémentation de la base de données ########################################################################################################

print('\n_________________________________________________________________________\n')

for gene in tableau_gene: ##Parcours de la liste de gènes trouvées par le pipeline
	print("Traitement du géne : ", gene[1], "\n")
	id_max=0
	sim_max=0
	for row in croisement[1:]:# parcours des gènes de références
		row[4]=re.sub("(\s+)","",row[4])
		pourcentage=sim(gene[7],row[4],match,missmatch,gap_ext,gap_int,gene[1],row[3]) ## Calcul de la similarité entre le géne testé et les références
		if pourcentage > sim_max :
			sim_max=pourcentage
			id_max=int(row[2])
	if sim_max>98:## géne de référence existant
		referenced_gene=gene
		referenced_gene[-1]=id_max
		tbl_gene.append(referenced_gene) ##Ajout des informations relatives au géne dans la table géne
		tbl_link.append([assemblie_ID, int(experience_ID), referenced_gene[0]]) ##Ajout des informations relative au géne, à l'experience et à l'assemlage dans la base de données 
	else:## nouveaux géne , sans référence
		non_referenced_gene=gene
		non_referenced_gene[-1]= non_referenced_gene[0]
		tbl_gene.append(non_referenced_gene)## Ajout du géne dans la table géne  
		tbl_link.append([assemblie_ID, experience_ID, non_referenced_gene[0]])# Ajout du géne dans la table link 
		croisement.append([assemblie_ID, int(experience_ID),non_referenced_gene[0],non_referenced_gene[1],non_referenced_gene[-2], non_referenced_gene[0]]) ## ajout du géne comme référence

	print(gene[1], " Traité")
	print('\n_________________________________________________________________________\n')
	
list_to_table(croisement,table_croisement)
list_to_table(tbl_gene,table_gene)
list_to_table(tbl_link,table_link)