#!/usr/bin/env python3
import psycopg2


# liste_ref='(1144, 1145, 1150, 1151, 1152, 1170, 1181, 1207, 1212, 1213, 1216, 1224, 1228)'
# assemblie="Tursiops truncatus mTurTru1.mat.Y"



connection = psycopg2.connect("dbname='CeGeC' user=postgres host='localhost' port='5433'")
cur=connection.cursor()
# requete= 'SELECT \"Séquence\" FROM gene, link where "Référence" in '+ str(liste_ref) + ' AND link."ID gène"=gene."ID" AND "ID assemblie" = \''+assemblie+'\';'
requete= 'SELECT \"Séquence\" FROM gene Where \"ID\" in (SELECT \"ID gène\" FROM link WHERE \"ID assemblie\"= \'Megaptera_novaeangliae_HiC\');'
cur.execute(requete)
resultat=cur.fetchall()

print("Séquences trouvées :", len(resultat))


with open (("TNCBI_verif" +'.fa'), 'w') as result:
	i=0
	while i<len(resultat) : 
		# result.write('>Séquence'+ str(i) + assemblie + '\n' + resultat[i][0]+ '\n') 
		result.write('>Séquence'+ str(i) +'\n' + resultat[i][0]+ '\n') 
		i+=1




