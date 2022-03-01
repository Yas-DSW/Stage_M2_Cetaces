import csv
import sys

liste_lien=[]
tableau= sys.argv[1]

###Lecture du fichier CSV et récupération de la colonne d'intérêt dans une liste

with open(tableau, newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		liste_lien.append(row['GenBank FTP'])

print (liste_lien)