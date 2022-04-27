num1_user = int(input('Ingrese un numero: '))
num2_user = int(input('Ingrese un numero: '))
num3_user = int(input('Ingrese un numero: '))

def funcion_max_exted(num1, num2, num3):
	num_max = 0
	if num1>num2 and num1>num3:
		num_max = num1
	elif num2>num1 and num1>num3:
		num_max = num2
	else:
		num_max = num3
	return num_max

resultado = funcion_max_exted(num1_user, num2_user, num3_user)
print(f'El numero mayor de los tres es el: {resultado}')
