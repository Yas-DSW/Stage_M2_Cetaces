#!/usr/bin/env python3

import sys 
import csv
import matplotlib.pyplot as plt
from matplotlib_venn import venn2


ncbi = sys.argv[1]
dnazoo = sys.argv[2]


NCBI=[]
DNAZoo=[]


#### Conversion des CSV en listes


with open(ncbi, newline='') as csvfile:
    lecteur = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in lecteur:
        NCBI.append(', '.join(row))


with open(dnazoo, newline='') as csvfile:
    lecteur = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in lecteur:
        DNAZoo.append(', '.join(row))

print("Total NCBI :", str(len(NCBI)))
print("Total DNAZoo :", str(len(DNAZoo)))




######## Décompte de l'intersection des trois assemblage
intersection=[]


for a in NCBI : 
    for b in DNAZoo :
        if (a==b)  :
            intersection.append(a)
                

centre=len(intersection)
print("\n Communs  :", str(centre))


propre_NCBI=[]
for a in NCBI : 
    if a not in intersection  :
        propre_NCBI.append(a)

NCBI_exclusive_number=len(propre_NCBI)
print("\n propre NCBI:", str())

##### Décompte des gènes propre à l'assemblage DNAZoo  :

propre_DNAZoo=[]
for b in DNAZoo : 
    if b not in intersection :
        propre_DNAZoo.append(a)

DNAZoo_exclusive_number=len(propre_DNAZoo)
print("\n propre DNAZoo:", str(DNAZoo_exclusive_number))


## construction du digramme avec venn2 de matplolib.venn
diag=venn2(subsets = ( NCBI_exclusive_number, DNAZoo_exclusive_number,centre), set_labels = ('NCBI', 'DNAZoo'))
plt.show()
                