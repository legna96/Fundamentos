import sys

# Formas de imprimir

nombre = "Angel"
apat = "Rebollo"

# por parametro
print("Nombre por parametro:", nombre, apat)
# por interpolacion
print(f"mi nombre interpolado es: {nombre} {apat}")
# por parametro end
print("Good Morning!", end = ' ')
print("What a wonderful day!")


# Las variables en python son del estilo DuckType

print(type(nombre))
nombre = 12
print(nombre)
print(type(nombre))

# Entradas

numero = int(input("Dame un numero: "))
print(numero)
cadena = str(input("Dame un cadena: "))
print(cadena)
flotante = float(input("Dame un flotante: "))
print(flotante)
