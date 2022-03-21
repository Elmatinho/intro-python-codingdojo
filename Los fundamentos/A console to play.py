
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


