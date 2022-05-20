#!/usr/bin/env python3

# Ce programme a été créer par Yascim Kamel dans le cadre de son stage de Master 2 au cours du projet ANR DICWOC porté 
# par Aurélie Célérier et Sylvia Campagna. Il permet de lancer les programmes d'implémentation de la base de données associée au projet.

from Bio import SeqIO
from Bio import pairwise2
import re
import sys
import psycopg2 
# import matrice,backtracking,calcul_similarité
import random
from datetime import datetime 

def my_format_alignment(align1, align2, score, begin, end): ## Code inspirée de Bastien Hervé sur https://www.biostars.org/p/370710/
    s = [score] 
    match=0
    for a, b in zip(align1[begin:end], align2[begin:end]): 
        if a == b:  
            match+=1
    s.append(match)
    return s ### Retourne une liste [score, match]

def align(seq1, seq2, open_gap, extend_gap ):
	score = pairwise2.align.globalxs(seq1, seq2,open_gap,extend_gap,penalize_end_gaps=(False,False), score_only=True)
	return my_format_alignment(score)






# def sim(seq1,seq2,match,missmatch,gap_ext,gap_int,id_gene1,id_gene2) : ### Définition de la fonction de calcul du pourcentage de similarité entre deux séquences
# 	now =datetime.now()
# 	current_time=now.strftime("%H:%M:%S")
# 	print("Curent time matrice begin :", current_time)
# 	matrice.matrice(seq1,seq2,match,missmatch,gap_ext,gap_int,id_gene1,id_gene2) #### Calcul de la matrice de score entre les deux séquences
# 	now =datetime.now()
# 	current_time=now.strftime("%H:%M:%S")
# 	print("Curent time matrice end:", current_time)
# 	now =datetime.now()
# 	current_time=now.strftime("%H:%M:%S")
# 	print("Curent time  start backtracking:", current_time)
# 	backtracking.backtracking(seq1,seq2,gap_int,gap_ext,match,missmatch,id_gene1,id_gene2) ### Etape de backtracking permettant de connaitre le nombre de match
# 	print("backtracking terminé !\n")
# 	now =datetime.now()
# 	current_time=now.strftime("%H:%M:%S")
# 	print("Curent time backtracking end :", current_time) 
# 	pourc=calcul_similarité.similarite(id_gene1,id_gene2) ### Calcul de la similarité entre les sséquence (score pondéré par la longueur)
# 	return pourc



######################################################################### Récupération des données d'entrées ########################################################################################################


def recup_donnees(connection):
	print ("\nrécupération des données de la table gene et la table link ...")
	cur=connection.cursor()
	cur.execute("SELECT id from experience;")
	liste_exp=cur.fetchall() ## Récupération des résultats de la requête sous forme de liste de tuples
	global experience_ID
	experience_ID=liste_exp[-1][0]
	cur.execute("SELECT * FROM gene")
	global table_gene
	table_gene= cur.fetchall()
	cur.execute("SELECT * FROM link")
	global table_link
	table_link=cur.fetchall()


########### Conversion du fichier multi fasta en tableau à deux dimensions  ###########


def conversion_multifasta(multi_fasta,table_gene,table_link):
	global tableau_gene
	tableau_gene=[]

	## Récupération de l'identifiant du dernier génes entré
	if len(table_gene)==0: 
		id_gene=0
	else :
		id_gene=int(table_gene[-1][0]) # Sinon id_gene = id max du csv +1

	for record in SeqIO.parse(multi_fasta,"fasta"):### Utilisation de SeqIO de Biopython pour parcourir les séquences fasta contenues dans le multifasta
		id_gene += 1
		header=str(record.id)# Récupération du header de la séquence fasta en chaîne de caractères.  
		split_header=header.split('|')### Récupération des informations contenues dans le header
		nom=split_header[0]
		famille=split_header[1]
		if len(split_header)==3 : ### L'état de pseudogéne apparait dans le header contrairement à l'état fonctionnel 
			etat="pseudogéne"
		else:
			etat="fonctionnel"
		position= nom.split(':')
		liste_position= position[1].split("-")
		start=liste_position[0]
		end=liste_position[1]

		gene=[id_gene,nom,'géne OR',famille,etat,int(start),int(end),str(record.seq),"" ]
		tableau_gene.append(gene) ## Stockage des différents génes dans un tableau à deux dimensions
	# print("tableau gene  : ", tableau_gene)
	

########################################################################## Définition des paramètres d'alignement (calcul de similarité) #############################################################


def completion_gene(tableau_gene,connection,experience_ID,espece, assemblie_ID):
	print ("\n Début de l'insertion des données dans les tables link et gene ...")
	#### Définition des valeurs utilisé dans l'alignement de la fonction sim
	match=2
	missmatch=-2
	gap_int=-1
	gap_ext=0
	cur=connection.cursor()

	print('\n_________________________________________________________________________\n')

	for gene in tableau_gene: ##Parcours de la liste des gènes trouvés par le pipeline
		print("Traitement du géne : ", gene[1], " Assemblage : "+ assemblie_ID + "\n")
		id_max=0
		sim_max=0
		length=len(gene)
		print("Construction/mise à jour de la table croisement \n")
		requete_croisement=f"SELECT distinct link.ID_experience,link.ID_gene, gene.nom, gene.sequence, gene.reference FROM link,gene,assemblie WHERE link.ID_assemblie IN (SELECT assemblie.identifiant FROM assemblie WHERE espece='{espece}') AND link.ID_gene IN (SELECT gene.ID FROM gene WHERE gene.ID= gene.reference) AND link.ID_gene=gene.ID AND assemblie.identifiant=link.id_assemblie;"
		cur.execute(requete_croisement)
		table_croisement=cur.fetchall()

		for row in table_croisement[1:]:# Parcours des gènes de références
			bd_sequence=re.sub("(\s+)","",row[-2])### élimination des caractéres invisibles pouvant êre contenu dans les séquences importés depuis la base. 
			# pourcentage=random.randrange(98,100)
			score_align=align( gene, row , -1 ,-1)
			if score_align[0] > score_max:
				score_max=score_align[0]
				nb_match=score_align[1]

		sim_max=nb_match/length
			# pourcentage=sim(gene[7],row[-2],match,missmatch,gap_ext,gap_int,gene[1],row[2]) ## Calcul de la similarité entre le géne testé et les références de la base. 
			# if pourcentage > sim_max :
			# 	sim_max=pourcentage
			# 	id_max=row[1]
		if sim_max>98:## Géne de référence similaire à 98 % existant. Le géne de la table devient la référence
			gene[-1]=id_max
			gene=tuple(gene)
			requete="INSERT INTO gene VALUES " + str(gene)+ ';'
			cur.execute(requete)
			link=(assemblie_ID, experience_ID,gene[0])
			requete="INSERT INTO link VALUES"+ str(link)+ ';'
			cur.execute(requete)
			connection.commit() ## envoi des données sur la base
		else:## Nouveau géne, sans référence
			gene[-1]=gene[0]
			gene=tuple(gene)
			requete="INSERT INTO gene VALUES " + str(gene)+ ';'
			cur.execute(requete)
			link=(assemblie_ID, experience_ID,gene[0])
			requete="INSERT INTO link VALUES"+ str(link)+ ';'
			cur.execute(requete)
			connection.commit()## envoi des données sur la base. 
		print(gene[1], " Traité")
		print('\n_________________________________________________________________________\n')

	print("\nAssemblie " + assemblie_ID +" entièrement traité.")

def multi_fasta_to_bd(multi_fasta, connection, espece,assemblie_ID): ### fonction d'appelle de toutes les autres fonctions
	recup_donnees(connection)
	conversion_multifasta(multi_fasta,table_gene,table_link)
	completion_gene(tableau_gene,connection, experience_ID, espece,assemblie_ID)