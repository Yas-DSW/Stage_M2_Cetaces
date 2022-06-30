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


diag=venn2([set(NCBI),set(DNAZoo)])
plt.show()


                