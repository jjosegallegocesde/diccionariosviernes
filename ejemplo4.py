numeros = []

for i in range(0,5,1):
    numero = int(input("Digite un numero: "))
    numeros.append(numero)

numeroBuscado = int(input("Digite el numero a buscar: "))

loTengo = False
for numero in numeros:
    if(numeroBuscado == numero):
        loTengo = True
        break
    else:
        loTengo = False

if(loTengo != False):
    print("Se lo tengo papá")
else:
    print("No lo tengo")
