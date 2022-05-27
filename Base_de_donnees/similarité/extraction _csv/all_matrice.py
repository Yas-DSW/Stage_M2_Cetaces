########### Construction de la matrice ################
import numpy


# ####"initialisation des valeurs choisies
# seq1='''ACGTACGTGCAGTGACTGACACCACACGTGGCCAGTGACT'''
# seq2='''ACGTGGCAGTAGAGACGATGAGACCCCAGTAGTGATGATGAGATG'''
# match=2
# missmatch=-2
# gap_int=-1
# gap_ext=0

def matrice(seq1,seq2,match,missmatch,gap_ext, gap_int):##### Fonction permettant de construire la matrice de score nécessaire à  l'alignement.
	global n
	n=len(seq1)
	global m
	m=len(seq2)
	global mat
	mat=numpy.zeros((m+1,n+1), dtype=int) #Construction d'une matrice de taille (m+1)*(n+1) avec numpy 

	#Initialisation de la première valeur de la matrice à zéro
	
	mat[0,0]=0
	

	for i in range (1,m+1) :mat[i,0]=mat[i-1,0]+gap_ext #remplissage de la première ligne
	for j in range(1, n+1) :mat[0,j]=mat[0,j-1]+gap_ext #remplissage de la première colonne

	#Remplissage de la matrice 
	for j in range(1,n+1) :
		for i in range (1,m+1) :
			if (seq1[j-1]==seq2[i-1]):diag=(mat[i-1,j-1]+match) #match
			else : diag=(mat[i-1,j-1]+ missmatch)

			if i==m:
				vert=(mat[i,j-1]+gap_ext)
			else :
				vert=(mat[i,j-1]+gap_int)
			if j==n:
				horz=(mat[i-1,j]+gap_ext)
			else : 
				horz=(mat[i-1,j]+gap_int)

			if (diag>=horz and diag>=vert):mat[i,j]=diag
			elif (horz>= diag and horz>=vert):mat[i,j]=horz
			else:mat[i,j]=vert
	print(mat)
	
def match_or_missmatch(a,b):
	cout_m=0
	if (seq1[b]==seq2[a]):
		cout_m= match
	else :
		cout_m=missmatch
	return (cout_m)

def backtracking(seq1,seq2):
	i=len(seq2)
	j=len(seq1)
	a=i-1
	b=j-1
	global nb_match
	nb_match=0
	global seq1_aff
	seq1_aff=""
	global seq2_aff
	seq2_aff=""
	
	
	while i > 0 or j > 0:
		if i == 0 or i == m:
			gap_horz=gap_ext
		else:
			gap_horz=gap_int
		if j==0 or j==n:
			gap_ver=gap_ext
		else:
			gap_ver=gap_int

		if (i>0 and j>0 and mat[i,j]==mat[i-1,j-1] + match_or_missmatch(a,b)):
			seq1_aff=seq1[b]+seq1_aff
			seq2_aff=seq2[a]+seq2_aff
			if (match_or_missmatch(a, b) == match):
				nb_match+=1
			if a>0:
				a=a-1
			if b>0:
				b=b-1
			i=i-1
			j=j-1 
			
			
			#gap &vert
		elif (i>0 and mat[i,j]==mat[i-1,j]+ gap_ver) :
			seq1_aff=("-")+seq1_aff
			seq2_aff=seq2[a]+seq2_aff
			if a>0:
				a=a-1
			i=i-1
		#gap & horz
		elif (j>0 and mat[i,j]==mat[i,j-1]+gap_horz):
			seq1_aff=(seq1[b])+seq1_aff
			seq2_aff=("-")+seq2_aff
			if b>0:
				b=b-1	
			j=j-1
	

def similarite():
	if len(seq1_aff) > len(seq2_aff) :
		longueur=len(seq1_aff)
	else: 
		longueur=len(seq2_aff)
	print("longueur :", longueur)
	similarite=nb_match/longueur

	return similarite

def comparaison(seq1,seq2,match,missmatch,gap_ext, gap_int):
	matrice(seq1,seq2,match,missmatch,gap_ext, gap_int)
	backtracking(seq1,seq2)
	pourcentage=similarite()
	print(pourcentage)

comparaison(seq1,seq2,match,missmatch,gap_ext, gap_int)