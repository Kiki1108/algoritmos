from lista import *
from arbol import insertarNodo, devolver_lista

def Lburbuja(lista):
    for i in range(tamanio(lista) - 1):
        for j in range(tamanio(lista) - i - 1):
            if index(lista, j) > index(lista, j + 1):
                aux = eliminar_pos(lista, j)
                insert_pos(lista, j+1, aux)


def LburbujaMejorada(lista):
    i = 0
    control = True
    while (i <= tamanio(lista) - 2) and control:
        control = False
        for j in range(0, tamanio(lista) - i - 1):
            if index(lista, j) > index(lista, j + 1):
                aux = eliminar_pos(lista, j)
                insert_pos(lista, j+1, aux)
                control = True
        i = i + 1


def LburbujaBidireccional(lista):
    izquierda = 0
    derecha = tamanio(lista) -1
    control = True
    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            if index(lista,i) > index(lista,i+1):
                aux = eliminar_pos(lista, i)
                insert_pos(lista, i+1, aux)
                control = True
        derecha -= 1
        for j in range(derecha, izquierda, -1):
            if index(lista,j) < index(lista,j-1):
                aux = eliminar_pos(lista, j-1)
                insert_pos(lista, j, aux)
                control = True
        izquierda += 1


def Lseleccion(lista):
    for i in range(0, tamanio(lista)-1):
        minimo = i
        for j in range(i + 1, tamanio(lista)):
            if index(lista,j) < index(lista, minimo):
                minimo = j
        if minimo != i:
            aux = eliminar_pos(lista, minimo)
            insert_pos(lista, i, aux)
            aux = eliminar_pos(lista, i+1)
            insert_pos(lista, minimo, aux)


def Linsercion(lista):
    for i in range(1, tamanio(lista) + 1):
        k = i - 1
        while (k > 0) and index(lista, k) < index(lista,k - 1):
            aux = eliminar_pos(lista, k-1)
            insert_pos(lista, k, aux)
            k -= 1


def LordenamientoRapido(lista, primero, ultimo):
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo
    while izquierda < derecha:
        while index(lista,izquierda) < index(lista,pivote) and izquierda <= derecha:
            izquierda += 1
        while index(lista,derecha) > index(lista,pivote) and derecha >= izquierda:
            derecha -= 1
        if izquierda < derecha:
            aux = eliminar_pos(lista, derecha)
            insert_pos(lista, izquierda, aux)
            aux = eliminar_pos(lista, izquierda+1)
            insert_pos(lista, derecha, aux)
    if index(lista,pivote) < index(lista,izquierda):
        aux = eliminar_pos(lista, pivote)
        insert_pos(lista, izquierda, aux)
        aux = eliminar_pos(lista, izquierda+1)
        insert_pos(lista, pivote, aux)
    if primero < izquierda:
        LordenamientoRapido(lista, primero, izquierda - 1)
    if ultimo > izquierda:
        LordenamientoRapido(lista, izquierda + 1, ultimo)


def LordenamientoMezcla(lista):
    if tamanio(lista) <= 1:
        return lista
    else:
        medio = tamanio(lista) // 2
        izquierda = Lista()
        for i in range(0, medio):
            insertar(izquierda, index(lista,i))
        derecha = Lista()
        for i in range(medio, tamanio(lista)):
            insertar(derecha, index(lista,i))
        izquierda = LordenamientoMezcla(izquierda)
        derecha = LordenamientoMezcla(derecha)
        if index(izquierda, medio - 1) <= index(derecha, 0):
            for k in range(tamanio(derecha)):
                insertar(izquierda, index(derecha, k))
            return izquierda
        resultado = Lmezcla(izquierda, derecha)
        return resultado


def Lmezcla(izquierda, derecha):
    lista_mezclada = Lista()
    while tamanio(izquierda)> 0 and (tamanio(derecha) > 0):
        if index(izquierda,0) < index(derecha,0):
            insertar(lista_mezclada, eliminar_pos(izquierda, 0))
        else:
            insertar(lista_mezclada, eliminar_pos(derecha,0))
    if tamanio(izquierda) > 0:
        for k in range(tamanio(izquierda)):
            insertar(lista_mezclada, index(izquierda, k))
    if tamanio(derecha) > 0:
        for k in range(tamanio(derecha)):
            insertar(lista_mezclada, index(derecha,k))
    return lista_mezclada


def LordenaminetoArbol(lista):
    arbol = None
    for i in range(tamanio(lista)):
        arbol = insertarNodo(arbol, index(lista, i))
    lista = Lista()
    devolver_lista(arbol, lista)
    return lista