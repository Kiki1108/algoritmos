"""
1)  Realizar una lista simple (puede ser python)  de 100, 1.000, 10.000, 100.000 y 1.000.000 de datos 
    (lo que aguante el PC) y ordenarla usando Heapsort. hacer pruebas de gráfico de tiempo(eje Y) y 
    datos (eje X)
"""

import random
import time
from heap import *

tamanios = [100, 1000, 10000, 100000, 1000000]
tiempos = []

for tamanio in tamanios:
    print(tamanio)
    vector = []
    for _ in range(tamanio):
        num = random.randint(1, tamanio*100)
        vector.append(num)
    
    heap = Heap(tamanio)
    heap.tamanio = tamanio
    heap.vector = vector

    inicio = time.time()
    monticulizar(heap)
    HeapSort(heap)
    fin = time.time()
    tiempos.append(fin-inicio)

print("\nTiempos")
for tiempo in tiempos:
    print(tiempo)

