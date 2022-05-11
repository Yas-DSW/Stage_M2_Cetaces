#!/usr/bin/env python3

from Bio import SeqIO
import re
import sys
import csv
import psycopg2
import matrice,backtracking,calcul_similarité

# Ce programme a été créér dans le cadre du projet ANR DICWOC, afin de stocker automatiquement les données généré par le pipelines informatiques mise en place 
# par Yascim Kamel, dans la base de données dédiée au projet.  


######################################################################### Définition des fonctions ##############################################################################

# def table_to_list(table, liste) :
# 	f=open (table, 'r')
# 	fichier=csv.reader(f)
# 	for row in fichier:
# 		liste.append(row)
# 	f.close()

def sim(seq1,seq2,match,missmatch,gap_ext,gap_int,id_gene1,id_gene2) : 
	matrice.matrice(seq1,seq2,match,missmatch,gap_ext,gap_int,id_gene1,id_gene2)
	backtracking.backtracking(seq1,seq2,gap_int,gap_ext,match,missmatch,id_gene1,id_gene2)
	pourc=calcul_similarité.similarite(id_gene1,id_gene2)
	return pourc

# def list_to_table (liste, table):
# 	f=open(table, 'w')
# 	fichier=csv.writer(f)
# 	for row in liste:
# 		fichier.writerow(row)
# 	f.close()



######################################################################### Récupération des données d'entrées ########################################################################################################



#Connexion à la base de données
connection=psycopg2.connect("dbname=Whale\ eat user=yascim")

## Ouverture d'un curseur
cur=connection.cursor()


esp = sys.argv[1]
assemblie_ID = sys.argv[2]
experience_ID= sys.argv[3]

cur.execute("SELECT * FROM gene")
table_gene= cur.fetchall()
cur.execute("SELECT * FROM link")
table_link=cur.fetchall()

# print("table_gene : ", table_gene)
# print("table_link : ", table_link),



# ########## Extraction des gènes contenue dans le fichier multi fasta sous forme de tableau à deux dimension (liste de liste) ###########

multi_fasta=sys.argv[4] 
tableau_gene=[]

if len(table_gene)==0: ## Si seulement le header est renseigner alors l'id du premier gène de la base de donénes sera 1. 
	id_gene=0
else :
	id_gene=int(table_gene[-1][0]) # Sinon id_gene = id max du csv +1

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
# print("tableau gene  : ", tableau_gene)

# ######################################################################### Définition des paramètres d'alignement (calcul de similarité) #############################################################
match=2
missmatch=-2
gap_int=-1
gap_ext=0
  
# ######################################################################### Début de l'algorithme d'implémentation de la base de données ########################################################################################################

print('\n_________________________________________________________________________\n')

for gene in tableau_gene: ##Parcours de la liste de gènes trouvées par le pipeline
	print("Traitement du géne : ", gene[1], "\n")
	id_max=0
	sim_max=0
	print("Construction/mise à jour de la table croisement \n")
	requete_croisement=f"SELECT distinct link.ID_experience,link.ID_gene, gene.nom, gene.sequence, gene.reference FROM link,gene,assemblie WHERE link.ID_assemblie IN (SELECT assemblie.identifiant FROM assemblie WHERE espece='{esp}') AND link.ID_gene IN (SELECT gene.ID FROM gene WHERE gene.ID= gene.reference) AND link.ID_gene=gene.ID AND assemblie.identifiant=link.id_assemblie;"
	cur.execute(requete_croisement)
	table_croisement=cur.fetchall()

	# print("table_croisement : ", table_croisement)

	for row in table_croisement[1:]:# parcours des gènes de références
		bd_sequence=re.sub("(\s+)","",row[-2])
		pourcentage=sim(gene[7],row[-2],match,missmatch,gap_ext,gap_int,gene[1],row[2]) ## Calcul de la similarité entre le géne testé et les références
		if pourcentage > sim_max :
			sim_max=pourcentage
			id_max=row[1]
	if sim_max>98:## géne de référence existant
		gene[-1]=id_max
		gene=tuple(gene)
		requete="INSERT INTO gene VALUES " + str(gene)+ ';'
		print(requete)
		cur.execute(requete)
		print("gene : ", gene)
		print('gene[0] :', gene[0])
		link=(assemblie_ID, int(experience_ID),gene[0])
		requete="INSERT INTO link VALUES"+ str(link)+ ';'
		cur.execute(requete)
		connection.commit()
	else:## nouveaux géne , sans référence
		gene[-1]=gene[0]
		gene=tuple(gene)
		requete="INSERT INTO gene VALUES " + str(gene)+ ';'
		cur.execute(requete)
		link=(assemblie_ID, int(experience_ID),gene[0])
		requete="INSERT INTO link VALUES"+ str(link)+ ';'
		cur.execute(requete)
		connection.commit()
	print(gene[1], " Traité")
	print('\n_________________________________________________________________________\n')