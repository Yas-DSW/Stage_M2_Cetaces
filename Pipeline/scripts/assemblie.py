from Bio import SeqIO
import csv

liste_espece=["Globicephala_melas", "Tursiop_truncatus"]

data=csv.reader(open('tables_CSV/assemblie.csv'))
out=csv.writer(open('assemblie_completed.csv', 'w'))

for row in data: 
	out.writerow(row)

with open('fasta.fasta',"r"):
	for record in SeqIO.parse('fasta.fasta',"fasta"):
			ID=str(record.id)
	for espece in liste_espece : 
		esp=espece.split("_")
		ligne=[ID,esp[0],esp[1],"","","","","",""]

out.writerow(ligne)