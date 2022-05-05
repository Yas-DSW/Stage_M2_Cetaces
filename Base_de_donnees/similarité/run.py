####initialisation des valeurs choisies ############

import matrice,backtracking,calcul_similarité

id_gene1="gene 1"
id_gene2="géne 2"
seq1='''ACGTACGTGCAGTGACTGACACCACACGTGGCCAGTGACT'''
seq2='''ACGTGGCAGTAGAGACGATGAGACCCCAGTAGTGATGATGAGATG'''

match=2
missmatch=-2
gap_int=-1
gap_ext=0

matrice.matrice(seq1,seq2,match,missmatch,gap_ext,gap_int, id_gene1,id_gene2)
backtracking.backtracking(seq1,seq2,gap_int,gap_ext,match,missmatch,id_gene1,id_gene2)
calcul_similarité.similarite(id_gene1,id_gene2)
