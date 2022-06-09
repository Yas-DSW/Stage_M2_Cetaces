#!/usr/bin/env python3

# Ce programme a été créer par Yascim Kamel dans le cadre de son stage de Master 2 au cours du projet ANR DICWOC porté 
# par Aurélie Célérier et Sylvia Campagna. Il permet de lancer les programmes d'implémentation de la base de données associée au projet.

from Bio import SeqIO
from Bio import pairwise2
import re
import sys
import psycopg2 




def my_format_alignment(align1, align2, score):
	s = [score] 
	match=0
	i=0
	if len(align1)==len(align2):
		while i<len(align1):
			if align1[i]==align2[i] and align1[i]!="-" and align2[i]!="-":
				match+=1
			i+=1
		s.append(match)
	else:
		print("Erreur : les alignements passés en argument ne sont pas de la même longueur ")
	return s

def align(seq1, seq2, open_gap, extend_gap ):
	score = pairwise2.align.globalxs(seq1, seq2,open_gap,extend_gap,penalize_end_gaps=(False,False))

	return my_format_alignment(score[0][0], score[0][1], score[0][2])




########### Conversion du fichier multi fasta en tableau à deux dimensions  ###########


def conversion_multifasta(multi_fasta):
	global tableau_gene
	tableau_gene=[]

	## Récupération de l'identifiant du dernier génes entré
	# if len(table_gene)==0: 
	# 	id_gene=0
	# else :
	# 	id_gene=int(table_gene[-1][0]) # Sinon id_gene = id max du csv +1

	for record in SeqIO.parse(multi_fasta,"fasta"):### Utilisation de SeqIO de Biopython pour parcourir les séquences fasta contenues dans le multifasta
		# id_gene += 1
		header=str(record.id)# Récupération du header de la séquence fasta en chaîne de caractères.  
		split_header=header.split('|')### Récupération des informations contenues dans le header
		nom=split_header[0]
		famille=split_header[1]
		if len(split_header)==3 : ### L'état de pseudogéne apparait dans le header contrairement à l'état fonctionnel 
			etat="pseudogène"
		else:
			etat="fonctionnel"
		# position= nom.split(':')
		# liste_position= position[1].split("-")
		# start=liste_position[0]
		# end=liste_position[1]

		# gene=[id_gene,nom,'géne OR',famille,etat,int(start),int(end),str(record.seq),"" ]
		gene=["",nom,'gène OR',famille,etat, "NULL","NULL",str(record.seq),"" ]
		tableau_gene.append(gene) ## Stockage des différents génes dans un tableau à deux dimensions
	# print("tableau gene  : ", tableau_gene)
	

########################################################################## Définition des paramètres d'alignement (calcul de similarité) #############################################################


def completion_gene(tmf,connection,ID_E,esp, ID_A):
	print ("\n Début de l'insertion des données dans les tables link et gene ...")
	#### Définition des valeurs utilisé dans l'alignement de la fonction sim
	match=2
	missmatch=-2
	gap_int=-1
	gap_ext=0


	list_comm_gene="INSERT INTO public.gene VALUES "
	list_comm_link="INSERT INTO public.link VALUES "

	cur=connection.cursor()
	requete="SELECT distinct gene.\"ID\", gene.\"Nom\", gene.\"Séquence\" FROM gene WHERE gene.\"ID\" in (SELECT link.\"ID gène\" FROM link Where link.\"ID assemblie\" in (SELECT assemblie.\"ID\" FROM assemblie WHERE \"Espèce\"=\'"+espece+"\') AND link.\"ID gène\" in (SELECT gene.\"ID\" FROM gene WHERE gene.\"ID\" = gene.\"Référence\"));"
	# requete="SELECT distinct link.ID_experience,link.ID_gene, gene.nom, gene.sequence, gene.reference FROM link,gene,assemblie WHERE link.ID_assemblie IN (SELECT assemblie.identifiant FROM assemblie WHERE espece='"+ espece +"') AND link.ID_gene IN (SELECT gene.ID FROM gene WHERE gene.ID= gene.reference) AND link.ID_gene=gene.ID AND link.ID_assemblie=assemblie.identifiant ;"
	cur.execute(requete)
	tc=cur.fetchall()
	IDg=0 #### Initialisation de IDg

	requete="SELECT max(\"ID\") FROM gene"
	cur.execute(requete)
	Liste_ID_max=cur.fetchall() #### LA fonction fetchall retourne une liste de tuple
	IDg=Liste_ID_max[0][0]#### Mise à jour de IDg



	for gt in tmf: ##Parcours de la liste des gènes trouvés par le pipeline
		print('\n_________________________________________________________________________\n')
		
		print("\nTraitement du géne : ", gt[1], " Assemblage : "+ ID_A + "\n")
		gr_id_max=""
		gr_score_max=0
		sim_max=0
		nb_match=0
		IDg+=1
		lgt=len(gt[-2])
		
		for gr in tc:# Parcours des gènes de références
			print("Comparaison entre :", gt[1] , " et ", gr[1] , "…")
			gr_sequence=re.sub("(\s+)","",gr[1])### élimination des caractéres invisibles pouvant être contenu dans les séquences importés depuis la base. 
			# pourcentage=random.randrange(98,100)
			score_match=align( gt[-2], gr[2] , -1 ,-1)
			print('score_match[0]', score_match[0], "score_match[1] :", score_match[1])
			if score_match[0] > gr_score_max:
				gr_id_max=gr[0]
				gr_score_max=score_match[0]
				nb_match=score_match[1]
			sim_max=nb_match/lgt

		if sim_max>0.98:## Géne de référence similaire à 98 % existant. Le géne de la table devient la référence
				print("\n Gène référent déja présent\n")	
				list_comm_gene+="("+str(IDg)+",'"+ str(gt[1])+",'"++"'," str(gt[3])+"','"+ str(gt[4])+"'," +str(gt[5])+","+ str(gt[6])+",'"+str(gt[7])+"',"+str(gr_id_max)+")"
		else :
				print("\n Gène \n")
				list_comm_gene+="("+str(IDg)+",'"+ str(gt[1])+"','gèneOR','"+ str(gt[3])+"','"+ str(gt[4])+"'," +str(gt[5])+","+ str(gt[6])+",'"+str(gt[7])+"',"+str(IDg)+")"
		if gt == tmf[-1]:#### 
			list_comm_gene+=";"
			list_comm_link+="('"+str(ID_A)+"',"+str(ID_E)+","+str(IDg)+");"
		else :
			list_comm_gene+=","
			list_comm_link+="('"+str(ID_A)+"',"+str(ID_E)+","+str(IDg)+"),"


	cur.execute(list_comm_gene)
	connection.commit()

	cur.execute(list_comm_link)
	connection.commit()

	print(gt[1], " Traité")
	print('\n_________________________________________________________________________\n')

	print("\nAssemblie " + assemblie_ID +" entièrement traité.")

def multi_fasta_to_bd(multi_fasta, connection, experience_ID, espece,assemblie_ID): ### fonction d'appelle de toutes les autres fonctions
	# recup_donnees(connection)
	conversion_multifasta(multi_fasta)
	completion_gene(tableau_gene,connection, experience_ID, espece,assemblie_ID)

################################## Main #########################################################
connection = psycopg2.connect("dbname='CeGeC' user=postgres host='localhost' port='5433'")

nom_complet=sys.argv[1] ### Récupération du nom de l'assemblage

BD=sys.argv[2] ## Récupération de la base de données sur laquelle les données ont été trouvées
esp_genre=nom_complet.split("_")

espece=esp_genre[1]
genre=esp_genre[0]

assemblie_ID= sys.argv[3]

# score_busco=sys.argv[3]
multi_fasta=sys.argv[4]
experience_ID=sys.argv[5]

multi_fasta_to_bd(multi_fasta,connection,experience_ID,espece,assemblie_ID)