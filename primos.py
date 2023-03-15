"""
Gabriel Lorenzo Felix

"""

""" 

Módulo de gestión de números primos 

""""


def esPrimo(numero):

    """
    Devuelve `True` si su argumento es primo, y `False` si no lo es.
    """

    for test in range(2, numero):
        if numero % test == 0: 
            return False 

    return True     


def  primos(numero):

    """
    Devuelve una **tupla** con todos los números primos menores que su argumento.
    """

    return tuple([prueba for prueba in range(2, numero) if esPrimo(prueba)])

def descompon(numero):

    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    """

    factores = []

    for factor in primos(numero):
        while numero%factor == 0:
            factores.append(factor)
            numero //= factor
    return tuple(factores)

import doctest 
doctest.testmod()