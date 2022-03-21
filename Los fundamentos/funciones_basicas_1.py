#1
def a():
    return 5
print(a())   # va a devolver el numero 5 
# devolvio 5

#2
def a():
    return 5
print(a()+a())  #Creo que va a devolver 10, pq se llama 2 veces a la función
 #Devolvió 10 

 #3
def a():
    return 5
    return 10
print(a())     #Creo que va adevolver 10, pq es el último valor que toma
 #devuelve 5, pq es donde termina la función

 #4
def a():
    return 5
    print(10)
print(a())    #Debería devolver 5, por el mismo principio de la anterior
#Devolvió 5

#5
def a():
    print(5)
x = a()
print(x)    #Debería devolver un error, no hay return
#devuelve 5 y none, esto es debido a que le digo que imprima 5 y el valor de a, pero en ningun lado ese valor se almacena

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))     #debería imprimir un valor de 8 
#devuelve un valor de 3 y 5, pq lo estamos imprimiendo por la función, pero no se suman porq son valores impresos

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))      #debería devolver una cadena de 2+5
#devolvio el valor 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())       #va a devolver 10, pq b es mayor q 10 y el tercer return no esta dentro de la función
#devuelve el 10, pero primero un 100 pq se imprime primero el b y luego se evalua

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) 
print(a(5,3))
print(a(2,3) + a(5,3))   #va a devolver 7, 14 y 21 respectivamente

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))   #va a devolver 8


#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)  #primero devolvera 500, luego 500 y despues será 300
#devuelve todo lo que dije,pero falto un 500, pq el valor de b de la función, solo funciona como 300 dentro de la función, luego retoma su valor natural

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)  #aquí va a devolver 500, luego imprimira 500,luego cuando entre a la función será 300, b tomará un nuevo valor y por último será 300
#me equivoque denuevo, es como el anterior, en el último print no se llama a la función, ese valor de 300 solo queda dentro de la función

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b) #ahora sí sera 500,500, 300 y 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()   #creo que imprimira 1,3,2 por el orden del codigo
#así fue

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)  #primero va a imprimir la función a, que imprimira 1, ejecutara la función b y va a imprimir el valor 5

#casí rey, será 1,3, 5 y 10 



















