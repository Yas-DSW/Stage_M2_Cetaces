#!/usr/bin/env python3

####### Le présent script traite les données afin d'homogénéisé les convention d'écriture 
####### entre le CSV généré par NCBI et le traitement Snakmake 
import sys
import csv


lecture = csv.reader(open(sys.argv[1]))
ligne =list(lecture)

i=0

while i < len (ligne) :
	if i<1 :
		fin=ligne[i][1:len(ligne[i])-1]
		ligne[i]= [ligne[i][0]]
		ligne[i].append("Pipeline(s) utilisé(s)")
		ligne[i]= ligne[i] + fin
		fin=ligne[i][7:len(ligne[i])-1]
		ligne[i] = ligne[i][0:7] 
		ligne[i].append("Base de donnée")
		ligne[i] = ligne[i] + fin
		ligne[i].append("Gene OR NCBI")
		ligne[i].append("Gene OR pipeline Y")
		ligne[i].append("Pseudogene OR pipeline Y")
		ligne[i].append("Gene OR pipeline M")
		ligne[i].append("Pseudogene OR pipeline M")
		i+=1
	elif i >= 1 : 
		ligne[i][0] = ligne[i][0].replace(' ','_')
		fin=ligne[i][1:len(ligne[i])-1]
		ligne[i]= [ligne[i][0]]
		ligne[i].append("")
		ligne[i]= ligne[i] + fin
		fin=ligne[i][7:len(ligne[i])-1]
		ligne[i] = ligne[i][0:7] 
		ligne[i].append("")
		ligne[i] = ligne[i] + fin
		ligne[i].append("")
		ligne[i].append("")
		ligne[i].append("")
		ligne[i].append("")
		ligne[i].append("")
		i+=1

output=csv.writer(open(sys.argv[2],'w'))
output.writerows(ligne)