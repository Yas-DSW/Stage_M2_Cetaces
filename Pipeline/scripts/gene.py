from Bio import SeqIO
import csv
import re 

liste_espece=["Globicephala_melas", "Tursiop_truncatus"]

data=csv.reader(open('ressources/tables_CSV/genes.csv'))
out=csv.writer(open('sorties/genes_completed.csv', 'w'))

for row in data: 
	out.writerow(row)

with open('ressources/fasta.fasta',"r"):
	for record in SeqIO.parse('ressources/fasta.fasta',"fasta"):
			ID=str(record.id)
	for espece in liste_espece : 
		esp=espece.split("_")
		

with open('ressources/Ora.fa',"r"):
	for record in SeqIO.parse('ressources/Ora.fa',"fasta"):
			header=str(record.id)
			print(header)
			if re.search ('OR\d*',header):
				family=re.search("OR\d*",header).group(0)
			if re.search('PSEUDOGENE',header):
				state='Pseudogene'
			else: 
				state='Géne fonctionnel'
			ligne=["à déterminer",family, state,ID]
			family=""
			state=""
			print(ligne)
			out.writerow(ligne)
