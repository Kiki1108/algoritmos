"""
3)  Usando Grafos deben buscar una actividad cotidiana o no tanto que pueda ser representada
    a través de un Grafo. y luego preguntas que le ayuden a tomar decisiones, usando 
    búsqueda de eficiencia. Por ejemplo el costo más barato, el tiempo más corto, ruta con
    menor riesgo, etc. La idea es que ustedes propongan donde usarlo. Debe tener un mínimo 
    de 10 vértices. Sean creativos
"""
import random
from grafo import *

grafo = Grafo()

nombres = ["Alejandro Ide",
           "Amanda Perez",
           "Cristian Pavez",
           "Felipe Mendez",
           "Francisco Abdala",
           "Gabriel Rojas",
           "Matias Gajardo",
           "Ricardo Macaya",
           "Wladimir Fernandez",
           "Miguel Oyarce"]

for nombre in nombres:
        insertarVertice(grafo, nombre)

for i in range(len(nombres)):
        for j in range(i+1, len(nombres)):
                insertarArista(grafo, 
                               random.randint(0,100), 
                               buscarVertice(grafo, nombres[i]), 
                               buscarVertice(grafo, nombres[j]))

# imprimir los adyacentes de cada uno
for nom in nombres:
        print(f"\n-----{nom}-----")
        print(adyacentes(buscarVertice(grafo, nom)))

"""
Ver la mejor cadena de favores:

Quieres pedirle un favor a alguien, pero no le caes bien, por eso le pides a tu informático
de confianza que cadena de favores es la que tiene más probabilidades de que logre el
cometido teniendo el cuenta el nivel de amistad presente
"""
origen = "Alejandro Ide"
destino = "Cristian Pavez"

# Cadena con el dijkstra normal, usando el valor minimo
cadena, peso = dijkstra(grafo, origen, destino)
print("\nCadena con menor nivel de amistad")
for persona in cadena:
        print(persona)
print("Peso:", peso[destino])

# Cadena con el dijkstra buscando la ruta de menos personas con el valor máximo
cadena, peso = artskjid(grafo, origen, destino)
print("\nCadena con + nivel de amistad y - personas")
for persona in cadena:
        print(persona)
peso = (peso[destino]*(-1)+(100*(len(cadena)-1)))
print("Peso:", peso)
print("Peso promedio:", peso/(len(cadena)-1))

# Cadena directa
peso = peso_vertice_adyacente(buscarVertice(grafo, origen), buscarVertice(grafo, destino))
print("\nPeso directo:", peso)