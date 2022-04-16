#Ejm
import random

number = int(input('Ingrese un numero: '))
number_rand = random.randint(1, 10)

if number == number_rand:
    print('Ore numbers are the same')
else: 
    print('Ore numbers are the different')

#Ejm
number = 3

if number < 3:
    print(f'{number} is less than 3 ')
elif number > 3:
    print(f'{number} is greater than 2')
else:
    print('Is equals')

#Short if
if 2 == 2: print('Short if')

#And y Or
if 2 < 5 and 2 < 4: print('Both are true') #Una tiene que evaluar en falso para que nose ejecute
if 2 < 5 or 2 > 4: print('One is false') #La dos tienen que evaluar en falso para que nose ejecute