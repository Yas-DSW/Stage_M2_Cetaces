
from Bio import SeqIO
from Bio import pairwise2
import re
import sys
import psycopg2 


gt='GAAAGCAGTCTCATCTGTGATGCTGGGGCCACCCTACAACCATACAATGGAACCCCCTGCCACCTTGTCCTGGTGGGTATTCCAGGTTTGCAATCTTCACATCTTTGGCTGGTTACCTCACTGAACATCATGTATACCATAGCCCTGTTAGAAAACACCCTCATAGTGACTGTAATGTGGATGGATTCCACCCTACAAGAGCCCATGTACTGCTCCCTGGATATTCTGGCTGCTGTGGACACTGTCATGGCTTCCTTGGTAGCGCCCAAGATGGTGAGCATTTTCTCCTTAGGAGACAGCTTCATCAGCTTTAATGCTTGTTTCACTCAGATGTATTTTGTCCATGCAGCCACAGCTGTGGAGACAGGGCTGCTACTGGCCACGGCTTTTTGCTATGTGGCCATCTGTAAGCCCCTACACTACAAGAGAATTCTCACACCTCAAGTGATACTGGGAACGAGTGTGATCATCACCATCGGAGCTATCATATTCATGACTCCATTGAGTTGGATGGTGAGTCATCTGCCTTTCTGTGGCTCCAATGTGGTTCTCCATTCCTACTGTGAGCACATAGCTGTGGCCAAGTTGGCATATGCCCACCCCATGCCCAGGAGTCTCTACAGCTTGATTGGTTCCATTACTGTGAAAACCCACAGAACCTCCATTACTGTGGGTTCTGATGTGGCCTTTATCGCTGCCTCCTATAACTTGATTCTTCAGGCAGTATTTGGTCTCTCCGCAAAGAATGCTCAGTTGAAAGCATTAAGCACATGCGGCTCCCATGTCAGGGTTATGGCTCTGTACTACCTACCTGGGATGGCATCCATCTATGTGGCCTGGCTAGGGAAGGACACAGTGCCTTTGCACATCCAGGTGCTGGTAGCTGACTTGTACCTGATCATCCCACCAACCTCAAACCCCATCATCTATGCCCTGAGAACCAAACAAATAAGGGAGCGAACATGGAGCTTGCTGACGCACTGCCTCTTTAACCACTCCAACCTGGGTTCATGA'

gr='GCAGTCTCATCTGTGATGCTGGGGCCACCCTACAACCATACAATGGAACCCCCTGCCACCNTTGTCCTGGTGGGTATTCCAGGTTTGCAATCTTCACATCTTTGGCTGGTTACCTCACTGAACATCATGTATACCATAGCCCTGTTAGAAAACACCCTCATAGTGACTGTAATGTGGATGGATTCCACCCTACAAGAGCCCATGTACTGCTCCCTGGATATTCTGGCTGCTGTGGACACTGTCATGGCTTCCTTGGTAGCGCCCAAGATGGTGAGCATTTTCTCCTTAGGAGACAGCTTCATCAGCTTTAATGCTTGTTTCACTCAGATGTATTTTGTCCATGCAGCCACAGCTGTGGAGACAGGGCTGCTACTGGCCACGGCTTTTTGCTATGTGGCCATCTGTAAGCCCCTACACTACAAGAGAATTCTCACACCTCAAGTGATACTGGGAACGAGTGTGATCATCACCATCGGAGCTATCATATTCATGACTCCATTGAGTTGGATGGTGAGTCATCTGCCTTTCTGTGGCTCCAATGTGGTTCTCCATTCCTACTGTGAGCACATAGCTGTGGCCAAGTTGGCATATGCCCACCCCATGCCCAGTAGTCTCTACAGCTTGATTGGTTCCATTACTGTGAAAACCCACAGAACCTCCATTACTGTGGGTTCTGATGTGGCCTTTATCGCTGCCTCCTATAACTTGATTCTTCAGGCAGTATTTGGTCTCTCCGCAAAGAATGCTCAGTTGAAAGCATTAAGCACATGCGGCTCCCATGTCAGGGTTATGGCTCTGTACTACCTACCTGGGATGGCATCCATCTATGTGGCCTGGCTAGGGAAGGACACAGTGCCTTTGCACATCCAGGTGCTGGTAGCTGACTTGTACCTGATCATCCCACCAACCTCAAACCCCATCATCTATGCCCTGAGAACCAAACAAATAAGGGAGCGAACATGGAGCTTGCTGACGCACTGCCTCTTTAACCACTCCAACCTGGGTTCATGA'
long_gt= len(gt)
long_gr= len(gr)


def my_format_alignment(align1, align2, score):
	s = [score] 
	match=0
	i=0
	if len(align1)==len(align2):
		while i<len(align1):
			if align1[i]==align2[i] and align1[i]!="-" and align2[i]!="-":
				match+=1
			i+=1
		s.append(match)
	else:
		print("Erreur : les alignements passés en argument ne sont pas de la même longueur ")
	return s

def align(seq1, seq2, open_gap, extend_gap ):
	score = pairwise2.align.globalxs(seq1, seq2,open_gap,extend_gap,penalize_end_gaps=(False,False))

	return my_format_alignment(score[0][0], score[0][1], score[0][2])

score_match=align(gt, gr, -1,-1)

nb_match=score_match[1]

if long_gr<long_gt : 

	sim=nb_match/long_gr
else :
	sim=nb_match/long_gt

if sim > 0.95: 
	print("pris, similarité:", sim)
else : 
	print("Pas pris : ", sim)