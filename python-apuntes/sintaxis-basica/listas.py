lista = [0,1,2,3,4,5,6,7,8,9]

# acortadores de lista
print("ACORTADORES DE LISTA")
lista2 = lista[:5]
print(lista2)
lista2 = lista[1:5]
print(lista2)
lista2 = lista[0:]
print(lista2)
print()

# inserta el elemento 1.5 en la posicion 2
print("INSERT DE LISTA")
lista.insert(2,1.5)
print(lista)
print()

# inserta el elemento al final
print("APPEND DE LISTA")
lista.append("al final")
print(lista)
print()

# saca y elimina un elemento de la lista
print("REMOVE ELEMENTO 9 DE LISTA")
lista.remove(9)
print(lista[:])
print("POP DE LISTA ", lista.pop())
print(lista)
print()

# operaciones con listas
print("SUMA DE LISTAS")
print([1,2,3] + [4,5,6])
print("REPETIR LISTA * N, N = 3")
print([1,2,3] * 3)
print("EXTEND DE LISTAS")
lista.extend([10,11,12])
print(lista)
print("Longitud de la lista ", len(lista))
print()

# Busquedas en listas
print("INDICE DE ELEMENTO EN LISTA")
print("indice de 1.5: ", lista.index(1.5))
print("ELEMENTO EN LISTA?")
boleano = 1.5 in lista
print("1.5 esta en la lista?: ", boleano)
