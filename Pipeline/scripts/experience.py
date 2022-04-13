from Bio import SeqIO
import csv

liste_espece=["Globicephala_melas", "Tursiop_truncatus"]

data=csv.reader(open('tables_CSV/experience.csv'))
out=csv.writer(open('experience_completed.csv', 'w'))

for row in data: 
	out.writerow(row)

with open('fasta.fasta',"r"):
	for record in SeqIO.parse('fasta.fasta',"fasta"):
			ID=str(record.id)
	for espece in liste_espece : 
		esp=espece.split("_")
		ligne=["",ID,'Pipeline de Yascim',""]

out.writerow(ligne)