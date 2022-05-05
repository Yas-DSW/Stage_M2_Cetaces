#!/usr/bin/env python3

from Bio import SeqIO
import re
import sys
import csv
import matrice,backtracking,calcul_similarité

#Afin de fonctionner ce programme necessite en entrée le nom (si le fichier se trouve dans le même dossier) ou le chemin des fichier suivants dans l'ordre indiqué : 
#			1) L'identifiant de l'assemblage déja rentré dans la table assemblage entre guillemet
#			2) L'identifiant de l'experience par laquelle les gènes ont été retrouvés
#			3) la table gene au format CSV
#			4) la table link au format CSV
#			5) la table croisement au format CSV 
#			6) la liste des gènes trouvés au format fasta

######ordre à refaire

######################################################################### Définition des fonctions##############################################################################

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


######################################################################### Définition des paramètres de l'alignement#############################################################
match=2
missmatch=-2
gap_int=-1
gap_ext=0

######################################################################### Récupération des données d'entrées ########################################################################################################
assemblie_ID = sys.argv[5]
experience_ID= sys.argv[6]

table_gene=sys.argv[3]
table_link=sys.argv[4]
table_croisement=sys.argv[2]

croisement=[]
tbl_gene=[]
tbl_link=[]

###### Initialisation: conversion des tables en liste de listes ############# 

table_to_list(table_croisement, croisement)
# print("croisement :", croisement)
table_to_list(table_gene, tbl_gene)
# print("table gene : ", tbl_gene)
table_to_list(table_link,tbl_link)
# print("tablé link :", tbl_link)


########## Extraction des gènes sous forme de liste ###########

multi_fasta=sys.argv[1]
liste_gene=[]
identifiant=1
for record in SeqIO.parse(multi_fasta,"fasta"):
 ### on utilise SeqIO de Biopython pour parcourir les séquences contenu dans les multifasta
	header=str(record.id)
# La plupart des informations sur le géne sont contenues dans le header. On récupére celui-ci dans un format simple a manipuler par la suite. 
	split_header=header.split('|')### Une majorité des informations de l'entête en sortie de ORA sont séparéé par un pipe et donc facilement récupérable grâce à la fonction split() de python.
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
	if len(tbl_gene)==1:
		id_gene=identifiant
		identifiant+=1
	else :
		id_gene=int(tbl_gene[-1][0])+1

	gene=[id_gene,nom,'géne OR',famille,etat,int(start),int(end),str(record.seq),"" ]
	liste_gene.append(gene)

# print(liste_gene[1])  
# print(len(liste_gene)) #### test du bon fonctionnement de l'extarction


######################################################################### Début de l'algorithme ########################################################################################################
# print("table link initial",tbl_link)
for gene in liste_gene:
	print("Traitement du géne : ", gene[1])
	id_max=0
	sim_max=0
	for row in croisement[1:]:
		# print("row :",row, "row[4]: ", row[4])
		row[4]=re.sub("(\s+)","",row[4])
		pourcentage=sim(gene[7],row[4],match,missmatch,gap_ext,gap_int,gene[1],row[3])
		if pourcentage > sim_max :
			sim_max=pourcentage
			id_max=int(row[2])
	if sim_max>98:
		# print("id_max :", id_max)
		referenced_gene=gene
		referenced_gene[-1]=id_max #### ici on écrit l'ID de la séquence de référence dans la table géne
		tbl_gene.append(referenced_gene)
		# print("referenced_gene :", referenced_gene )
		tbl_link.append([assemblie_ID, int(experience_ID), referenced_gene[0]]) #####Possiblement ici utiliser un transtypage pour referenced gene (selon la base de données)
		# print("table link:",tbl_link)	
	else:
		non_referenced_gene=gene
		non_referenced_gene[-1]= non_referenced_gene[0]
		# print("non_referenced_gene : ", non_referenced_gene)
		tbl_gene.append(non_referenced_gene)
		# print("table gene non_referenced_gene : ", tbl_gene)
		tbl_link.append([assemblie_ID, experience_ID, non_referenced_gene[0]])
		# print("table link non_referenced_gene :", tbl_link)
		croisement.append([assemblie_ID, int(experience_ID),non_referenced_gene[0],non_referenced_gene[1],non_referenced_gene[-2], non_referenced_gene[0]])

	print(gene[1], " Traité")
	print('_________________________________________________________________________')

list_to_table(croisement,table_croisement)
list_to_table(tbl_gene,table_gene)
list_to_table(tbl_link,table_link)