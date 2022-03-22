b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,101,1):
    if i/10 in range(1,11):
        print("Coding Dojo")
    elif i/5 in range(1,21):
        print("Coding")
    else:
        print(i)


sumando=0
for contar in range(1,500000,2):
    sumando=sumando+contar
    print(contar)
print(sumando)