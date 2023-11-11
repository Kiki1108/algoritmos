def burbuja_pura(vector):
    n = len(vector)
    cont = 0
    for i in range(n):
        for j in range(n):          
            if vector[j] > vector[i]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux
            print(cont, vector)
            cont = cont + 1


def burbuja_optimizado(vector):
    n = len(vector)
    cont = 0
    for i in range(n-1):
        for j in range(n-1-i):       
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
            print(cont, vector)
            cont = cont + 1


def burbuja_control(vector):
    cont = 0
    for i in range(len(vector)-1):
        for j in range(len(vector)-1-i):       
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
            print(cont, vector)
            cont = cont + 1


def seleccion(vector):
    n = len(vector)
    for i in range(n-1):
        min = i
        for j in range(n-i):
            k = i+j
            if vector[min] > vector[k]:
                min = k
        vector[i], vector[min] = vector[min], vector[i]
        print(vector)


def insercion(vector):
    n = len(vector)
    for i in range(n):
        for j in range(n):
            pass



if __name__ == "__main__":

    print("\nBurbuja Pura")
    vector = [11, 3, 81, 7, 45, 1]
    burbuja_pura(vector)


    print("\nBurbuja Optimizado")
    vector = [11, 3, 81, 7, 45, 1]
    burbuja_optimizado(vector)

    """
    print("\nBurbuja Control")
    vector = [11, 3, 81, 7, 45, 1]
    burbuja_control(vector)
    """

    print("\nSeleccion")
    vector = [11, 3, 81, 7, 45, 1]
    seleccion(vector)

    print("\nInersión")
    vector = [11, 3, 81, 7, 45, 1]
    insercion(vector)

