'''
Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

Sample Dataset
A C G T
2
Sample Output
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT
'''
from itertools import product

def lexicoStr(s,n):
	p = product(s,repeat=n)
	op = []
	for i,j in enumerate(list(p)):
		perm = ''
		for item in j:
			perm += item
		op.append(perm)
	op = sorted(op)
	return op

inp = 'A B C D E F G'
arr = []
for i in inp.split(' '):
	arr.append(i)

n = 3
for i in lexicoStr(arr,n):
	print(i,end='\n')

'''
OUTPUT:
AAA
AAB
AAC
AAD
AAE
AAF
AAG
ABA
ABB
ABC
ABD
ABE
ABF
ABG
ACA
ACB
ACC
ACD
ACE
ACF
ACG
ADA
ADB
ADC
ADD
ADE
ADF
ADG
AEA
AEB
AEC
AED
AEE
AEF
AEG
AFA
AFB
AFC
AFD
AFE
AFF
AFG
AGA
AGB
AGC
AGD
AGE
AGF
AGG
BAA
BAB
BAC
BAD
BAE
BAF
BAG
BBA
BBB
BBC
BBD
BBE
BBF
BBG
BCA
BCB
BCC
BCD
BCE
BCF
BCG
BDA
BDB
BDC
BDD
BDE
BDF
BDG
BEA
BEB
BEC
BED
BEE
BEF
BEG
BFA
BFB
BFC
BFD
BFE
BFF
BFG
BGA
BGB
BGC
BGD
BGE
BGF
BGG
CAA
CAB
CAC
CAD
CAE
CAF
CAG
CBA
CBB
CBC
CBD
CBE
CBF
CBG
CCA
CCB
CCC
CCD
CCE
CCF
CCG
CDA
CDB
CDC
CDD
CDE
CDF
CDG
CEA
CEB
CEC
CED
CEE
CEF
CEG
CFA
CFB
CFC
CFD
CFE
CFF
CFG
CGA
CGB
CGC
CGD
CGE
CGF
CGG
DAA
DAB
DAC
DAD
DAE
DAF
DAG
DBA
DBB
DBC
DBD
DBE
DBF
DBG
DCA
DCB
DCC
DCD
DCE
DCF
DCG
DDA
DDB
DDC
DDD
DDE
DDF
DDG
DEA
DEB
DEC
DED
DEE
DEF
DEG
DFA
DFB
DFC
DFD
DFE
DFF
DFG
DGA
DGB
DGC
DGD
DGE
DGF
DGG
EAA
EAB
EAC
EAD
EAE
EAF
EAG
EBA
EBB
EBC
EBD
EBE
EBF
EBG
ECA
ECB
ECC
ECD
ECE
ECF
ECG
EDA
EDB
EDC
EDD
EDE
EDF
EDG
EEA
EEB
EEC
EED
EEE
EEF
EEG
EFA
EFB
EFC
EFD
EFE
EFF
EFG
EGA
EGB
EGC
EGD
EGE
EGF
EGG
FAA
FAB
FAC
FAD
FAE
FAF
FAG
FBA
FBB
FBC
FBD
FBE
FBF
FBG
FCA
FCB
FCC
FCD
FCE
FCF
FCG
FDA
FDB
FDC
FDD
FDE
FDF
FDG
FEA
FEB
FEC
FED
FEE
FEF
FEG
FFA
FFB
FFC
FFD
FFE
FFF
FFG
FGA
FGB
FGC
FGD
FGE
FGF
FGG
GAA
GAB
GAC
GAD
GAE
GAF
GAG
GBA
GBB
GBC
GBD
GBE
GBF
GBG
GCA
GCB
GCC
GCD
GCE
GCF
GCG
GDA
GDB
GDC
GDD
GDE
GDF
GDG
GEA
GEB
GEC
GED
GEE
GEF
GEG
GFA
GFB
GFC
GFD
GFE
GFF
GFG
GGA
GGB
GGC
GGD
GGE
GGF
GGG
'''