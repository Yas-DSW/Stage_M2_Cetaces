from Bio import SeqIO
import csv


data=csv.reader(open('ressources/tables_CSV/experience.csv'))
out=csv.writer(open('sorties/experience_completed.csv', 'w'))

for row in data: 
	out.writerow(row)

with open('ressources/fasta.fasta',"r"):
	 for record in SeqIO.parse('ressources/fasta.fasta',"fasta"):
		ID=str(record.id)##Attention ici en raiosn de la boucle si le fichier fasta contient plusieurs génome seul le dernier sera considéré
		ligne=["",ID,'Pipeline de Yascim',""]

out.writerow(ligne)