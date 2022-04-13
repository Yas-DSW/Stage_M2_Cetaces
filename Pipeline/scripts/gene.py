from Bio import SeqIO
import csv
import re 

liste_espece=["Globicephala_melas", "Tursiop_truncatus"]

data=csv.reader(open('../tables_CSV/genes.csv'))
out=csv.writer(open('genes_completed.csv', 'w'))

for row in data: 
	out.writerow(row)

with open('fasta.fasta',"r"):
	for record in SeqIO.parse('fasta.fasta',"fasta"):
			ID=str(record.id)
	for espece in liste_espece : 
		esp=espece.split("_")
		

with open('Ora.fa',"r"):
	for record in SeqIO.parse('Ora.fa',"fasta"):
			header=str(record.id)
			if re.search ('OR\d*',header):
				family=re.search("OR\d*",header).group(0)
			if re.search('PSEUDOGENE',header):
				state='Pseudogene'
			else: 
				state='Géne fonctionnel'

			family=""
			state=""

ligne=["à déterminer",family, state,ID]

out.writerow(ligne)