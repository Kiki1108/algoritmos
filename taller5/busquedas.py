

def secuencial(vector, buscado):
    for elemento in vector:
        if elemento == buscado:
            return elemento
    return None


def binaria(vector, buscado):
    izq = 0 
    der = len(vector) -1
    
    while izq <= der:
        pos = (der-izq)//2 + izq

        if vector[pos] == buscado:
            return vector[pos]
        elif vector[pos] > buscado:
            der = pos-1
        else:
            izq = pos+1
    return None



def binaria_recursiva(vector, buscado, izq, der):
    pos = ((der-izq) // 2) + izq

    if vector[pos] == buscado:
        return vector[pos]
    else:
        if der == izq:
            return None
        elif vector[pos] > buscado:
            return binaria_recursiva(vector, buscado, izq, pos-1)
        else:
            return binaria_recursiva(vector, buscado, pos+1, der)


