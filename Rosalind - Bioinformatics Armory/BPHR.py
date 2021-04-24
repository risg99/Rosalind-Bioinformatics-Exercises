'''
Quality of the bases can vary depends on position in read due to nature of the sequencing procedure. One can check this quality distribution using "Per Base Sequence Quality" module of the FastQC program.

Average accepted quality values is a 10 for the lower quartile and 25 for median. If the values falls below this limit, then the module returns a warning.

Note that for the reads >50bp long FastQC will group the bases. To show data for every base in the read use "--nogroup" option.

Given: FASTQ file, quality threshold q

Return: Number of positions where mean base quality falls below given threshold

Sample Dataset
26
@Rosalind_0029
GCCCCAGGGAACCCTCCGACCGAGGATCGT
+
>?F?@6<C<HF?<85486B;85:8488/2/
@Rosalind_0029
TGTGATGGCTCTCTGAATGGTTCAGGCAGT
+
@J@H@>B9:B;<D==:<;:,<::?463-,,
@Rosalind_0029
CACTCTTACTCCCTAGCCGAACTCCTTTTT
+
=88;99637@5,4664-65)/?4-2+)$)$
@Rosalind_0029
GATTATGATATCAGTTGGCTCCGAGAGCGT
+
<@BGE@8C9=B9:B<>>>7?B>7:02+33.

Sample Output
17
'''

from Bio import SeqIO

def baseQualityPhre(file,threshold):
	count = 0
	qualities = []
	for record in SeqIO.parse(file,'fastq'):		
		quality = record.letter_annotations['phred_quality']
		qualities.append(quality)
	print(qualities)
	
	for i in range(len(qualities[0])):
		if sum([q[i] for q in qualities])/len(qualities) < threshold:
			count += 1
	print(count)

threshold = 20
file = 'C:\\Users\\ADMIN\\Downloads\\rosalind_bphr.fastq'
baseQualityPhre(file,threshold)

'''
OUTPUT:
14
'''