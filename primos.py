"""
Gabriel Lorenzo Felix
"""

""" 
Módulo de gestión de números primos 

"""


def esPrimo(numero):

    """
    Devuelve `True` si su argumento es primo, y `False` si no lo es.

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """

    for test in range(2, numero):
        if numero % test == 0: 
            return False 

    return True     


def  primos(numero):

    """
    Devuelve una **tupla** con todos los números primos menores que su argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """

    return tuple([prueba for prueba in range(2, numero) if esPrimo(prueba)])

def descompon(numero):

    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """

    factores = []

    for factor in primos(numero):
        while numero%factor == 0:
            factores.append(factor)
            numero //= factor
    return tuple(factores)


def mcm(numero1, numero2):

    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcm(36, 30)
    180
    """

    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = []
    for i in factores1:
        if i in factores2:
            factores_comunes.append(i)
            factores2 = list(factores2)
            factores2.remove(i)
            factores2 = tuple(factores2)
    factores_totales = factores_comunes + list(factores1) + list(factores2)
    mcm = 1
    for i in set(factores_totales):
        mcm *= i ** max(factores1.count(i), factores2.count(i))
    return mcm


def mcd(numero1, numero2):

    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> mcd(924, 780)
    12
    """

    factores1 = list(descompon(numero1))
    factores2 = list(descompon(numero2))
    factores_comunes = set(factores1) & set(factores2)
    if not factores_comunes:
        return 1
    else:
        mcd = 1
        for i in factores_comunes:
            mcd *= i ** min(factores1.count(i), factores2.count(i))
        return mcd

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcmN(42, 60, 70, 63)
    1260
    """
    a = list(numeros)   
    b = []
    for x in a:
        b.append(descompon(x))
    l = len(b)
    A = list(b[0])
    i = 1
    while i < l:
        B = list(b[i])
        for x in A:                     
            if x in B:                  
                B.remove(x)             
        A = A + B  
        i += 1            
    mcm = 1                         
    for x in A:                     
        mcm = mcm * x               
    return mcm                      

def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    lista = list(numeros)
    num1 = int(lista.pop())
    a = descompon(num1)
    c = list()
    while len(lista) > 0:
        num2 = int(lista.pop())
        b = list(descompon(num2))

        for x in a:
            if x in b:
                b.remove(x)
                c.append(x)
        a = c
        c = list()

    mcdN=1
    for x in a:
        mcdN=mcdN*x

    return mcdN

import doctest 
doctest.testmod()