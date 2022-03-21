#1 tamaño grande
def big_size(a):
    for i in range(len(a)):
        if a[i] > 0:
            a.insert(i,"Big Size")
            a.pop(i+1)
    print(a)
big_size([1,2,3,-5])

#2 contar positivos
def contando_positivos(a):
    b=0
    for i in range(len(a)):
        if a[i]>0:
            b=b+1
    a.pop()
    a.insert(len(a),b)
    print(a)
contando_positivos([-3,2,3,8])

#3 sum_total
def sum_total(a):
    b=0
    for i in a:
        b= b + i
    print(b)
sum_total([1,2,3,-8])

#4 average
def average(a):
    b=0
    d=0
    for i in a:
        b=b+i
    d=b/(len(a))
    print(d)
average([2,8])

#5 longitud 
def length(a):
    length=len(a)
    print(length)
length([1,2,3,4,5,6,7,99])

#6 min 
def minimum(a):
    b=0
    for i in a:
        if i < b:
            b=i
    print(b)
minimum([1,2,-5,0,9,-14])

#7 max 
def maximum(a):
    b=0
    for i in a:
        if i > b:
            b=i
    print(b)
maximum([1,2,-5,0,9,-14])