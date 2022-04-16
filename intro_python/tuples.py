#las tuplas no tienen metodos (ejem: .append)

tuple = ('valores', 'al', 'azar', 'sin', 'sentido')

print(tuple)
print(tuple.count('al')) #cuenta los elementos
print(tuple.index('al')) #cuenta la pocision en la que se encuentra 

list_the_tuple = list(tuple) #trasforma una tupla a lista

list_the_tuple.append('hola')
print(list_the_tuple)

rango = range(7) #estipula un rango del 0 al n° que se quiera
print(rango)