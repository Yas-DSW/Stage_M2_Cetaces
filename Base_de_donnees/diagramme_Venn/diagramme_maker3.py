#!/usr/bin/env python3

import sys 
import csv
import psycopg2
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

TNCBI  = sys.argv[1]
ncbi = sys.argv[2]
dnazoo = sys.argv[3]

# def choix_ensemble2():
# 	rep2=input("Vous intéréssez vous uniquement aux gènes fonctionnel ? (Oui/Non) ")
# 	if rep2=='oui' or rep2=='Oui' or rep2=='ouI' or rep2=='OUI'or rep2=='oUi':
# 		finreq="AND \"Etat\"=\'fonctionnel\'"
# 	elif rep2=='non' or rep2=='Non' or rep2=='noN' or rep2=='NON'or rep2=='nOn':
# 		finreq=""
# 	else:
# 		print("La réponse entrée est invalide veuillez recommencer")
# 		finreq=choix_ensemble2()
# 	return finreq



# def choix_ensemble():
# 	rep=input("Vous intéréssez vous uniquement aux pseudogènes ? (Oui/Non) ")
# 	if rep=='oui' or rep=='Oui' or rep=='ouI' or rep=='OUI'or rep=='oUi':
# 		fin_req="AND \"Etat\"=\'pseudogène\'"
# 	elif rep=='non' or rep=='Non' or rep=='noN' or rep=='NON'or rep=='nOn':
# 		fin_req=choix_ensemble2()
# 	else:
# 		print("La réponse entrée est invalide veuillez recommencer")
# 		choix_ensemble()
# 	return fin_req



# fin_req2=choix_ensemble()
fin_req= ["","AND \"Etat\"=\'pseudogène\'","AND \"Etat\"=\'fonctionnel\'"]

for fin_req2 in fin_req : 

	connection = psycopg2.connect("dbname='CeGeC' user=postgres host='localhost' port='5433'")
	cur=connection.cursor()
	requete="SELECT distinct(\"Référence\") FROM gene Where \"ID\" in (SELECT \"ID gène\" FROM link WHERE \"ID assemblie\"= \'"+TNCBI+"\' "+fin_req2+");"
	print(requete)
	cur.execute(requete)
	trouver_NCBI=cur.fetchall()

	print(len(trouver_NCBI))



	requete="SELECT distinct(\"Référence\") FROM gene Where \"ID\" in (SELECT \"ID gène\" FROM link WHERE \"ID assemblie\"= \'"+ncbi+"\' "+fin_req2+");"
	cur.execute(requete)
	NCBI=cur.fetchall()




	requete="SELECT distinct(\"Référence\") FROM gene Where \"ID\" in (SELECT \"ID gène\" FROM link WHERE \"ID assemblie\"= \'"+dnazoo+"\' "+fin_req2+");"
	cur.execute(requete)
	DNAZoo=cur.fetchall()

	requete="SELECT distinct(\"Référence\") FROM gene Where \"ID\" in (SELECT \"ID gène\" FROM link WHERE \"ID assemblie\"= \'"+TNCBI+"\' "+fin_req2+");"
	cur.execute(requete)
	tncbi=cur.fetchall()



	intersection=[]

	for a in trouver_NCBI : 
		for b in NCBI : 
			for c in DNAZoo :
				if (a==b) and (a==c) and (c==b) :
					intersection.append(a)

	inter_NCBI_DNAZoo=[] 

	for y in NCBI :  
			for c in DNAZoo :
				if (y==c) and y not in intersection :
					inter_NCBI_DNAZoo.append(y)

					
	inter_TNCBI_DNAZoo=[] 

	for x in NCBI :  
			for c in tncbi :
				if (x==c) and x not in intersection :
					inter_TNCBI_DNAZoo.append(x)


	print ("1:",len(intersection), "\n2:",len(inter_TNCBI_DNAZoo), "\n3:",len(inter_NCBI_DNAZoo))
	for d in NCBI: 
		if d not in inter_NCBI_DNAZoo and d not in intersection and d not in inter_TNCBI_DNAZoo: 
			print(d)




	## Construction du diagramme de Venn avec venn3 de matplotlib_venn

	diag=venn3([set(trouver_NCBI), set(NCBI), set(DNAZoo)], set_labels = ('Requête  NCBI', ' EXTASOR - assemblage NCBI', 'EXTASOR - assemblage DNAZoo'), set_colors=('#FB8F2A', '#AB1F00','#AB1F00'), alpha = 0.8 )
	for text in diag.set_labels:
	 text.set_fontsize(16);

	plt.title('Diagramme de Venn',fontname='Georgia',fontweight='bold',fontsize=20,
	pad=30,color='black',style='italic');
	plt.show()


				


				
