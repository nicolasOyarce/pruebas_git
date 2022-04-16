dictionary = {
    'name': 'Thor',
    'age': 1,
    'color': 'Orange'
}

copydictionary = dictionary.copy() #copia el diccionario original

dictionary['color'] = 'Black' #cambia o agrega algun valor
dictionary.pop('age') #elimina valores
dictionary.popiteam() #elemina el ultimo valor 
del dictionary['name'] #elimina valores
dictionary.clear() #elimina todo el diccionario

print(dictionary)
print(dictionary['name']) #sirve para acceder a algun valor 
print(dictionary.get('age')) #otra manera de acceder a algun valor

dogs = {
    'dog1':{
        'name': 'muss',
        'age': 5,
        'color': 'brown'
    },
    'dog2':{
        'name': 'sasha',
        'age': 3,
        'color': 'brown'
    }
}

print(dogs)

#Otra forma de escribir diccionarios (dict)

animals = dict(name = 'nala', age = 1)
print(animals)

