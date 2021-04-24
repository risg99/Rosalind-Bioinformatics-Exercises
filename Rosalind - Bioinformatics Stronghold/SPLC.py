'''
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output
MVYIADKQHVASREAYGHMFKVCA
'''

dnaTable = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def getData():
	f = open('C:\\Users\\ADMIN\\Downloads\\rosalind_splc.txt')
	strs = []
	currStr = ''
	for i in f:
		if i[0] == '>':
			if currStr:
				strs.append(currStr)
			currStr = ''
		else:
			i = i.replace('\n','')
			currStr += i
	strs.append(currStr)
	return strs

def removeIntrons(dna,introns):
	introns = sorted(introns)
	introns = introns[::-1]
	for intron in introns:
		dna = dna.replace(intron,'')
	return dna

def getRNA(dnaTable,dna):
	dna = dna.replace('T','U')
	rna = ''
	for i in range(0,len(dna)-3,3):
		codon = dna[i:i+3]
		if dnaTable[codon] == 'STOP':
			break
		rna += dnaTable[codon]
	return rna

data = getData()
dna = data[0]
introns = data[1:]
newDna = removeIntrons(dna,introns)
rna = getRNA(dnaTable,newDna)
print(rna)

'''
OUTPUT:
MTRLGVCLTRTSGMIAWYLAERNSLFEPSLARLRVVSTIDIHRPHTITRIAEAIYAYPPAAMGSLSCMTFLGCHEPPPSNTFPMAVTRYWYFIAAISRVTDERQGHKPALVRIRLGRYRLECQEGAKRQGLKIEIGKNYQNPPNVIRRMEGVNRMLASRLPSTVAKPLLIGHTMPTAK
'''