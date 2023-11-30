from math import inf
from cola import *
from heap import *
from pila import *
import heapq


class nodoArista(object):
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.siguiente = None


class nodoVertice(object):
    def __init__(self, info):
        self.info = info
        self.siguiente = None
        self.visitado = False
        self.adyacentes = Arista()


class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


class Grafo(object):
    def __init__(self, dirigido=False):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0
        self.nodos = set()
        self.aristas = {}


def insertarVertice(grafo, info):
    nodo = nodoVertice(info)
    grafo.nodos.add(info)
    grafo.aristas[info] = {}
    if grafo.inicio is None or grafo.inicio.info > info:
        nodo.siguiente = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.siguiente
        while act is not None and act.info < nodo.info:
            ant = act
            act = act.siguiente
        nodo.siguiente = act
        ant.siguiente = nodo
    grafo.tamanio += 1


def agregarArista(origen, info, destino):
    nodo = nodoArista(info, destino)
    if origen.inicio is None or origen.inicio.destino > destino:
        nodo.siguiente = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.siguiente
        while act is not None and act.destino < nodo.destino:
            ant = act
            act = act.siguiente
        nodo.siguiente = act
        ant.siguiente = nodo
    origen.tamanio += 1


def insertarArista(grafo, info, origen, destino):
    agregarArista(origen.adyacentes, info, destino.info)
    grafo.aristas[origen.info][destino.info] = info
    grafo.aristas[destino.info][origen.info] = info
    if not grafo.dirigido:
        agregarArista(destino.adyacentes, info, origen.info)


def eliminarArista(vertice, destino):
    x = None
    if vertice.inicio.destino == destino:
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.siguiente
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.siguiente
        while act is not None and act.destino != destino:
            ant = act
            act = act.siguiente
        if act is not None:
            x = act.info
            ant.siguiente = act.siguiente
            vertice.tamanio -= 1
        return x


def eliminarVertice(grafo, info):
    x = None
    if grafo.inicio.info == info:
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.siguiente
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.siguiente
        while act is not None and act.info != info:
            ant = act
            act = act.siguiente
        if act is not None:
            x = act.info
            ant.siguiente = act.siguiente
            grafo.tamanio -= 1
    if x is not None:
        aux = grafo.inicio
        while aux is not None:
            if aux.adyacentes.inicio is not None:
                eliminarArista(aux.adyacentes, info)
            aux = aux.siguiente
    return x


def tamanio(grafo):
    return grafo.tamanio


def grafoVacio(grafo):
    return grafo.inicio is None


def buscarVertice(grafo, info):
    aux = grafo.inicio
    while aux is not None and aux.info != info:
        aux = aux.siguiente
    return aux


def buscarArista(vertice, info):
    aux = vertice.adyacentes.inicio
    while aux is not None and aux.info != info:
        aux = aux.siguiente
    return aux


def existePaso(grafo, origen, destino):
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        verticesAdyacentes = origen.adyacentes.inicio
        while verticesAdyacentes is not None and not resultado:
            adyacente = buscarVertice(grafo, verticesAdyacentes.destino)
            if adyacente.info == destino.info:
                return True
            elif not adyacente.visitado:
                resultado = existePaso(grafo, adyacente, destino)
            verticesAdyacentes = verticesAdyacentes.siguiente
    return resultado


def adyacentes(vertice):
    if vertice is None:
        return None
    aux = vertice.adyacentes.inicio
    while aux is not None:
        print(aux.destino, aux.info)
        aux = aux.siguiente


def peso_vertice_adyacente(vertice, destino):
    aux = vertice.adyacentes.inicio
    while aux is not None:
        if aux.destino == destino.info:
            return aux.info
        aux = aux.siguiente


def esAdyacente(vertice, destino):
    resultado = False
    aux = vertice.adyacentes.inicio
    while aux is not None and not resultado:
        if aux.destino == destino:
            resultado = True
        aux = aux.siguiente
    return resultado


def marcarNoVisitado(grafo):
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.siguiente


def imprimirVertices(grafo):
    aux = grafo.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.siguiente


def imprimirPorProfundidad(grafo, vertice):
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                adyacente = buscarVertice(grafo, adyacentes.destino)
                if not adyacente.visitado:
                    imprimirPorProfundidad(grafo, adyacente)
                adyacentes = adyacentes.siguiente
        vertice = vertice.siguiente


def imprimirPorAmplitud(grafo, vertice):
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            arribo(cola, vertice)
            while not esVacia(cola):
                nodo = atencion(cola)
                adyacentes = nodo.adyacentes.inicio
                while adyacentes is not None:
                    adyacente = buscarVertice(grafo, adyacentes.destino)
                    if not adyacente.visitado:
                        print(adyacente.info)
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.siguiente
        vertice = vertice.siguiente


def dijkstra(grafo, nodo_inicial, nodo_destino):
    distancia = {nodo: float('inf') for nodo in grafo.nodos}
    distancia[nodo_inicial] = 0

    heap = [(0, nodo_inicial)]
    padres = {nodo_inicial: None}

    while heap:
        (dist, nodo_actual) = heapq.heappop(heap)

        if nodo_actual == nodo_destino:
            ruta = []
            while nodo_actual is not None:
                ruta.insert(0, nodo_actual)
                nodo_actual = padres[nodo_actual]

            return ruta, distancia

        for vecino, peso in grafo.aristas[nodo_actual].items():
            nueva_distancia = distancia[nodo_actual] + peso

            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                padres[vecino] = nodo_actual
                heapq.heappush(heap, (nueva_distancia, vecino))
    return None


def artskjid(grafo, nodo_inicial, nodo_destino):
    distancia = {nodo: float('inf') for nodo in grafo.nodos}
    distancia[nodo_inicial] = 0

    heap = [(0, nodo_inicial)]
    padres = {nodo_inicial: None}

    while heap:
        (dist, nodo_actual) = heapq.heappop(heap)

        if nodo_actual == nodo_destino:
            ruta = []
            while nodo_actual is not None:
                ruta.insert(0, nodo_actual)
                nodo_actual = padres[nodo_actual]

            return ruta, distancia

        for vecino, peso in grafo.aristas[nodo_actual].items():
            nueva_distancia = distancia[nodo_actual] + (peso-100)*(-1)

            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                padres[vecino] = nodo_actual
                heapq.heappush(heap, (nueva_distancia, vecino))
    return None


    
