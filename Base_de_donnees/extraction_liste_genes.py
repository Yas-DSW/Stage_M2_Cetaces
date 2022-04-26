#!/usr/bin/env python3

from Bio import SeqIO
import sys

#Afin de fonctionner ce programme necessite en entrée le nom (si le fichier se trouve dans le même dossier) ou le chemin des fichier suivants dans l'ordre indiqué : 
#			1) L'identifiant de l'assemblage déja rentré dans la table assemblage entre guillemet
#			2) L'identifiant de l'experience par laquelle les gènes ont été retrouvés
#			3) la table gene au format csv
#			4) la table link au format csv
#			5) la table croisement au format CSV 
#			6) la liste des gènes trouvés au format fasta

######################################################################### Récupération des données d'entrées ########################################################################################################
assemblie = sys.argv[1]
experience= sys.argv[2]
table_gene=sys.argv[3]
table_link=sys.argv[4]
table_croisement=sys.argv[5]

###### Conversion de la table croisement en liste ############# 



########## Extraction des gènes sous forme de liste ###########

multi_fasta=sys.argv[6]
liste_gene=[]

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

	gene=["",nom,famille,etat,int(start),int(end),str(record.seq),"Géne OR","" ]
	liste_gene.append(gene)

# print(liste_gene[1])  
# print(len(liste_gene)) #### test du bon fonctionnement de l'extarction


######################################################################### Début de l'algorithme ########################################################################################################

for gene in liste_gene:
	id_max=0
	sim_max=0
	for row in croisement : 
		if sim (ro)


