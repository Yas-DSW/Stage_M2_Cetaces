#!/usr/bin/env python3

import sys 
import csv
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

TNCBI  = sys.argv[1]
ncbi = sys.argv[2]
dnazoo = sys.argv[3]

trouver_NCBI=[]
NCBI=[]
DNAZoo=[]


#### Conversion des CSV en listes
with open(TNCBI, newline='') as csvfile:
	lecteur = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in lecteur:
 		trouver_NCBI.append(', '.join(row))


with open(ncbi, newline='') as csvfile:
	lecteur = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in lecteur:
 		NCBI.append(', '.join(row))


with open(dnazoo, newline='') as csvfile:
	lecteur = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in lecteur:
 		DNAZoo.append(', '.join(row))

print("Total touver_NCBI:", str(len(trouver_NCBI)))
print("Total NCBI :", str(len(NCBI)))
print("Total DNAZoo :", str(len(DNAZoo)))




######## Décompte de l'intersection des trois assemblage
intersection=[]


for a in trouver_NCBI : 
	for b in NCBI : 
		for c in DNAZoo :
			if (a==b) and (a==c) and (c==b) :
				intersection.append(a)
				

centre=len(intersection)
print("\n Total communs des 3 assemblages :", str(centre))


##### Décompte des gènes entre les gènes trouvés dur NCBI et ceux trouvé sur l'assemblage du NCBI grâce au pipeline :  

inter_TNCBI_NCBI=[] 
for a in trouver_NCBI : 
	for b in NCBI : 
			if (a==b) and a not in intersection :
				inter_TNCBI_NCBI.append(a)

croisement1=len(inter_TNCBI_NCBI)
print("\n Communs trouvés NCBI et assemblage NCBI:", str(croisement1))

##### Décompte des gènes entre les gènes trouvés dur NCBI et ceux trouvé sur l'assemblage du DNAZoo :


inter_TNCBI_DNAZoo=[] 

for a in trouver_NCBI :  
		for c in DNAZoo :
			if (a==c) and a not in intersection :
				inter_TNCBI_DNAZoo.append(a)

croisement2=len(inter_TNCBI_DNAZoo)
print("\n Communs trouvés NCBI et DNAZoo:", str(croisement2))



##### Décompte des gènes entre les gènes trouvés dur NCBI et ceux trouvé sur l'assemblage du DNAZoo :


inter_NCBI_DNAZoo=[] 

for b in NCBI :  
		for c in DNAZoo :
			if (b==c) and b not in intersection :
				inter_NCBI_DNAZoo.append(b)

croisement3=len(inter_NCBI_DNAZoo)
print("\n Communs NCBI et DNAZoo:", str(croisement3))

##### Décompte des gènes propre aux génes trouvé sur NCBI  :

propre_TNCBI=[]
for a in trouver_NCBI : 
	if a not in intersection and a not in inter_TNCBI_DNAZoo and a not in inter_TNCBI_NCBI :
		propre_TNCBI.append(a)

TNCBI_exclusive_number=len(propre_TNCBI)
print("\n Propres TNCBI:", str(TNCBI_exclusive_number))

##### Décompte des gènes propre à l'assemblage NCBI  :

propre_NCBI=[]
for a in NCBI : 
	if a not in intersection and a not in inter_NCBI_DNAZoo and a not in inter_TNCBI_NCBI :
		propre_NCBI.append(a)

NCBI_exclusive_number=len(propre_NCBI)
print("\n Propre NCBI:", str())

##### Décompte des gènes propre à l'assemblage DNAZoo  :

propre_DNAZoo=[]
for a in DNAZoo : 
	if a not in intersection and a not in inter_TNCBI_DNAZoo and a not in inter_NCBI_DNAZoo :
		propre_DNAZoo.append(a)

DNAZoo_exclusive_number=len(propre_DNAZoo)
print("\n Propre DNAZoo:", str(DNAZoo_exclusive_number))






# Construction du diagramme de Venn avec venn3 de matplotlib_venn

diag=venn3(subsets = (TNCBI_exclusive_number, NCBI_exclusive_number, croisement1, DNAZoo_exclusive_number, croisement2, croisement3, centre), set_labels = ('Trouvés sur NCBI', 'NCBI', 'DNAZoo'))
plt.show()
				


				
