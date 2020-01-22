paises = {
  "Alemania": "Berlin",
  "Francia": "Paris",
  "Reino Unido": "Londres",
  "España": "Madrid",
  "Mexico": "CDMX"
}

dicMixto = {
  "Mexico": "CDMX",
  2: 100,
  ("paises",): ["Chile", "Colombia", "Peru"]
}

print("Paises: ", paises, end="\n\n")
print("longitud diccionario paises", len(paises))
print("llaves: ", paises.keys())
print("valores: ", paises.values())

print()

print("Diccionario Mixto:", end=" ")
print(dicMixto)
print()

#####################################
# Operaciones CRUD con diccionarios #
#####################################

print("OPERACIONES CRUD", end="\n\n")

# Obtener elemento de diccionario
cdmx = paises["Mexico"]
print(cdmx)
print()

# Agregar elemento a diccionario
paises["Italia"] = "Lisboa"
print(paises)
print()

# Modificar elemento a diccionario
paises["Italia"] = "Roma"
print(paises)
print()

# Eliminar elemento a diccionario
del paises["Italia"]
print(paises)
print()
