import time
import matplotlib.pyplot as plt
import numpy as np


def main():
    list1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
    list2 = []
    for i in list1:
        list2.append(numeros_pares_impares(i))
    print(list2)
    return list2


def numeros_pares_impares(numero):
    inicio = time.time()
    cont_imp = 0
    for i in range(1, numero+1):
        if(i % 2 == 0):
            pass
            #print(i, "Es par")
        else:
            #print(i, "Es impar")
            cont_imp += 1
    print("cantidad de Números Impares", cont_imp)
    fin = time.time()
    return (fin-inicio)

if __name__ == "__main__":
    list2 = []
    list1 = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
    for j in range(10):
        list2.append(main())
        plt.plot(list1, list2[j])
    plt.grid()       
    plt.xlabel('Datos')
    plt.ylabel('tiempo')
    plt.title('Uwu')
    plt.show()