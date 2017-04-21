# !/usr/bin/python

# declaracion de variables globales
maxCalled = 0
minCalled = 0


def max_val(a, b):
    """
    funcion para analizar el numero mayor entre dos valores
    :param a: el valor del primer argumento
    :param b: el valor del segundo argumento
    :return: el valor maximo de los argumentos que recibe
    """

    global maxCalled
    maxCalled = maxCalled + 1

    if (a > b):
        return a
    elif (b > a):
        return b
    else:
        return a


def min_val(a, b):
    """    
    funcion para analizar el numero menor entre dos valores
    :param a: valor del primer argumento
    :param b: valor del segundo argumento
    :return: el valor minimo de los argumentos que recibe
    """

    global minCalled
    minCalled = minCalled + 1

    if (a < b):
        return a
    elif (b < a):
        return b
    else:
        return a


def print_usage(init_msg, max_val=True, min_val=True):
    """
    funcion para mostrar un mensaje de los valores
    :param init_msg: mensaje a mostrar
    :param max_val: contador del valor maximo
    :param min_val: contador del valor minimo
    :return: sin retorno
    """
    global maxCalled, minCalled
    print (init_msg)
    if max_val:
        print ('functin max_val was called', maxCalled, ' times')
    if min_val:
        print ('function min_val was called', minCalled, ' times')

print ('Calling function max_val')
# calcular el valor maximo
max_val(1, 4)
max_val(2, b=1)
max_val(b=4, a=3)

print('Calling function min_val')
# impresion de la documentacion de la funcion min_val
print(min_val.__doc__)
# calcuar el valor minino
min_val(1, 4)
min_val(2, 4)
min_val(4, b=9)
# impresion de los contadores
print_usage('The usage of functions min_val and max_val')
