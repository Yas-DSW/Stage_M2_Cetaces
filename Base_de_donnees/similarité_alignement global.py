###########matrix############
import numpy


####"initialisation des valeurs choisies
seq1='CGTAGCTT'
seq2='AGGCT'
match=2
missmatch=-1
gap=0

def matrice(seq1,seq2,match,missmatch,gap):
	
	global n
	n=len(seq1)
	global m
	m=len(seq2)
	mat=numpy.zeros((m+1,n+1), dtype=int) #Construction d'une matrice de taille (m+1)*(n+1) avec numpy 

	#Initialisation de la première valeur de la matrice à zéro
	
	mat[0,0]=0
	

	for i in range (1,m+1) :mat[i,0]=mat[i-1,0]+gap #remplissage de la première ligne
	for j in range(1, n+1) :mat[0,j]=mat[0,j-1]+gap#remplissage de la première colonne

	#Remplissage de la matrice 
	for j in range(1,n+1) :
		for i in range (1,m+1) :
			if (seq1[j-1]==seq2[i-1]):diag=(mat[i-1,j-1]+match) #match
			else : diag=(mat[i-1,j-1]+missmatch)
			horz=(mat[i-1,j]+gap)
			vert=(mat[i,j-1]+gap)
			if (diag>=horz and diag>=vert):mat[i,j]=diag
			elif (horz>= diag and horz>=vert):mat[i,j]=horz
	
			else:mat[i,j]=vert
	
	global score
	score=mat[m,n]
	print(mat)
	print(m)



def similarite():
	if n > m :
		longueur= n
	else: 
		longueur=m

	similarite=score/longueur

	return similarite

def comparaison(seq1,seq2,match,missmatch,gap):
	matrice(seq1,seq2,match,missmatch,gap)
	pourcentage=similarite()
	print(pourcentage)

comparaison(seq1,seq2,match,missmatch,gap)