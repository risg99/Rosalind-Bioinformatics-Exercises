'''
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample Dataset
6 3

Sample Output
4
'''

def mortalFib(n,m):
	living = [1,1]
	for i in range(2, n):

		# first reproduction
		temp = living[i - 1] + living[i - 2]

		# then death
		if i == m:
			temp = temp - 1
		if i > m:
			temp = temp - living[i - m - 1]
		living.append(temp)

	return living[-1]

n = 92
m = 19

op = mortalFib(n,m)
print(op)

'''
OUTPUT:
7513165195107624104
'''