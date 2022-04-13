import csv


data=csv.reader(open('tables_CSV/merged.csv'))
out=csv.writer(open('out.csv', 'w'))

for row in data: 
	out.writerow(row)
for colomn in data : 
	if colomn 