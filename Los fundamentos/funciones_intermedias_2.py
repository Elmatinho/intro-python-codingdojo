x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1
def corte(a):
    lista_chica=x[a]
    lista_chica.pop(0)
    lista_chica.insert(0,15)
    x.pop(1)
    x.insert(1,lista_chica)
corte(1)
print(x)

#1.2
students[0]["last_name"]= "Bryat"
print(students)

#1.3
sports_directory["soccer"][0]="Andres"
print(sports_directory["soccer"][0])

#1.4
z[0]["y"]=30
print(z[0]["y"])

#2
students1 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(listaDiccionarios):
    for i in listaDiccionarios:
        print(i)
iterateDictionary(students1)

#3
def iterateDictionary(name="first_name",listaDiccionarios=""):
    for i in listaDiccionarios:
        if name== "first_name":
            print(i["first_name"])
        elif name == "last_name":
            print(i["last_name"])
        else:
            print("No existe esa llave")
            break   
iterateDictionary(name="last_name",listaDiccionarios=students1)

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def imprimiendo_dict(dict):
    for llave in dict:
        print(f"{len(dict[llave])} {llave}")
        for dato in dict[llave]:
            print(f"{dato}")
imprimiendo_dict(dojo)
