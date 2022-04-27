valor_user = input('Ingrese alguna palabra: ')
	
def longitud(valor):
	cont = 0
	for i in valor:
		cont += 1
	return cont

print_respuesta = longitud(valor_user)
print(f'La longitud de su palabra es de {print_respuesta} letras')