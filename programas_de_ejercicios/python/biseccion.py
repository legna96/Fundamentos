import math

def pedirNumeros():
    while(1):
        try:
            a = float( input("dame el numero a:\t"))
            if type(a) is type(float()):
                break
        except:
            print("no has escrito un numero, intenta de nuevo")


    while(1):
        try:
            b = float( input("dame el numero b:\t"))
            if type(b) is type(float()):
                break
        except:
            print("no has escrito un numero, intenta de nuevo")

    return a,b


def funcion( x ):

    try:
        fx = math.sin(x)/x
    except:
        fx = math.sin(x)

    return fx

def biseccion( a, b ):


    m = float( a + b ) / 2

    # Cuando sea limite del intervalo
    if round(b,12) == round(a,12):
        fm = funcion(m)
        if fm == 0:
            return m
        else:
            return -1

    # Cuando sea una raiz traida por recusividad
    if b - a <= 10**-5:
        return round(m,4)

    fm = funcion( m )
    fa = funcion( a )
    fb = funcion( b )

    if fa * fm < 0:
        return biseccion( a, m )

    elif fm * fb < 0:
        return biseccion( m, b )

    # Ya es raiz, no es menor que cero
    elif fa == 0:
        return a

    elif fb == 0:
        return b

    return -1


def main():

    print("forma del intervalo:\t[a,b]")

    a = 0
    b = 0

    while round(a,5) == round(b,5) or round(b,5) < round(a,5):
        numeros = pedirNumeros()
        a = numeros[0]
        b = numeros[1]

        if round(a,5) == round(b,5) or round(b,5) < round(a,5):
            print("debes propocionar un intervalo coherente, intentalo otra vez desde el inicio\n\n")

    inicio = a
    final = b

    while round(inicio, 1 ) <= round( final, 1 ):

        res = biseccion( inicio, inicio + .1 )

        if res != -1:

            print("resultado en [" + str(inicio) + "] = " + str(res))
            print("f(" + str(res) + ") = " + str(int(funcion(res))) + "\n\n")

        else:
            print("Sin raices en [" + str(inicio) + "]" + "\n\n")

        inicio += .1

main()
