### PROBLEMA 1 ###

'''Calcula el valor de pi utilizando la serie de Leibniz y Gregory.
La serie es: pi = 4 * (1 - 1/3 + 1/5 - 1/7 + ...)'''

def calcular_pi(n):
    pi = 0.0
    for k in range(1,n+1):
        numerador = (-1)**(k+1)
        denominador = 2*k-1
        pi += numerador / denominador

    pi *= 4
    print("Valor aproximado de pi:", pi)


### PROBLEMA 2 ###

'''Calcular el valor aproximado e con la serie de Euler'''

def factorial(n):
    f = 1
    if n == 0 or n == 1:
        f
    else:
        f = 1
        for i in range(2, n + 1):
            f *= i
    # print("Factorial de", n, ":", f)    
    return f
    
    
def calcular_e(n):
    e = 0.0
    for k in range(n + 1):
        e += 1 / factorial(k)
    print("Valor aproximado de e:", e)


#### PROBLEMA 3 ###
'''Números amigos y suma de divisores propios'''

def divisores_propios(n):
    divisores = list()
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

def amigos(n1, n2):
    suma_n1 = sum(divisores_propios(n1))
    suma_n2 = sum(divisores_propios(n2))
    if suma_n1 == n2 and suma_n2 == n1:
        return True
    return False

#### PROBLEMA 4 ###
'''Conjetura de Collatz'''
def collatz(n):
    sequence = []
    current = n 
    sequence.append(current)
    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
        sequence.append(current)
    print(current)
    return sequence

#### PROBLEMA 5 ###
'''Conjetura de Goldbach'''

def es_primo(n):
    if n<2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

def lista_de_primos(n):
    primos = []
    for i in range(2, n + 1):
        if es_primo(i):
            primos.append(i)
    return primos

def goldbach(n):
    #se asume que n es mayor estricto que 2
    primos_posibles = lista_de_primos(n)
    print(primos_posibles)
    for p in primos_posibles:
        for q in primos_posibles:
            if p + q == n:
                return (p, q)
    return None
