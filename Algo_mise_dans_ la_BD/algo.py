Entrée : Table Géne et link, dictionnaire de gènes


for seq in liste :
	family_dictionnary={}	
	interm=[]
	interm.append(seq)
	remove_of_liste(seq)
	for next_seq in liste :
		intermediate(seq, next_seq)## compare, add fasta sequence to "interm" list and remove of "liste" list if similarity > 98%
	for interm_seq in interm :	
		classification(interm_seq) ## add gene family number like key to the family_dictionnary if doesn't exist, else add seq to the correct key
	reference=retrieve_seq_family(dictionnary)## retrieve the first sequence of the family who have the lower family number to make a reference
	for key in dictionnary :

		add_to_BD(dictionnary[key][1])### Verification that the first sequence (associated to the same family) isn't in the table (compare to 98%). In this case add informations (Name,family,sequence,ref) to Gene table and complete gene ID link table in consequence.
		count_gen_pseudo(dictionnary[key])#### Count the number of gene and pseudogene in the list of sequences associated to an key and add to "link" table.
