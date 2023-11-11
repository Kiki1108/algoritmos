# Nodo simplemente enlazado
class nodoListaSimple(object):
    info, siguiente = None, None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

def insertar(lista, info):
    nodo = nodoListaSimple()
    nodo.info = info
    if lista.inicio is None:
        nodo.siguiente = lista.inicio
        lista.inicio = nodo
    else:
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while siguiente is not None:
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        nodo.siguiente = siguiente
        actual.siguiente = nodo
    lista.tamanio += 1


def gen_vector(lista):
    actual = lista.inicio
    vec = []
    while actual is not None:
        vec.append(actual.info)
        actual = actual.siguiente
    return vec


def imprimir(lista):
    actual = lista.inicio
    while actual is not None:
        print(actual.info)
        actual = actual.siguiente

def tamanio(lista):
    return lista.tamanio

def eliminar(lista, info):
    data = None
    # saber si es el primero de la lista
    if(lista.inicio.info == info):
        data = lista.incio
        lista.inicio = lista.inicio.siguiente
        lista.tamanio -= 1
    else:      
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while (siguiente is not None and info != siguiente.info):
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        # saber si es el ultimo de la lista
        if(siguiente is not None):
            data = siguiente.info
            actual.siguiente = siguiente.siguiente
            lista.tamanio -= 1
    return data


def return_index(lista, info):
    actual = lista.inicio
    contador = 0

    while actual.info != info:
        actual = actual.siguiente
        contador += 1
        if actual == None:
            return None
        
    return contador


def index(lista, index):
    actual = lista.inicio

    if actual == None:
            return None

    for i in range(index):
        if actual == None:
            return None
        actual = actual.siguiente

    return actual.info


def insert_pos(lista, index, info):
    if tamanio(lista) < index:
        print("Error, index out of the range")
        return None
    
    nodo = nodoListaSimple()
    nodo.info = info

    if index == 0:
        nodo.siguiente = lista.inicio
        lista.inicio = nodo  
    else:
        actual = lista.inicio
        siguiente = lista.inicio.siguiente

        for i in range(index-1):
            if siguiente == None:
                break
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        
        nodo.siguiente = siguiente
        actual.siguiente = nodo
    lista.tamanio += 1


def eliminar_pos(lista, index):
    if tamanio(lista) < index:
        print("Error, index out of the range")
        return None
    
    if index == 0:
        data = lista.inicio.info
        lista.inicio = lista.inicio.siguiente
        lista.tamanio -= 1
        return data
    
    actual = lista.inicio
    for i in range(index-1):
        actual = actual.siguiente

    data = actual.siguiente
    actual.siguiente = actual.siguiente.siguiente

    lista.tamanio -= 1
    return data.info

    

