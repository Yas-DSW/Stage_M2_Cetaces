#!/usr/bin/env python3
import psycopg2


liste_ref='(1145,1181,1228,1224,1151,1213,1207,1152,1216,1170,1212,1150)'
assemblie="Tursiops truncatus mTurTru1.mat.Y"



connection = psycopg2.connect("dbname='CeGeC' user=postgres host='localhost' port='5433'")
cur=connection.cursor()
requete= 'SELECT \"Séquence\" FROM gene, link where "Référence" in '+ str(liste_ref) + ' AND link."ID gène"=gene."ID" AND "ID assemblie" = \''+assemblie+'\';'
cur.execute(requete)
resultat=cur.fetchall()

print("Séquences trouvées :", len(resultat))
with open (('sortie.fa'), 'w') as result:
	i=0
	while i<len(resultat) : 
		result.write('>Séquence'+ str(i) + assemblie + '\n' + resultat[i][0]+ '\n') 
		i+=1




