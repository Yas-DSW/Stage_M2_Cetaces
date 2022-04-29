
from Bio import pairwise2

alignements=pairwise2.align.globalxx("ACCGATCGATAGATAGATA","GATAGA")

print(len(alignements))
# print(str(float(alignements[0][2])/float()))