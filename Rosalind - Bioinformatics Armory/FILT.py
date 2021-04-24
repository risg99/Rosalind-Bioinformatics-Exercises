'''
Poor-quality reads can be filtered out using the FASTQ Quality Filter tool from the FASTX toolkit. A command-line version of FASTX can be downloaded for Linux or MacOS from its website. An online interface for the FASTQ Quality Filter is also available here within the Galaxy web platform.

Given: A quality threshold value q, percentage of bases p, and set of FASTQ entries.

Return: Number of reads in filtered FASTQ entries

Sample Dataset
20 90
@Rosalind_0049_1
GCAGAGACCAGTAGATGTGTTTGCGGACGGTCGGGCTCCATGTGACACAG
+
FD@@;C<AI?4BA:=>C<G=:AE=><A??>764A8B797@A:58:527+,
@Rosalind_0049_2
AATGGGGGGGGGAGACAAAATACGGCTAAGGCAGGGGTCCTTGATGTCAT
+
1<<65:793967<4:92568-34:.>1;2752)24')*15;1,.3*3+*!
@Rosalind_0049_3
ACCCCATACGGCGAGCGTCAGCATCTGATATCCTCTTTCAATCCTAGCTA
+
B:EI>JDB5=>DA?E6B@@CA?C;=;@@C:6D:3=@49;@87;::;;?8+

Sample Output
2
'''

from Bio import SeqIO

def getFilteredFastq(file,threshold,percentage):
	count = 0
	for record in SeqIO.parse(file,'fastq'):
		passedPhre = 0
		phres = record.letter_annotations['phred_quality']
		for phre in phres:
			if phre >= threshold:
				passedPhre += 1
		if (passedPhre/ len(phres))*100 >= percentage:
			count += 1
	print(count)

threshold = 21
percentage = 64
file = 'C:\\Users\\ADMIN\\Downloads\\rosalind_filt.fastq'
getFilteredFastq(file,threshold,percentage)

'''
OUTPUT:
62
'''