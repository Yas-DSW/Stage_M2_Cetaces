#!/usr/bin/env python3

from Bio import SeqIO
from Bio import pairwise2

# def align(seq1, seq2, open_gap, extend_gap ):
# 	score = pairwise2.align.globalxs(seq1, seq2,open_gap,extend_gap,penalize_end_gaps=(False,False))
# 	print("score : ", score)
# 	print( "retourner:", score[0][seqA], score[0][seqB], score[0][score])
def align(seq1, seq2, open_gap, extend_gap ):
	score = pairwise2.align.globalxs(seq1, seq2,open_gap,extend_gap,penalize_end_gaps=(False,False))
	print("score : ", score[0][2])


align('GTATGTGGCCGTCTGTCA','CTATGTGGCCATCTGCCA', -1,-1)
