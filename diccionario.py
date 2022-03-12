estudiante={
    'nombre':'Falcao',
    'edad':34,
    'esFutbolista':True
}
#imprimir/acceder a todas las llaves 
#atributos de mi diccionario
print(estudiante)
#necesito acceder A UN ATRIBUTO O LLAVE DEL DICCIONARIO
print(estudiante['nombre'])
print(estudiante.get('edad'))

#recorrer un diccionario
#y obtener sus valores
for valor in estudiante.values():
    print(valor)