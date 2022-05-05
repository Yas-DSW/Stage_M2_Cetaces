import matrice

def match_or_missmatch(a,b,seq1,seq2,match,missmatch):
	cout_m=0
	if (seq1[b]==seq2[a]):
		cout_m= match
	else :
		cout_m=missmatch
	return (cout_m)

def backtracking(seq1,seq2, gap_int,gap_ext,match,missmatch,id_gene1,id_gene2):
	print("début de l'étape de backtracking entre "+  id_gene1 + " et " + id_gene2 +" ...")
	i=len(seq2)
	j=len(seq1)
	a=i-1
	b=j-1
	global nb_match
	nb_match=0

	### Un affichage des séquences a été réaliser pour vérifier l'adéquation de l'alignement avec les séquences. Le code correspondant à été mis en commentaire dans la fonction backtracking.	
	global seq1_aff
	seq1_aff=""
	global	seq2_aff
	seq2_aff=""
	
	while i > 0 or j > 0:
		if i == 0 or i == matrice.m:
			gap_horz=gap_ext
		else:
			gap_horz=gap_int
		if j==0 or j==matrice.n:
			gap_ver=gap_ext
		else:
			gap_ver=gap_int

		if (i>0 and j>0 and matrice.mat[i,j]==matrice.mat[i-1,j-1] + match_or_missmatch(a,b,seq1,seq2,match,missmatch)):
			seq1_aff=seq1[b]+seq1_aff
			seq2_aff=seq2[a]+seq2_aff
			if (match_or_missmatch(a, b,seq1,seq2,match,missmatch) == match):
				nb_match+=1
			if a>0:
				a=a-1
			if b>0:
				b=b-1
			i=i-1
			j=j-1 
			
			
			#gap &vert
		elif (i>0 and matrice.mat[i,j]==matrice.mat[i-1,j]+ gap_ver) :
			seq1_aff=("-")+seq1_aff
			seq2_aff=seq2[a]+seq2_aff
			if a>0:
				a=a-1
			i=i-1
		#gap & horz
		elif (j>0 and matrice.mat[i,j]==matrice.mat[i,j-1]+gap_horz):
			seq1_aff=(seq1[b])+seq1_aff
			seq2_aff=("-")+seq2_aff
			if b>0:
				b=b-1	
			j=j-1
	print("backtracking terminé !")
