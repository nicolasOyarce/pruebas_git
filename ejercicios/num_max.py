import os

num1_user = int(input('Ingrese el primer numero: '))
num2_user = int(input('Ingrese el segundo numero: '))

def clear_screen():
	os.system('cls')

def funcion_max(num1, num2, clear):
	num_max = 0
	if num1>num2:
		num_max = num1
	else:
		num_max = num2
	return num_max
	clear_screen()

resultado = funcion_max(num1_user, num2_user, clear_screen())
print(f'El numero mayor es: {resultado}')