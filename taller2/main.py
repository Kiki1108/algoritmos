"""
Calculo de promedio de las notas de estudiantes pasantes donde los
estudiantes tendrán N notas en todas sus M posibles asignaturas
"""
import random
import time


def genera_asignaturas(cantidad_asignaturas, cantidad_notas):
    asignaturas = [[random.randint(10,70) for i in range(cantidad_notas)] for i in range(cantidad_asignaturas)]
    return asignaturas


def calcula_promedio(asignaturas):
    promedios = []
    final = 0
    
    inicio = time.time()
    for notas in asignaturas:
        promedio = 0
        for nota in notas:
            promedio += nota
        promedios.append((promedio)/len(asignaturas))

    for notas in promedios:
        final += notas
    final = final/len(promedios)
    fin = time.time()

    tiempo = fin - inicio

    return tiempo


if __name__ == "__main__":
    cantidad_datos = [100*n for n in range(1, 11)]
    #cantidad_datos = [1, 10, 100, 1000, 10000, 100000]
    tiempos = [0 for i in cantidad_datos]
    for j in range(10):
        for i in range(len(cantidad_datos)):
            asignaturas = genera_asignaturas(cantidad_asignaturas=cantidad_datos[i], cantidad_notas=10)
            tiempos[i] = tiempos[i] + calcula_promedio(asignaturas)

    for i in tiempos:
        print(i/10)

    


