#Básico
for contador in range (0,151,1):
    print(contador)
    
# Múltiplos de 5 
for i in range(5,1001,5):
    print(i)

#Contar al estilo Dojo
for i in range(1,101,1):
    if i % 10 ==0:
        print("Coding Dojo")
    elif i % 5 ==0:
        print("Coding")
    else:
        print(i)

#Whoa. Es un gran idiota
count=0
sumando=0
while count<500000:
    count=count+1
    sumando=sumando+count
else:
    resultado_impar=(sumando-250000)/2
print(resultado_impar)

#Cuenta regresiva 4 en 4
for s in range(2018,0,-4):
    print(s)


