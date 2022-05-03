import backtracking

def similarite():
	if len(backtracking.seq1_aff) > len(backtracking.seq2_aff) :
		longueur=len(backtracking.seq1_aff)
	else: 
		longueur=len(backtracking.seq2_aff)
	print("nb_match similarité :", backtracking.nb_match)
	print("longueur: ", longueur) 
	global similarite
	similarite=backtracking.nb_match/longueur

	print (similarite)