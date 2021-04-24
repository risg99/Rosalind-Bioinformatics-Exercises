'''
For positive integers a and n, a modulo n (written amodn in shorthand) is the remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that a and b are congruent modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.

Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
MA

Sample Output
12
'''


data = {
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
"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
}

def inferRNAFromProtein(s,data):
	rna = []
	count = 0
	if len(s) >= 1:
		# for start codon AUG
		count = 1
	for i in range(1,len(s)):
		temp = 0
		for key, value in data.items():
			if value == s[i]:
				temp += 1
		count *= temp
	# for start codons UAG UAA and UGA
	count *= 3
	return count % 1000000

s = 'MDYWAIYHPTIFIYPSHNSGAHGDYSHHEPFCDRDAMITVVTIMRDHFNWIVLPTGGGYSVNFYNKHTLWGWACWRNNLGKEELSWNFPPDHWDAYTIQIKENTMSSIVMGVGLSMIDDCWDQTHQGDDENWLTFGIWGPTQMHQETMPFIADGLEACKDWNDQNACQQCFGELCFPMPYNDMDTPATIKAGIKYVMLQTCQCSWGTYLLHYFWHWSEQDIEYPTDVDNSHDSVHNDAMIVQWLEMYGYHLNRNVPIWTNDEILKAVIKKDYANFSDALEPSMNCWLPQQHPWIPCRSEELARYCERYVRTKAKHGGDFQPIAATISKQNIRMWDQKNSDNQVAQHHDTGDFPFMKTHIGMNFKYTMFCLWPTFLWVNCTCFWECQQFTRPRACPWYDDPCCMYMPNTEYRQMQGNRSCGPNKHPIGIEQPAPNTIHNSSSWPTMCTFFAQSPMHYYHRSPCNCHFLDPQDSAVKTYNEQNNSFYWHHDGEHCEFNPEMRHLFPCDPWEIPNMKLQYAYQYDKCEIIGEFSTLHFKEDSYEKVIKNGFFRHNRDCCGQEVLSMNNNFCEGHGYMSLQGDHLQICAFYDHWLMYMIYSIDFNWVWPLNCQYWERTEHSGKFQTGYRNEITWWAMCQFSQANFRLRCRPCLKVWTKVSDWEDLIPQTEASINRNINRVKCMLFWWTHLGCCRKPWLQVIDDADERCNCGSGLVHYMLTNTAMSDQEFCWDETYCNPKLVVFNIASGVHPSSQCQGCICGICHTRDVRCGTLLSNHGCSNMYMFANSFQSTITYHAKDQCDCMMKTPQDCVRGPAHTTGSWCTPLNGVYYYATYPNQVNLNGSAKCEHCDSPPCITFELTNGRQIFDDENAYWEKCIDSYILPNERNANGFNRTHDADNLGGTIQIGIKHQHMFCQGRDEYLVDKPWYTSPIRMNTMADYVRNRVGYDNQNAMLLLLLYSTQKGMELFYTTQRMCMCCYHHIWEEEQILSVNQHSQSTHQVYK'
c = inferRNAFromProtein(s,data)
print(c)

'''
OUTPUT:
742464
'''