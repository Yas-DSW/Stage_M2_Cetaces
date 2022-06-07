def completion_gene(tmf,connection,ID_E,esp, ID_A):
	print ("\n Début de l'insertion des données dans les tables link et gene ...")
	#### Définition des valeurs utilisé dans l'alignement de la fonction sim
	match=2
	missmatch=-2
	gap_int=-1
	gap_ext=0

	list_comm_gene="INSERT INTO gene "
	list_comm_link="INSERT INTO link "

	cur=connection.cursor()
	
	requete="SELECT distinct link.ID_experience,link.ID_gene, gene.nom, gene.sequence, gene.reference FROM link,gene,assemblie WHERE link.ID_assemblie IN (SELECT assemblie.identifiant FROM assemblie WHERE espece='{espece}') AND link.ID_gene IN (SELECT gene.ID FROM gene WHERE gene.ID= gene.reference) AND link.ID_gene=gene.ID AND assemblie.identifiant=link.id_assemblie;"
	cur.execute(requete)
	tc=cur.fetchall()

	requete="SELECT max(id_gene) FROM gene"
	cur.execute(requete)
	Liste_ID_max=cur.fetchall() #### LA fonction fetchall retourne une liste de tuple
	IDg=Liste_ID_max[0][0]

	print('\n_________________________________________________________________________\n')

	for gt in tmf: ##Parcours de la liste des gènes trouvés par le pipeline
		print("Traitement du géne : ", gene[1], " Assemblage : "+ ID_A + "\n")
		gr_id_max=0
		gr_score_max=0
		sim_max=0
		IDg+=1
		lgt=len(gt)
		for gr in tc:# Parcours des gènes de références
			print("comparaison des gènes", gr, " et ", gt)
			gr_sequence=re.sub("(\s+)","",gr[-2])### élimination des caractéres invisibles pouvant êre contenu dans les séquences importés depuis la base. 
			# pourcentage=random.randrange(98,100)
			score_match=align( gt[-2], gr[-1] , -1 ,-1)
			if score_match[0] > gr_score_max:
				gr_score_max=score_match[0]
				nb_match=score_match[1]
		sim_max=nb_match/length

		if sim_max>0.98:## Géne de référence similaire à 98 % existant. Le géne de la table devient la référence	
				list_comm_gene+="("+str(IDg)+","+ str(gt[1])+",gène OR,"+ str(gt[3])+","+ str(gt[4])+"," +str(gt[5])+","+ str(gt[6])+","+str(gt[7])+","+str(IDg)+")"
		else :
				list_comm_gene+="("+str(IDg)+","+ str(gt[1])+",gène OR,"+ str(gt[3])+","+ str(gt[4])+"," +str(gt[5])+","+ str(gt[6])+","+str(gt[7])+","+str(IDg)+")"
		if gr == tc[-1]:
			list_comm_gene+=";"
			list_comm_link+="("+str(IDg)+","+str(ID_A)+","+str(ID_E)+");"
		else :
			list_comm_gene+=","
			list_comm_link+="("+str(IDg)+","+str(ID_A)+","+str(ID_E)+"),"

	cur.execute(list_comm_gene)
	connection.commit()

	cur.execute(list_comm_link)
	connection.commit()