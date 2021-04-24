'''
Recall that in a DNA string s, 'A' and 'T' are complements of each other, as are 'C' and 'G'. Furthermore, the reverse complement of s is the string sc formed by reversing the symbols of s and then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

The Reverse Complement program from the SMS 2 package can be run online here.

Given: A collection of n (n≤10) DNA strings.

Return: The number of given strings that match their reverse complements.

Sample Dataset
>Rosalind_64
ATAT
>Rosalind_48
GCATA

Sample Output
1
'''

from Bio.Seq import Seq
from Bio import SeqIO

def getRevComp(file):
	count = 0
	for record in SeqIO.parse(file,'fasta'):
		if record.seq.reverse_complement() == record.seq:
			count += 1
	print(count)

file = 'C:\\Users\\ADMIN\\Downloads\\rosalind_rvco.fasta'
getRevComp(file)

'''
OUTPUT:
6
'''