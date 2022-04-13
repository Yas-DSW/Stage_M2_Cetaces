from Bio import SeqIO
import csv

liste_espece=["Globicephala_melas", "Tursiop_truncatus"]
liste_BD=["NCBI"]
fa="fasta.fasta"

data=csv.reader(open('tables_CSV/merged.csv'))
out=csv.writer(open('out.csv', 'w'))

####### récupération des header
for row in data: 
	out.writerow(row)

for espece in liste_espece : 
	esp=espece.split("_")
	with open(fa,"r"):
		for record in SeqIO.parse(fa,"fasta"):
			ID=str(record.id)		###Rajouter l'extraction du nom par ici
	with open(Ora.fa,"r"):
		for record in SeqIO.parse

print(esp[0]+","+ esp[1]+","+","+","+","+","+","+","+ID+","+esp[0]+"," +esp[1]+",")
# out.writerow(esp[0], esp[1],,,,,,,ID,esp[0], esp[1],liste_BD[0],,,,ID,"Pipeline de Yascim",,famille)
# Penser à chaanger l'entree de la  BD