import sys

numero = 1

if numero < 2:
  print("entre a condicional 2 > 1")

numero = int(input("Ingresa un numero: "))

if numero < 0:
  print("El numero es negativo y su valor es: " + str(numero))
elif numero == 1:
  print("El numero es: 1")
else:
  print("El numero es: " + str(numero))

sexo = str(input("Escribe 'Hombre' ó 'Mujer': "))
edad = int(input("Escribe tu edad: "))

if sexo == 'Hombre' and edad > 18:
  print("Cumples con los requerimientos")
else:
  print("No Cumples con los requerimientos")

print("\n")
print("Lenguajes de Programacion")

opcion = str(input("Escribe un lenguaje de programacion: "))
lenguaje = opcion.lower()

if lenguaje in ("java", "python", "golang", "ruby", "c"):
  print("Tu lenguaje ", lenguaje, " si es valido")
else:
  print("Intenta con otro lenguaje")
