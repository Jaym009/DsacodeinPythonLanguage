def countingsort(arr):
    n = len(arr)
    max_ele = max(arr)
    count = [0]*(max_ele+1)
    result = [0]*n
    for i in range(n):
        count[arr[i]]+=1
    for i in range(1,max_ele+1):
        count[i] += count[i-1]
        
    i = n-1
    while i>=0:
        result[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(n):
        arr[i] = result[i]       

arr = [4,2,2,5,3,3,1]
countingsort(arr)
print("Sorted Array is:")
print(arr)
    