import random
def randInt(min=0  , max=100   ):
    num =  random.random() * (max-min)
    if (num-int(num)) > 0.5:
        aprox=int(num)+1
    else:
        aprox=int(num)
    texto ="el numero es "+ str(num) +" y el entero es " + str(aprox)
    return texto
print(randInt()) 		# debe imprimir un número entero aleatorio entre 0 y 100
print(randInt(max=50)) 	# debe imprimir un número entero aleatorio entre 0 y 50
print(randInt(min=50)) 	# debe imprimir un número entero aleatorio entre 50 y 100
print(randInt(min=50, max=500))    # debe imprimir un número entero aleatorio entre 50 y 500