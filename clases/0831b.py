import time
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    datos_sumas = [n*10 for n in range(1000)]
    datos_potencias = [n*10 for n in range(1000)]
    datos_factorial = [n*10 for n in range(1000)]
    #datos_factorial_recursiva = [n*1 for n in range(50)]

    lista_sumas = [0 for i in range(1000)]
    lista_potencias = [0 for i in range(1000)]
    lista_factorial = [0 for i in range(1000)]
    #lista_factorial_recursiva = [0 for i in range(50)]
    

    print("Sumas")
    for j in range(10):
        for i in range(1000):
            lista_sumas[i] = lista_sumas[i] + suma_consecutiva(datos_sumas[i]) 

    lista_sumas = [n/10 for n in lista_sumas]
    print(lista_sumas)


    print("\nPotencias")
    for j in range(10):
        for i in range(1000):
            inicio = time.time()
            a = 2 ** datos_potencias[i]
            fin = time.time()
            lista_potencias[i] = lista_potencias[i] + (fin-inicio)

    lista_potencias = [n/10 for n in lista_potencias]
    print(lista_potencias)


    print("\nfactorial")
    for j in range(10):
        for i in range(1000):
            inicio = time.time()
            a = math.factorial(datos_factorial[i])
            fin = time.time()
            lista_factorial[i] = lista_factorial[i] + (fin - inicio)

    lista_factorial = [n/10 for n in lista_factorial]
    print(lista_factorial)

    
    """
    print("\nFactorial Recursivo")
    for j in range(10):
        for i in range(50):
            inicio = time.time()
            factorial_recursiva(datos_factorial_recursiva[i])
            fin = time.time()
            lista_factorial_recursiva[i] = lista_factorial_recursiva[i] + (fin-inicio)
    print(lista_factorial_recursiva)
    """

    grafico(datos_sumas, lista_sumas, "Sumas")
    grafico(datos_potencias, lista_potencias, "Potencias")
    grafico(datos_factorial, lista_factorial, "Factorial")
    #grafico(datos_factorial_recursiva, lista_factorial_recursiva, "Factorial recursiva")
    

def grafico(datos, lista, titulo):
    plt.plot(datos, lista)
    plt.grid()       
    plt.xlabel('Datos')
    plt.ylabel('tiempo')
    plt.title(titulo)
    plt.show()

def suma_consecutiva(numero):
    inicio = time.time()

    if isinstance(numero, int):
        suma = 0
        for i in range(numero):
            suma += i + 1
        return time.time()-inicio


def potencia(n1, n2):
    inicio = time.time()
    potencia = 1
    for i in range(n2):
        potencia = potencia * n1
    return time.time()-inicio


def factorial(numero):
    inicio = time.time()
    if isinstance(numero, int):
        factorial = 1
        for i in range(numero):
            factorial = factorial * (i+1)
        return time.time()-inicio


def factorial_recursiva(numero):
    if isinstance(numero, int):
        if numero != 1:
            factorial = numero * factorial_recursiva(numero-1)
            return factorial
        else:
            return 1


if __name__ == "__main__":
    main()