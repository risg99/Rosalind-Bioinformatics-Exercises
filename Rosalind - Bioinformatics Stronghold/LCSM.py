'''
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC
'''

def getDnaMatrix():
	'''Getting the DNA Matrix'''
	x = open("C:\\Users\\ADMIN\\Downloads\\rosalind_lcsm.txt")
	curr = ""
	matrix = []
	for i in x:
		if i[0] == '>':
			if curr:
				matrix.append(curr)
			curr = ""
			continue
		if i[-1] == '\n':
			curr += i[:-1]
		else:
			curr += i
	matrix.append(curr)
	return matrix	

def findSharedMotif(dnaList):

	# Getting the index of shortest dna
	index = dnaList.index(min(dnaList,key = len))

	# Getting the shortest dna
	motif = ""
	shortestDNA = dnaList[index]

	# Traverse over the string letters in the shortestDNA
	for i in range(len(shortestDNA)):
		n = 0
		present = True
		while present:

			# Traverse through all dna to find the shortestDNA string's letters
			for dna in dnaList:
				if shortestDNA[i:i+n] not in dna or n > 1000:
					present = False
					break
			if present:
				motif = max(shortestDNA[i:i+n], motif, key = len)
			n += 1
	return motif

dna = getDnaMatrix()
print(findSharedMotif(dna))

'''
OUTPUT:
GCCTAGCTGACTGTCAACACACATTCCCTGGTCCCCCCAGGATCTAACAGGCAGAAAAGTCGCAATGACGCAAATATGCAGGCTTTACGCGAACTCGCCACATCTCATCTGTTAAAGTTTCGCGGCCAGTATAAATCGATGCGTCTTGGATTGCAATAACGCAAAAACCCCCACGGCCTGCTGGGGGCTCTTCTACCATAGGCGACACTCACAAAACGCTATACTAAACCGATGCGCCCGAGGGCGGCGTCCT
'''