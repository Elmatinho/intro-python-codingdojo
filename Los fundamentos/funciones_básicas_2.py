# 1 cuenta regresiva
def hacia_atras(a):
    lista=[]
    for i in range(a,-1,-1):
        lista.append(i)

    return lista
    
hacia_atras(8)

#2 print and return
def print_return(a,b):
    print(a)
    return b
print(print_return(1,2))
print_return(1000,90)

# 3 primero + lobgitud
def primero(a):
    x=a[0]+len(a)
    print(x)
primero([1,2,3])

# 4 esta longitud y ese valor
def crear_lista(a,b):
    lista_nueva=[]
    for i in range(a): 
        lista_nueva.append(b)
    print(lista_nueva)
crear_lista(6,7)



