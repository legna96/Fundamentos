##
# Las tuplas son listas inmutables
# no permiten agregar ni eliminar elementos
# solo se puede extraer informacion de tuplas
# son mas rapidas que las listas y se pueden usar como clave de diccionario
##

tupla = ("hola", "mundo", 1, 2)
tuplaUnitaria = ("unitaria",)
tuplaEmpaquetada = "hola", "mundo", 1, 2

print(tupla)
print(tuplaUnitaria)
print(tuplaEmpaquetada)
print(tupla[1])

# operaciones
print("operaciones con tuplas")
print("hola" in tupla)
print(tupla.count("mundo"))
print(len(tupla))
print()

#converciones de tupla a lista y diceversa
print("convertir tupla en lista")
lista = list(tupla)
print(lista)
print()

print("convertir lista en tupla")
tupla = tuple(lista)
print(tupla)
print()

# Desempaquetado de tupla
print("desempaquetado de tupla")
hola, mundo, uno, dos = tuplaEmpaquetada
print(hola)
print(mundo)
print(uno)
print(dos)
print()
