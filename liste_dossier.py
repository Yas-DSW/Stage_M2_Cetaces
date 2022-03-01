import os
import sys

from os import listdir
from os.path import isfile, join

monRepertoire= sys.argv[1]

fichiers = [f for f in listdir(monRepertoire) if isfile(join(monRepertoire, f))]

print (fichiers)


### tiré de https://www.journaldunet.fr/web-tech/developpement/1202869-comment-lister-tous-les-fichiers-d-un-repertoire-en-python/#:~:text=Le%20langage%20Python%20fournit%20au,un%20r%C3%A9pertoire%20pass%C3%A9%20en%20param%C3%A8tres.