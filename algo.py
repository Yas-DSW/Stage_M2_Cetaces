Entrée : Table Géne et link, liste de gènes


for seq in liste :
	dictionnary={}	
	interm=[]
	interm.append(seq)
	remove_of_liste(seq)
	for next_seq in liste :
		intermediate(seq, next_seq)## compare, add fasta seqence to "interm" list and remove of "liste" list if similarity > 98%
	for interm_seq in interm :	
		classification(interm_seq) ## add gene family number like key to the dictionnary if doesn't exist, else add seq to the correct key
	reference=retrieve_seq_family(dictionnary)## retrieve the first sequence of the family who have the lower family number to make a reference
	for key in dictionnary :

		add_to_BD(dictionnary[key][1])### Verification that the first sequence (associated to the same family) isn't in the table (compare to 98%). In this case add informations (Name,family,sequence) to Gene table and complete gene ID link table in consequence.
		count_gen_pseudo(dictionnary[key])#### Count the number of gene and pseudogene in the list of sequences associated to an key and add to "link" table.






lower=retrieve_seq_family(seq)## retrieve sequence of the family who have the lower family number



liste_esp=[]

for liste in LL :
	if liste.assemblie not in Assemblie: 
		Fillrow(assemblie)

	esp=Assemblie.column["espece"]
	Ass=Assemblie.column["ID"]

	Fillrow(experience)

	if esp not in liste_esp:  #### Checher si le géne est déja dans la table : rajouter un champs dans la table organisme
		for seq in liste:
			Fillrow(gene)

	else : 
		for seq in liste : 
			croisement=cross(Géne; Assemblie) where espece=esp  #### prendre que les génes de référence

		i=0
		While i <= len(croisement) :
			if i< len(croisement):
				seqrow=row[i].seq
				percent=(compare(seq,seqrow))
				if percent >=98 : 
					id=row.ref
					for row in Géne: 
						if row.ref=id:
							row exemplaire +=1
							exemplaire =row.exemplaire
						if seq.famille=row.famille:
							fam=seq.famille
						else:
							fam =-1 #### peut être remplacer par -(seq.fam)

					Fillrow(gene, gene.exemplaire=exemplaire, gene.famille=fam, gene.ref = id , sim=percent)
					i=len(croisement)+1
				elif i=len(croismeent): 
					Fillrow(gene)
				else : 
					i+=1



### Rajouter le nombre d'experience dans organisme
### supprimer de gene 