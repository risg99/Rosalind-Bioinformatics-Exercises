'''
Problem
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
'''

from rosalind_revComp import reverseComplement

data = {
		'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
		'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
		'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
		'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
		'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
		'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
		'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
		'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
		'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
		'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
		'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
		'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
		'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
		'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
		'TAC':'Y', 'TAT':'Y', 'TAA':'STOP', 'TAG':'STOP',
		'TGC':'C', 'TGT':'C', 'TGA':'STOP', 'TGG':'W',
	}

def openReadingFrame(s,data):
	rev = reverseComplement(s)
	proteins = set()
	startIndices = []
	for i in range(len(s)-3):
		if s[i:i+3] and s[i:i+3] == 'ATG':
			startIndices.append(i)
	
	for x in startIndices:
		protein = ''
		for p in range(x,len(s)-3,3):
			if data[s[i:i+3]] and data[s[p:p+3]] == 'STOP':
				proteins.add(protein)
				break
			protein += data[s[p:p+3]]
		

	s = rev
	startIndices = []

	for i in range(len(s)-3):
		if s[i:i+3] and s[i:i+3] == 'ATG':
			startIndices.append(i)

	for x in startIndices:
		protein = ''
		for p in range(x,len(s)-3,3):
			if data[s[i:i+3]] and data[s[p:p+3]] == 'STOP':
				proteins.add(protein)
				break
			protein += data[s[p:p+3]]

	return proteins

s = 'CGAATGATACTATCACAAGGTTGGCATGCCAGTAACCATCACTAAGTGCGCTTGAAATAAGCTCTATGGCTGAGACCGGGAATTATGGCTGGGAGGTACGTGCACTTGTTCGCTAGTTCTGTCAGTACTCGAGCTACTCTTTCCTTGGATCACTGTACTCTGTAGTTCTGGTTTAAACGTGTAAAGAAGCCAACCCGAACACGCCCTAGTGCTATGCACTAGTGTACAAAACTCGTATCATGAGGCGCACAGGATTCGTGCTGCCTGGAGATCGGGTCCTGCATCGGAACCGAGGGCCCGAATGCTTGAGCTATGATCATCCCGTATGGAAAGGCGTTATCGTAGTGACTTTCTTCAAGTTTGGAAGGTTGCCTCAATTTCCTTGCGGTTGCGTGAACCCGTAGAACACCTCCGCGTATATGTGTATCATGGTTTAAGGTAAAGAATGCTAGCTAGCATTCTTTACCTTAAACCATGATACACATAGGCGTACTATAAACGCAATACCTACGTCAGGATCCTTCGGCCAAGGCTGGTCAATAACCTGGGTCTGCGATCACCAAGGGCCCTAACGGGAGCTCATAGCAACCCAAACACAGTCCGCATCAGATAGGCAGCTTCTAGATGTTTGTTAACCAGGAGTGAGCATATCTTGCGCCCAGATTGCGGCTGTGAGCAAGAATGCTCTGGCAGCTTACGGTCGCACACTCATGAGGCGGGGGACAAATTAAAGTACGTGTCCAGCCAAGGGAGCACGAGAACTAAGAACGCGGTCGCGCGCCTGTAATTCACACAAGGGGAGCAACATATCCCTGGGCCTCTTCAGCAAATGCGCCAAGGGCTATTTGATATGATAGGGCGGAGGTCATGATTGGCTCTAGTCCCAAAGCGAAGATGAGCAGTG'
lis = openReadingFrame(s,data)

for item in lis:
	print(item)

'''
OUTPUT:
MRRGTN
MIHIYAEVFYGFTQPQGN
MH
MRQGLFDMIGRRS
MLEL
MSSR
MILSQGWHASNHH
MIIAQAFGPSVPMQDPISRQHESCAPHDTSFVH
MIIPYGKALS
MERRYRSDFLQVWKVASISLRLREPVEHLRVYVYHGLR
MQDPISRQHESCAPHDTSFVH
MLLPLCELQARDRVLSSRAPLAGHVL
MRTVFGLL
MPTL
MTSALSYQIALGAFAEEAQGYVAPLV
MPVTITKCA
MAGRYVHLFASSVSTRATLSLDHCTL
MIRVLYTSA
MRRTGFVLPGDRVLHRNRGPECLSYDHPVWKGVIVVTFFKFGRLPQFPCGCVNP
MIGRRS
MLWQLTVAHS
MLTPG
MCIMV
MAETGNYGWEVRALVR
MSVRP
MFVNQE
MVTGMPTL
MV
MLASILYLKP
MIHIGVL
'''