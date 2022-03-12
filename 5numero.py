
from ast import For


listaNumeros = []
for k in range(0, 5, 1):
    numeroIngresado = int(input('Ingrese el numero :'))
    listaNumeros.append(numeroIngresado)

buscarNumero = int(input('¿Que número buscas?:'))
if(buscarNumero in listaNumeros):
    print('Si esta en la lista')
else:
    print('No esta en la lista')


