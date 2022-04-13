import csv

liste_espece=["Globicephala_melas", "Tursiop_truncatus"]

data=csv.reader(open('tables_CSV/organisme.csv'))
out=csv.writer(open('organisme_completed.csv', 'w'))

for row in data: 
	out.writerow(row)

for espece in liste_espece : 
	esp=espece.split("_")
	ligne=[esp[0],esp[1],"","","","","","",""]

out.writerow(ligne)


