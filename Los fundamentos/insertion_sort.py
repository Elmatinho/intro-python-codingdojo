arr=[40, 11, 13, -5, 6]

def sorting(arr):
    for i in range(1, len(arr)):
        valor=arr[i]
        j=i-1
        while j>=0 and valor < arr[j]:
            arr[j+1]=arr[j]
            j =j - 1
        arr[j+1]=valor
    return arr    
print(sorting(arr))

