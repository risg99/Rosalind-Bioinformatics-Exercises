'''
A version of FastQC can be downloaded here and run locally on any operating system with a suitable Java Runtime Environment (JRE) installed.

An online version of FastQC is also available here in the "Andromeda" Galaxy instance.

Given: A quality threshold, along with FASTQ entries for multiple reads.

Return: The number of reads whose average quality is below the threshold.

Sample Dataset
28
@Rosalind_0041
GGCCGGTCTATTTACGTTCTCACCCGACGTGACGTACGGTCC
+
6.3536354;.151<211/0?::6/-2051)-*"40/.,+%)
@Rosalind_0041
TCGTATGCGTAGCACTTGGTACAGGAAGTGAACATCCAGGAT
+
AH@FGGGJ<GB<<9:GD=D@GG9=?A@DC=;:?>839/4856
@Rosalind_0041
ATTCGGTAATTGGCGTGAATCTGTTCTGACTGATAGAGACAA
+
@DJEJEA?JHJ@8?F?IA3=;8@C95=;=?;>D/:;74792.

Sample Output
1
'''
from Bio import SeqIO

def checkPhre(file,threshold):
	count = 0		
	for record in SeqIO.parse(file,'fastq'):
		phres = record.letter_annotations['phred_quality']
		phreQuality = sum(phres)/len(phres)
		if phreQuality < threshold:
			count += 1
	print(count)


file = 'C:\\Users\\Admin\\Downloads\\rosalind_phre.fastq'
checkPhre(file,23)

'''
OUTPUT:
28
'''