def mensaje(mensaje):
  print(mensaje)

def suma(a,b):
  return a+b

def regresoMultiple(a,b,c):
  return a,b,c

def parametrosInfinitos(*parametros):
  for p in parametros:
    print(p)

def generador(*params):
  for p in params:
    yield p

def generadorProfundo(*params):
  for p in params:
    yield from p

mensaje("Hola Mundo")
print("La suma es:", suma(1,2))
print("regresa tupla", regresoMultiple(1,2,3))
print()

# parametros indefinidos
parametrosInfinitos("hola","mundo",12,8+8,[1,2,3])
print()

# funciones generadoras, regresan un objeto iterable (no se usa return sino yield)
# cada elemento del objeto iterable se regresa uno a uno cada que se indique con next

# funcion generadora
parametros = generador("param1","param2",[1,2,3])

param = next(parametros)
print(f"el primer regreso de la funcion generadora es: {param}")
param = next(parametros)
print(f"el segundo regreso de la funcion generadora es: {param}")

print()

# funcion generadora a un nivel mas profundo
parametros = generadorProfundo("hola","mundo")
param = next(parametros)
print(f"el primer regreso de la funcion generadora profunda es: {param}")
param = next(parametros)
print(f"el segundo regreso de la funcion generadora profunda es: {param}")
