from Bio import SeqIO
import csv

liste_espece=["Globicephala_melas", "Tursiop_truncatus"]

data=csv.reader(open('ressources/tables_CSV/assemblie.csv'))
out=csv.writer(open('sorties/assemblie_completed.csv', 'w'))

for row in data: 
	out.writerow(row)

with open('ressources/fasta.fasta',"r"):
	for espece in liste_espece : 
		esp=espece.split("_")
		for record in SeqIO.parse('ressources/fasta.fasta',"fasta"):
			ID=str(record.id)
			print (ID)
			ligne=[ID,esp[0],esp[1],"","","","","",""]

out.writerow(ligne)