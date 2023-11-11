from LSortMethods import *
import random

vec = []
for i in range(100):
    vec.append(random.randint(0,100000000))


def gen_lista():
    lista = Lista()
    for i in vec:
        insertar(lista, i)
    return lista

print(vec)
print(sorted(vec))


lista = gen_lista()
Lburbuja(lista)
if gen_vector(lista) == sorted(vec):
    print("Burbuja OK")
else:
    print("Burbuja not OK")

lista = gen_lista()
LburbujaMejorada(lista)
if gen_vector(lista) == sorted(vec):
    print("Burbuja Mejorada OK")
else:
    print("Burbuja Mejorada not OK")


lista = gen_lista()
LburbujaBidireccional(lista)
if gen_vector(lista) == sorted(vec):
    print("Burbuja Bidireccional OK")
else:
    print("Burbuja Bidireccional not OK")


lista = gen_lista()
Lseleccion(lista)
if gen_vector(lista) == sorted(vec):
    print("Selección OK")
else:
    print("Selección not OK")


lista = gen_lista()
Linsercion(lista)
if gen_vector(lista) == sorted(vec):
    print("Insercion OK")
else:
    print("Inserción not OK")


lista = gen_lista()
LordenamientoRapido(lista, 0, tamanio(lista)-1)
if gen_vector(lista) == sorted(vec):
    print("QuickSort OK")
else:
    print("QuickSort not OK")


lista = gen_lista()
lista = LordenamientoMezcla(lista)
if gen_vector(lista) == sorted(vec):
    print("Merge OK")
else:
    print("Merge not OK")

    
lista = gen_lista()
lista = LordenaminetoArbol(lista)
if gen_vector(lista) == sorted(vec):
    print("Arbol OK")
else:
    print("Arbol not OK")