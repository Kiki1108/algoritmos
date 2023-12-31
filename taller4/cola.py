class nodoCola(object):
    info, siguiente = None, None


class Cola(object):
    def __init__(self):
        self.entrada, self.salida = None, None
        self.tamanio = 0


def arribo(cola, info):
    nuevoNodo = nodoCola()
    nuevoNodo.info = info
    if cola.salida is None:
        cola.salida = nuevoNodo
    else:
        cola.entrada.siguiente = nuevoNodo
    cola.entrada = nuevoNodo
    cola.tamanio += 1


def atencion(cola):
    info = cola.salida.info
    cola.salida = cola.salida.siguiente
    if cola.salida is None:
        cola.entrada = None
    cola.tamanio -= 1
    return info


def esVacia(cola):
    return cola.entrada is None


def imprimir(cola):
    colaAuxiliar = Cola()
    while not esVacia(cola):
        info = atencion(cola)
        print(info)
        arribo(colaAuxiliar, info)

    while not esVacia(colaAuxiliar):
        info = atencion(colaAuxiliar)
        arribo(cola, info)


def index(cola, elemento):
    colaAuxiliar = Cola()
    indice = 0
    encontro = False

    while not esVacia(cola):
        actual = atencion(cola)
        arribo(colaAuxiliar, actual)
        if actual == elemento:
            encontro = True
        if not encontro:
            indice += 1
    while not esVacia(colaAuxiliar):
        actual = atencion(colaAuxiliar)
        arribo(cola, actual)

    if encontro:
        return indice
    return None


def colar(cola, elemento, pos):
    pos = pos-1
    contador = 0

    colaAuxiliar = Cola()
    while not esVacia(cola):
        info = atencion(cola)
        arribo(colaAuxiliar, info)
        if pos == contador:
            arribo(colaAuxiliar, elemento) 

    while not esVacia(colaAuxiliar):
        info = atencion(colaAuxiliar)
        arribo(cola, info)

    
