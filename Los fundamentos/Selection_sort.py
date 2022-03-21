arr=[8,3,6,2,9,0]

def minimum(arr):
    for i in range(len(arr)):
        minimo_indice=i
        print(minimo_indice)
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                minimo_indice=j
        arr[i],arr[minimo_indice]=arr[minimo_indice],arr[i]
    print(arr)
minimum(arr)