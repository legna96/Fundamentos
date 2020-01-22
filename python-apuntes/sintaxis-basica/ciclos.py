#############
# Bucle For #
#############

def imprimeFor(elemento):
  print(f"Recorre elemento: {elemento}")
  for e in elemento:
    print(f"item={e}")
  print()

imprimeFor(range(5))
imprimeFor(range(-2,3))
# incremento de 2
imprimeFor(range(0,10,2))
# En reversa y decremento de 2
imprimeFor(range(10,0,-2))
imprimeFor("Hola")
imprimeFor([11,12,13])

###############
# Bucle While #
###############
i = 0
while i < 5:
  print(f"while: i={i}")
  i += 1

#########################
# continue, pass y else #
#########################

# continue -> ignora lo que sigue pasa a la siguiente iteracion
# pass -> pasa a la siguiente linea y sigue codificando (mas para ayuda del desarrallor)
# else -> sirve como un finaly pero solo en la condicion final del incremento del for. No aplica con break
#         ya break rompe todo el for y no llega a la condicion final del for
print()
for letra in "Python":

  if letra == "h":
    continue

  print(f"letra={letra}")
else:
  print(f"final de for. ultima letra: {letra}")
print()
