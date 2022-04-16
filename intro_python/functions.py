"""
def my_function():
    print('My firts function!!')

my_function()

def print_data(argument1):
    print('My agument is: {}'.format(argument1))

print_data('parameter 1')

#ejm1
def print_data(name, lastname): 
    print('My name is {} and my lastname is {}'.format(name, lastname)) 

print_data('Nicolas', 'Oyarce') #Al momento de establecer argumentos es simepre necesario establecer la misma cant de parametros

#ejm2
def print_data(*name): #el * convierte al parametro en una tupla
    print('My name is {}'.format(name,)) 

print_data('Nicolas', 'Alexandra', 'Sandra', 'Andrea')

#ejm3
def complete_name(lastname, name):
    print(name, lastname)

complete_name(name = 'Nicolas', lastname = 'Oyarce') #se puede ocupar el nombre del argumento para ordenar los parametros

#ejm4
def complete_name2(**kwargs): #**kwargs nos permite aceder a los argumentos como diccionarios
    print(kwargs['name'], kwargs['lastname'])

complete_name2(name = 'Nicolas', lastname = 'Oyarce')

#ejm5
def my_function2(argument = 'XD'): #de esta forma al argumento se le da un valor por defecto
    print(argument)

my_function2('Batman')
my_function2()

#ejm6
def my_function_list(list):
    for el in list:
        print(el)

my_function_list(['Nicolas', 'Alexandra', 'Sandra', 'Andrea'])
"""
#ejm7: como concatenar una lista
def conatenarnames(list):
    i = ''
    for el in list:
        i = i + el + ' '
    return i

names = conatenarnames(['Nicolas', 'Oyarce'])
print(names)

#ejm8: recursividad

def recursion(i):
    if (i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)
