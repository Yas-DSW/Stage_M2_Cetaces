import numpy
def matrice(seq1,seq2,match,missmatch,gap_ext, gap_int,id_gene1,id_gene2):##### Fonction permettant de construire la matrice de score nécessaire à  l'alignement.
	print ("Construction de la matrice d'alignement pour : " + id_gene1 + " et " + id_gene2 +" ...\n")
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
	print("Matrice terminée ! \n")