'''
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
'''

from rosalind_revComp import reverseComplement

def locationRestrictionSites(s):
	arr = []
	for i in range(len(s)):
		for j in range(len(s),i,-1):
			str1 = s[i:j]
			str2 = reverseComplement(str1)
			if str1 == str2 and len(str1) >= 4 and len(str2) <= 12:
				new = []
				new.append(i+1)
				new.append(len(str1))
				arr.append(new)
	return arr

s = 'TATAGCTTCAAGAATAATGAGAGCCTTTGACGTTACCATCAGATATCACACATGGCCCCGCTTTTCTCTGTCTGAGCCCCGAACATACCGAAGCTACTGCAAAGATGTCTAGAGTTCTATGGTTCTGGCATCCGTTAATACCTCGTCTAATAACATAAGTCTGACACAAATATACGCAGATAAACGGCTAAGTATAACCAAGCAATGGATGCCATTCGAACGAACGCCGTAGCGAATTGTCCCACCAACAAATTGGTTTTGCCAATTGGAAATCACGGTCACGTGCATCGCCCAAGGGACGCAAGACCGAACAATCAGATGTATATGCTGTTTTATGTGCTACGGCCTTTGCAGATCATCCAAGCAAGAACTATGCGGGGGGTTAACCCCGATTCCTTCTCGGCTTACTCGGTGAAAGATCATGTGACGGCATCTTCCGTGGCCGCCCTATTAATAGGATTACGTGTAACGGTCGGCGCTATCACTTACGAATCCCGGTCCAGGAACCTGCACCTCAGGCAGGACCCAAATACCCGAGATCCGTGAGCAGATACTGGCGAACGTTATGGCGCGTCGACCGCTGATTTCACATTTTTAGTTATTATAACTTTTTCGAATATTATCACCCCTAAAACAATCGACTGAACAAAGCTAGTTAGGTGAACTGCCCTTGAACTCCCTGCAACGCTATATCGGTTGCGGCGATGTTCATCGGACCAAATCCGTTGTCGTTGGCGCATTTTACAGTCTCACAAGTAGACTCAGCCCGCTGCGGTGGATACTGTTATGCACGTCCAGTTGTTTTCGAGAGGGAACCCTGTGACCGCGGTCAGGCTGTTATCGGCCCGCACACACCGCATACGCATGGAGCGATTGGGATATTCTCTCACAGGTCGCAACATAT'
arr = locationRestrictionSites(s)
for i in arr:
	print(*i)

'''
OUTPUT:
1 4
4 4
30 4
42 6
43 4
51 4
54 4
92 4
98 4
108 6
109 4
135 4
170 4
171 4
193 4
215 6
216 4
235 4
251 4
262 8
263 6
264 4
280 6
281 4
284 4
322 4
323 4
344 4
350 4
354 4
379 12
380 10
381 8
382 6
383 4
418 4
421 4
441 4
447 12
448 10
449 8
450 6
451 4
462 4
476 4
495 4
509 4
538 4
560 6
561 4
569 4
570 4
573 6
574 4
602 6
603 4
612 6
613 4
616 6
617 4
638 4
650 4
652 4
681 4
689 4
690 4
735 4
788 4
791 4
805 4
821 12
822 10
823 8
824 6
825 4
843 4
864 4
879 4
901 4

'''