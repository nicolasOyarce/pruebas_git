list = ['thor', 'gorda', 'muss', 'sasha']
list2 = list.copy() #copiar

list.append('nala') #agregar
list.clear() #limpiar
list.pop() #elimina el ultimo elem.
list.remove('sasha') #elimina elm. especificos
list.reverse() #da vuelta la lista
list.sort() #ordena la lista

print(list, list2)
print(list.count('thor')) #contar elem.
print(len(list)) #contar la longitud de la lista