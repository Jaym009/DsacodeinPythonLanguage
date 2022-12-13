def merge(arr, left, right):
    i=0
    j=0
    k=0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
        
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        
            

def mergesort(arr):
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        merge(arr, left, right)
        
arr = [54,26,93,17,77,31,44,55]
mergesort(arr)
print("Sorted Array is:")
print(arr)