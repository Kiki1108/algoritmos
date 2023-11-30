"""
2)  Realizar una lista simple (puede ser python) de 100.000 elementos ordenarla con HeapSort().
    Luego deben comparar los tiempos de búsqueda de datos usando los algoritmos secuencial, 
    búsqueda binaria iterativa y búsqueda binaria recursiva teniendo como referencia y comparación

        a) tiempo en buscar el elemento menor, b) tiempo en buscar el elemento del medio c) tiempos en 
        buscar el elemento mayor. d) tiempo en buscar elementos Random() deseable 3 pruebas.  

"""

import random
import time
from heap import *
from busquedas import *

def buscar(vector, buscado):
    tiempos = []

    inicio = time.time()
    secuencial(vector, buscado)
    fin = time.time()
    tiempos.append(fin-inicio)

    inicio = time.time()
    binaria(vector, buscado)
    fin = time.time()
    tiempos.append(fin-inicio)

    inicio = time.time()
    binaria_recursiva(vector, buscado, 0, len(vector)-1)
    fin = time.time()
    tiempos.append(fin-inicio)

    for tiempo in tiempos:
        print(tiempo)

tamanio = 10000000
vector = []

for _ in range(tamanio):
    num = random.randint(1, tamanio*100)
    vector.append(num)

heap = Heap(tamanio)
heap.tamanio = tamanio
heap.vector = vector

monticulizar(heap)
HeapSort(heap)
vector = heap.vector

print("Elemento menor")
buscado = vector[0]
buscar(vector, buscado)

print("Elemento medio")
buscado = vector[tamanio//2]
buscar(vector, buscado)

print("Elemento mayor")
buscado = vector[-1]
buscar(vector, buscado)

print("Elemento random")
buscado = vector[random.randint(0, tamanio)]
buscar(vector, buscado)

