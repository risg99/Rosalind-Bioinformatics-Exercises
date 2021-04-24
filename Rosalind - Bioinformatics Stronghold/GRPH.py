'''
Problem
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph O(k) in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O(3). You may return edges in any order.

Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
'''

def getDNAid():
	# dict = {}
	ids = []
	with open("C:\\Users\\ADMIN\\Downloads\\rosalind_grph.txt") as f:
		for line in f:
			p = line.split('>')
			if len(p) == 2:
				ids.append(p[1][:-1])
	return ids

def getDNAvalue():
	x = open("C:\\Users\\ADMIN\\Downloads\\rosalind_grph.txt")
	curr = ""
	values = []
	for i in x:
		if i[0] == '>':
			if curr:
				values.append(curr)
			curr = ""
			continue
		if i[-1] == '\n':
			curr += i[:-1]
		else:
			curr += i
	values.append(curr)
	return values

def overLappingGraphs(ids,values):
	result = []
	for i in range(len(values)):
		for j in range(len(values)):
			if i != j:
				if values[i][-3:] == values[j][:3]:
						new = []
						new.append(ids[i])
						new.append(ids[j])
						result.append(new)
	return result

ids = getDNAid()
values = getDNAvalue()
result = overLappingGraphs(ids,values)
for ans in result:
	for p in ans:
		print(p,end=" ")
	print()

'''
OUTPUT:
Rosalind_9993 Rosalind_7996 
Rosalind_9993 Rosalind_6255 
Rosalind_9993 Rosalind_6259 
Rosalind_6684 Rosalind_4414 
Rosalind_6684 Rosalind_5600 
Rosalind_0802 Rosalind_1203 
Rosalind_0802 Rosalind_4400 
Rosalind_9247 Rosalind_0802 
Rosalind_2297 Rosalind_5253 
Rosalind_2297 Rosalind_6458 
Rosalind_8313 Rosalind_7215 
Rosalind_8313 Rosalind_7404 
Rosalind_5963 Rosalind_5034 
Rosalind_0407 Rosalind_5440 
Rosalind_2078 Rosalind_4865 
Rosalind_8813 Rosalind_5138 
Rosalind_8813 Rosalind_1140 
Rosalind_8813 Rosalind_7890 
Rosalind_8813 Rosalind_7829 
Rosalind_3111 Rosalind_5319 
Rosalind_3111 Rosalind_7952 
Rosalind_6431 Rosalind_6516 
Rosalind_6431 Rosalind_8431 
Rosalind_2452 Rosalind_2401 
Rosalind_2452 Rosalind_0547 
Rosalind_4078 Rosalind_2078 
Rosalind_4078 Rosalind_3111 
Rosalind_4078 Rosalind_6541 
Rosalind_7215 Rosalind_8476 
Rosalind_9907 Rosalind_5911 
Rosalind_9907 Rosalind_2711 
Rosalind_7631 Rosalind_9455 
Rosalind_5911 Rosalind_2078 
Rosalind_5911 Rosalind_3111 
Rosalind_5911 Rosalind_6541 
Rosalind_9116 Rosalind_1957 
Rosalind_6929 Rosalind_0298 
Rosalind_5319 Rosalind_8560 
Rosalind_7278 Rosalind_8476 
Rosalind_8093 Rosalind_7215 
Rosalind_8093 Rosalind_7404 
Rosalind_2401 Rosalind_9565 
Rosalind_1140 Rosalind_3321 
Rosalind_5792 Rosalind_2234 
Rosalind_5034 Rosalind_1957 
Rosalind_7890 Rosalind_6929 
Rosalind_7890 Rosalind_0298 
Rosalind_4414 Rosalind_5600 
Rosalind_8264 Rosalind_5911 
Rosalind_8264 Rosalind_2711 
Rosalind_8666 Rosalind_4414 
Rosalind_8666 Rosalind_5600 
Rosalind_8560 Rosalind_2452 
Rosalind_8560 Rosalind_2401 
Rosalind_8560 Rosalind_0547 
Rosalind_6516 Rosalind_9455 
Rosalind_1225 Rosalind_8813 
Rosalind_1225 Rosalind_4078 
Rosalind_1225 Rosalind_6013 
Rosalind_1225 Rosalind_3681 
Rosalind_1225 Rosalind_1327 
Rosalind_1225 Rosalind_5213 
Rosalind_1225 Rosalind_2859 
Rosalind_4400 Rosalind_2078 
Rosalind_4400 Rosalind_3111 
Rosalind_4400 Rosalind_6541 
Rosalind_7404 Rosalind_0802 
Rosalind_0797 Rosalind_7631 
Rosalind_0797 Rosalind_9216 
Rosalind_8664 Rosalind_2297 
Rosalind_8664 Rosalind_8313 
Rosalind_8664 Rosalind_1225 
Rosalind_8664 Rosalind_6384 
Rosalind_6748 Rosalind_5911 
Rosalind_6748 Rosalind_2711 
Rosalind_0547 Rosalind_6929 
Rosalind_0547 Rosalind_0298 
Rosalind_5246 Rosalind_6431 
Rosalind_5246 Rosalind_9116 
Rosalind_5246 Rosalind_3762 
Rosalind_3762 Rosalind_9993 
Rosalind_3762 Rosalind_2294 
Rosalind_3762 Rosalind_6643 
Rosalind_6255 Rosalind_7278 
Rosalind_6255 Rosalind_2566 
Rosalind_7829 Rosalind_2297 
Rosalind_7829 Rosalind_8313 
Rosalind_7829 Rosalind_1225 
Rosalind_7829 Rosalind_8664 
Rosalind_7829 Rosalind_6384 
Rosalind_9018 Rosalind_5440 
Rosalind_2566 Rosalind_1645 
Rosalind_2566 Rosalind_9805 
Rosalind_6541 Rosalind_7631 
Rosalind_6541 Rosalind_9216 
Rosalind_0354 Rosalind_1645 
Rosalind_0354 Rosalind_9805 
Rosalind_6259 Rosalind_7996 
Rosalind_6259 Rosalind_6255 
Rosalind_1327 Rosalind_5911 
Rosalind_1327 Rosalind_2711 
Rosalind_4539 Rosalind_9247 
Rosalind_4539 Rosalind_3366 
Rosalind_5253 Rosalind_2078 
Rosalind_5253 Rosalind_3111 
Rosalind_5253 Rosalind_6541 
Rosalind_1957 Rosalind_6431 
Rosalind_1957 Rosalind_9116 
Rosalind_1957 Rosalind_5246 
Rosalind_1957 Rosalind_3762 
Rosalind_5496 Rosalind_9247 
Rosalind_5496 Rosalind_3366 
Rosalind_6643 Rosalind_1957 
Rosalind_3321 Rosalind_2101 
Rosalind_3321 Rosalind_7304 
Rosalind_3366 Rosalind_8476 
Rosalind_8335 Rosalind_8813 
Rosalind_8335 Rosalind_4078 
Rosalind_8335 Rosalind_6013 
Rosalind_8335 Rosalind_3681 
Rosalind_8335 Rosalind_1327 
Rosalind_8335 Rosalind_5213 
Rosalind_8335 Rosalind_2859 
Rosalind_7952 Rosalind_6684 
Rosalind_9565 Rosalind_4865 
Rosalind_8541 Rosalind_5689 
Rosalind_8541 Rosalind_1708 
Rosalind_8541 Rosalind_6007 
Rosalind_6119 Rosalind_2234 
Rosalind_6511 Rosalind_8813 
Rosalind_6511 Rosalind_4078 
Rosalind_6511 Rosalind_6013 
Rosalind_6511 Rosalind_3681 
Rosalind_6511 Rosalind_1327 
Rosalind_6511 Rosalind_5213 
Rosalind_6511 Rosalind_2859 
Rosalind_9216 Rosalind_4865 
Rosalind_0006 Rosalind_6929 
Rosalind_0006 Rosalind_0298 
Rosalind_6722 Rosalind_5138 
Rosalind_6722 Rosalind_1140 
Rosalind_6722 Rosalind_7890 
Rosalind_6722 Rosalind_7829 
Rosalind_9455 Rosalind_6929 
Rosalind_9455 Rosalind_0298 
Rosalind_0298 Rosalind_6684 
Rosalind_5689 Rosalind_6516 
Rosalind_5689 Rosalind_8431 
Rosalind_5213 Rosalind_5733 
Rosalind_6911 Rosalind_0802 
Rosalind_1708 Rosalind_1203 
Rosalind_1708 Rosalind_4400 
Rosalind_6867 Rosalind_5034 
Rosalind_0122 Rosalind_8813 
Rosalind_0122 Rosalind_4078 
Rosalind_0122 Rosalind_6013 
Rosalind_0122 Rosalind_3681 
Rosalind_0122 Rosalind_1327 
Rosalind_0122 Rosalind_5213 
Rosalind_0122 Rosalind_2859 
Rosalind_0859 Rosalind_6929 
Rosalind_0859 Rosalind_0298 
Rosalind_8431 Rosalind_4865 
Rosalind_0293 Rosalind_8541 
Rosalind_0293 Rosalind_0859 
Rosalind_2859 Rosalind_5963 
Rosalind_2859 Rosalind_0407 
Rosalind_2859 Rosalind_8264 
Rosalind_2859 Rosalind_6722 
Rosalind_6458 Rosalind_8541 
Rosalind_6458 Rosalind_0859 
Rosalind_9805 Rosalind_7996 
Rosalind_9805 Rosalind_6255 
Rosalind_9805 Rosalind_6259 
Rosalind_6007 Rosalind_7631 
Rosalind_6007 Rosalind_9216 
Rosalind_4865 Rosalind_6929 
Rosalind_4865 Rosalind_0298 
[Finished in 0.1s]
'''