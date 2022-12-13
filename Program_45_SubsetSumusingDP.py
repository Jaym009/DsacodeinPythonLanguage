def subsetSum(A, sum):
 
	n = len(A)
 
	
	T = [[False for x in range(sum + 1)] for y in range(n + 1)]
 
	
	for i in range(n + 1):
		T[i][0] = True
 
	for i in range(1, n + 1):
		
		for j in range(1, sum + 1):
			if A[i - 1] > j:
				T[i][j] = T[i - 1][j]
			else:
				T[i][j] = T[i - 1][j] or T[i - 1][j - A[i - 1]]
 
	return T[n][sum]
 
 
if __name__ == '__main__':
	A = [7, 3, 2, 5, 8]
	sum = 18
 
	if subsetSum(A, sum):
		print("Yes")
	else:
		print("No")