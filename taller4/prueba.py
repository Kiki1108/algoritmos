from LSortMethods import *
from SortMethods import *
import random
import time
import csv

cant = [(i+1)* 10000 for i in range(10)]
pruebas = 10

for n in cant:
    for _ in range(pruebas):
        vec = []
        for i in range(n):
            vec.append(random.randint(0,100000000))

        tiempos = [n]

        def gen_lista():
            lista = Lista()
            for i in vec:
                insertar(lista, i)
            return lista

        """
        lista = gen_lista()
        inicio = time.time()
        Lburbuja(lista)
        fin = time.time()
        tiempos.append(fin-inicio)
        print("Burbuja Ok")

        lista = gen_lista()
        inicio = time.time()
        LburbujaMejorada(lista)
        fin = time.time()
        tiempos.append(fin-inicio)
        print("Burbuja Mejorada Ok")

        lista = gen_lista()
        inicio = time.time()
        LburbujaBidireccional(lista)
        fin = time.time()
        tiempos.append(fin-inicio)
        print("Burbuja Bidireccional Ok")

        lista = gen_lista()
        inicio = time.time()
        Lseleccion(lista)
        fin = time.time()
        tiempos.append(fin-inicio)
        print("Selección Ok")

        lista = gen_lista()
        inicio = time.time()
        Linsercion(lista)
        fin = time.time()
        tiempos.append(fin-inicio)
        print("Inserción Ok")

        lista = gen_lista()
        inicio = time.time()
        LordenamientoRapido(lista, 0, tamanio(lista)-1)
        fin = time.time()
        tiempos.append(fin-inicio)
        print("QuickSort Ok")

        lista = gen_lista()
        inicio = time.time()
        LordenamientoMezcla(lista)
        fin = time.time()
        tiempos.append(fin-inicio)
        print("MergeSort Ok")

        lista = gen_lista()
        inicio = time.time()
        LordenaminetoArbol(lista)
        fin = time.time()
        tiempos.append(fin-inicio)
        print("Arbol Ok")
        

        lista = vec.copy()
        inicio = time.time()
        burbuja(lista)
        fin = time.time()
        tiempos.append(fin-inicio)

        lista = vec.copy()
        inicio = time.time()
        burbujaMejorada(lista)
        fin = time.time()
        tiempos.append(fin-inicio)

        lista = vec.copy()
        inicio = time.time()
        burbujaBidireccional(lista)
        fin = time.time()
        tiempos.append(fin-inicio)

        lista = vec.copy()
        inicio = time.time()
        seleccion(lista)
        fin = time.time()
        tiempos.append(fin-inicio)

        lista = vec.copy()
        inicio = time.time()
        insercion(lista)
        fin = time.time()
        tiempos.append(fin-inicio)
        """
        
        lista = vec.copy()
        inicio = time.time()
        ordenamientoRapido(lista, 0, len(lista)-1)
        fin = time.time()
        tiempos.append(fin-inicio)

        lista = vec.copy()
        inicio = time.time()
        ordenamientoMezcla(lista)
        fin = time.time()
        tiempos.append(fin-inicio)

        lista = vec.copy()
        inicio = time.time()
        ordenaminetoArbol(lista)
        fin = time.time()
        tiempos.append(fin-inicio)
        print(f"{n} Ok")

        with open('tiempos.csv', mode='a') as csv_file:
            tiempos_csv = csv.writer(csv_file)
            tiempos_csv.writerow(tiempos)
