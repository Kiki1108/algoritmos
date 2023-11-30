import heapq

class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
        
    def agregar_nodo(self, valor):
        self.nodos.add(valor)
        self.aristas[valor] = {}
        
    def agregar_arista(self, desde, hacia, peso):
        self.aristas[desde][hacia] = peso
        self.aristas[hacia][desde] = peso  # Si el grafo es no dirigido

def dijkstra_unica_ruta(grafo, nodo_inicial, nodo_destino):
    distancia = {nodo: float('inf') for nodo in grafo.nodos}
    distancia[nodo_inicial] = 0

    heap = [(0, nodo_inicial)]
    padres = {nodo_inicial: None}

    while heap:
        (dist, nodo_actual) = heapq.heappop(heap)

        if nodo_actual == nodo_destino:
            # Construir la ruta si hemos llegado al nodo destino
            ruta = []
            while nodo_actual is not None:
                ruta.insert(0, nodo_actual)
                nodo_actual = padres[nodo_actual]
            return ruta

        for vecino, peso in grafo.aristas[nodo_actual].items():
            nueva_distancia = distancia[nodo_actual] + peso
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                padres[vecino] = nodo_actual
                heapq.heappush(heap, (nueva_distancia, vecino))

    # Si no se encontró una ruta al nodo destino
    return None

# Ejemplo de uso:
grafo_ejemplo = Grafo()
grafo_ejemplo.agregar_nodo('2 sur')
grafo_ejemplo.agregar_nodo('30 oriente')
grafo_ejemplo.agregar_nodo('11 oriente')
grafo_ejemplo.agregar_nodo('6 oriente')
grafo_ejemplo.agregar_nodo('16 sur')
grafo_ejemplo.agregar_nodo('2 norte')
grafo_ejemplo.agregar_nodo('26 sur')
grafo_ejemplo.agregar_nodo('26 1/2 sur')
grafo_ejemplo.agregar_nodo('6 poniente')
grafo_ejemplo.agregar_nodo('22 poniente')


grafo_ejemplo.agregar_arista('2 sur', '30 oriente', 15)
grafo_ejemplo.agregar_arista('2 sur', '16 sur', 20)
grafo_ejemplo.agregar_arista('30 oriente', '6 oriente', 6)
grafo_ejemplo.agregar_arista('30 oriente', '11 oriente', 8)
grafo_ejemplo.agregar_arista('6 oriente', '22 poniente', 10)
grafo_ejemplo.agregar_arista('11 oriente', '6 poniente', 7)
grafo_ejemplo.agregar_arista('16 sur', '2 norte', 5)
grafo_ejemplo.agregar_arista('16 sur', '26 sur', 3)
grafo_ejemplo.agregar_arista('16 sur', '6 poniente', 2)
grafo_ejemplo.agregar_arista('2 norte', '26 1/2 sur', 7)
grafo_ejemplo.agregar_arista('26 sur', '26 1/2 sur', 1)
grafo_ejemplo.agregar_arista('6 poniente', '22 poniente', 5)
grafo_ejemplo.agregar_arista('26 1/2 sur', '22 poniente', 4)



nodo_inicial_ejemplo = '2 sur'
nodo_destino_ejemplo = '22 poniente'

ruta_eficiente = dijkstra_unica_ruta(grafo_ejemplo, nodo_inicial_ejemplo, nodo_destino_ejemplo)

# Imprimir la ruta eficiente
if ruta_eficiente:
    print(f"Ruta más eficiente desde {nodo_inicial_ejemplo} hasta {nodo_destino_ejemplo}: {ruta_eficiente}")
else:
    print(f"No hay ruta desde {nodo_inicial_ejemplo} hasta {nodo_destino_ejemplo}")