'''
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614

'''
import urllib.request as ur
import re

def getUniprots():
	inp = open('C:\\Users\\ADMIN\\Downloads\\rosalind_mprt.txt')
	uniprotIds = []
	for i in inp:
		if i[-1] == '\n':
			uniprotIds.append(i[:-1])
		else:
			uniprotIds.append(i)
	inp.close()
	return uniprotIds

def getVal(file):
	protein = ''
	for line in file:
		decodedLine = line.decode('utf-8')
		if '>' not in decodedLine:
			if '\n' in decodedLine[-1]:
				protein += decodedLine[:-1]
			else:
				protein += decodedLine
	return protein

def getUniprotData(uniprotIds):
	dict = {}
	for uniprotId in uniprotIds:
		webUrl = ur.urlopen('http://www.uniprot.org/uniprot/'+uniprotId+'.fasta')
		val = getVal(webUrl)
		dict[uniprotId] = val
	return dict	

def checkForNGlycosylation(dict):
	pattern = re.compile('N[^P][S|T][^P]')
	for key,value in dict.items():
		positions = []
		for m in re.finditer(pattern, str(value)):              
			positions.append(m.start() + 1)                               
		if len(positions) > 0:                                    
			print(key)                                      
			print(' '.join(map(str, positions)))                  

uniprotIds = getUniprots()
dict = getUniprotData(uniprotIds)
op = checkForNGlycosylation(dict)

'''
OUTPUT:
Q07287_ZPB_PIG
70 203 220 333 474
B3CNE0
107
A8GP89
101
Q6A9W5
8 220 394
P10761_ZP3_MOUSE
146 273 304 327 330
Q1E9Q9
185 255 347 640 1326
P00749_UROK_HUMAN
322
Q7S432
173
P01880_DTC_HUMAN
225 316 367
P31096_OSTP_BOVIN
101 209
'''