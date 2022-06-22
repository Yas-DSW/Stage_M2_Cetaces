#!/usr/bin/env python3
import psycopg2


liste_ref='(1144, 1145, 1150, 1151, 1152, 1170, 1181, 1207, 1212, 1213, 1216, 1224, 1228)'
assemblie="Tursiops truncatus mTurTru1.mat.Y"



connection = psycopg2.connect("dbname='CeGeC' user=postgres host='localhost' port='5433'")
cur=connection.cursor()
# requete= 'SELECT \"Séquence\" FROM gene, link where "Référence" in '+ str(liste_ref) + ' AND link."ID gène"=gene."ID" AND "ID assemblie" = \''+assemblie+'\';'
requete= 'SELECT \"Séquence\" FROM gene where "ID" in ( 1233, 1217, 1158, 1205, 1156, 1173, 1229, 1172, 1208, 1201, 1234, 1148, 1197, 1185, 1202, 1153, 1204, 1138, 1146, 1140, 1139, 1166, 1223, 1182, 1159, 1203, 1186, 1191, 1194, 1206, 1221);'
cur.execute(requete)
resultat=cur.fetchall()

print("Séquences trouvées :", len(resultat))


with open ((assemblie +'.fa'), 'w') as result:
	i=0
	while i<len(resultat) : 
		result.write('>Séquence'+ str(i) + assemblie + '\n' + resultat[i][0]+ '\n') 
		i+=1




