#!/usr/bin/env python3

from Bio import SeqIO
import sys
import csv
import matrice,backtracking,calcul_similarité

#Afin de fonctionner ce programme necessite en entrée le nom (si le fichier se trouve dans le même dossier) ou le chemin des fichier suivants dans l'ordre indiqué : 
#			1) L'identifiant de l'assemblage déja rentré dans la table assemblage entre guillemet
#			2) L'identifiant de l'experience par laquelle les gènes ont été retrouvés
#			3) la table gene au format csv
#			4) la table link au format csv
#			5) la table croisement au format CSV 
#			6) la liste des gènes trouvés au format fasta

######################################################################### Définition des fonctions##############################################################################

def table_to_list(table, liste) :
	f=open (table, 'r')
	fichier=csv.reader(f)
	for row in fichier:
		liste.append(row)

def sim(seq1,seq2,match,missmatch,gap_ext,gap_int,id_gene1,id_gene2) : 
	matrice.matrice(seq1,seq2,match,missmatch,gap_ext,gap_int)
	backtracking.backtracking(seq1,seq2,gap_int,gap_ext,match,missmatch)
	calcul_similarité.similarite()
	return calcul_similarité.similarite
######################################################################### Définition des paramètres de l'alignement#############################################################
match=2
missmatch=-2
gap_int=-1
gap_ext=0

######################################################################### Récupération des données d'entrées ########################################################################################################
# assemblie_ID = sys.argv[1]
# experience_ID= sys.argv[2]

table_gene=sys.argv[3]
table_link=sys.argv[4]
table_croisement=sys.argv[2]

croisement=[]
tbl_gene=[]
tbl_link=[]

###### Initialisation: conversion des tables en liste de listes ############# 

table_to_list(table_croisement, croisement)
print(croisement)
table_to_list(table_gene, tbl_gene)
print(tbl_gene)
table_to_list(table_link,tbl_link)
print(tbl_link)


########## Extraction des gènes sous forme de liste ###########

multi_fasta=sys.argv[1]
liste_gene=[]
identifiant=1

for record in SeqIO.parse(multi_fasta,"fasta"): ### on utilise SeqIO de Biopython pour parcourir les séquences contenu dans les multifasta
	header=str(record.id) # La plupart des informations sur le géne sont contenues dans le header. On récupére celui-ci dans un format simple a manipuler par la suite. 
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
	if len(tbl_gene)=1:
		id_gene=identifiant
		identifiant+=1
	else :
		id_gene=int(tbl_gene[len(tbl_gene)-1]+1)

	gene=[id_gene,nom,"géne OR",famille,etat,int(start),int(end),str(record.seq),"" ]
	liste_gene.append(gene)

# print(liste_gene[1])  
# print(len(liste_gene)) #### test du bon fonctionnement de l'extarction


######################################################################### Début de l'algorithme ########################################################################################################

for gene in liste_gene:
	print(gene)
	id_max=0
	sim_max=0
	for row in croisement : 
		similarite=sim(gene[7],row)

		if similarite>= 0.98 :
			sim_max=similarite
			id_max=row[2]
	if sim_max>0.98:
		referenced_gene=gene
		referenced_gene[-1]=id_max #### ici on écrit l'ID de la séquence de référence dans la table gène 
		tbl_gene.append(gene)
		tbl_link.append([assemblie_ID, experience_ID, referenced_gene[0]]) #####Possiblement ici utiliser un transtypage pour referenced gene (selon la base de données)
	else:
		non_referenced_gene=gene
		non_referenced_gene[-1]= non_referenced_gene[0]
		tbl_gene.append(gene)
		tbl_link.append([assemblie_ID, experience_ID, non_referenced_gene[0]])
		croisement.append([assemblie_ID, experience_ID, non_referenced_gene[0],non_referenced_gene[0]]) 







