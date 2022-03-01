import os
import sys

from os import listdir
from os.path import isfile, join

monRepertoire= "~/genome/" + sys.argv[1]

fichiers = [f for f in listdir(monRepertoire) if isfile(join(monRepertoire, f))]


rule read_csv : 
	input: 
		"données/données.csv"
	output: 
		"données.txt"
	shell: 
		"python3 recup_lien.py {input} > {output}"


#rule name_recuperation :
#	input :
#		expand ("~/genome/{espece}", espece = fichiers)
#
#	shell:
#		"ls ~/genome/{espece} > assemblie.txt " 


rule copy : 
	input: 
		expand("~/genome/{assembly}", assembly = fichiers)
	output:
		"~/Snakemake/" + sys.argv[1]
	shell:
		"cp {input} {output}/{assembly}"
