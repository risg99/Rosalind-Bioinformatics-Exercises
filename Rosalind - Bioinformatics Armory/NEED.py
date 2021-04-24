'''
An online interface to EMBOSS's Needle tool for aligning DNA and RNA strings can be found here.

Use:

The DNAfull scoring matrix; note that DNAfull uses IUPAC notation for ambiguous nucleotides.
Gap opening penalty of 10.
Gap extension penalty of 1.
For our purposes, the "pair" output format will work fine; this format shows the two strings aligned at the bottom of the output file beneath some statistics about the alignment.

Given: Two GenBank IDs.

Return: The maximum global alignment score between the DNA strings associated with these IDs.

Sample Dataset
JX205496.1 JX469991.1

Sample Output
257
'''

from Bio import Entrez, SeqIO, pairwise2

def getIds(s):
	ids = []
	x = s.split(' ')
	for id in x:
		ids.append(id)
	return ids

def getScore(genbank_ids):
	Entrez.email = "your_name@your_server.com"
	handle = Entrez.efetch(db="nucleotide", id=genbank_ids, rettype="fasta")
	records = list(SeqIO.parse(handle, "fasta"))
	print(pairwise2.align.globalms(records[0].seq, records[1].seq, 5, -4, -10, -1)[0][2])
	
s = 'NM_001251956.1 JX398977.1'
ids = getIds(s)
getScore(ids)

'''
OUTPUT:
223.0
'''