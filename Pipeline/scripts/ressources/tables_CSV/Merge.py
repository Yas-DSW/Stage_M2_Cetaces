#!/usr/bin/env python3

####### Le présent script traite les données afin d'homogénéisé les convention d'écriture 
####### entre le CSV généré par NCBI et le traitement Snakmake 
import sys
import csv


assemblie = csv.reader(open("assemblie.csv"))
experience=csv.reader(open("experience.csv"))
gene=csv.reader(open("genes.csv"))
organisme=csv.reader(open("organisme.csv"))

ligne_organisme =list(organisme)
ligne_assemblie=list(assemblie)
ligne_experience=list(experience)
ligne_gene=list(gene)

merged=[[]]

i=0


while i<len(ligne_organisme[0]):
	merged[0].append(ligne_organisme[0][i])
	i+=1
i=0

while i<len(ligne_assemblie[0]):
	merged[0].append(ligne_assemblie[0][i])
	i+=1
i=0

while i<len(ligne_experience[0]):
	merged[0].append(ligne_experience[0][i])
	i+=1
i=0

while i<len(ligne_gene[0]):
	merged[0].append(ligne_gene[0][i])
	i+=1
i=0

print (merged)

output=csv.writer(open('merged.csv','w'))
output.writerows(merged)