#exercise 1:
""""
data = input('Enter a data: ')
lista = ['calculator', 'race', 'green', 'telefone']

if lista.count(data) > 0:
    print(f'The data exist, {data}')
else: 
    print(f'The data does not exist, {data}')
"""
#exercise 2:
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

try:
    num1 = int(num1)
except:
    num1 = 'error'

if num1 == 'error':
    print('You entered a wrong entry')
    exit()

try:
    num2 = int(num2)
except:
    num2 = 'error'

if num2 == 'error':
    print('You entered a wrong entry')
    exit()

sign = input('Enter the sign: ')

if sign == '+':
    print('Plus: {}'.format(num1 + num2))
elif sign == '-':
    print('Subtract: {}'.format(num1 - num2))
elif sign == '/':
    print('Division: {}'.format(num1 / num2))
elif sign == '*':
    print('Multiply: {}'.format(num1 * num2))
else:
    print('The signal enter is not valid')