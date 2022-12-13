def subsetSum(A, n, sum):
 
	if sum == 0:
		return True
 
	if n < 0 or sum < 0:
		return False
 
	include = subsetSum(A, n - 1, sum - A[n])
 
	exclude = subsetSum(A, n - 1, sum)
 
	return include or exclude
 
 

if __name__ == '__main__':
 
	
	A = [7, 3, 2, 5, 8]
	sum = 14
 
	print("Yes" if subsetSum(A, len(A) - 1, sum) else "No")