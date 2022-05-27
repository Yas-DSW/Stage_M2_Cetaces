import backtracking

def similarite(id_gene1,id_gene2):

	if len(backtracking.seq1_aff) > len(backtracking.seq2_aff) :
		longueur=len(backtracking.seq1_aff)
	else: 
		longueur=len(backtracking.seq2_aff)
	similarite=(backtracking.nb_match/longueur)*100
	print ("La similarité entre " + id_gene1 + " et " + id_gene2 + " est de " + str(round(similarite,2)) + " %")
	return similarite
	