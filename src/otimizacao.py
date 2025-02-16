import heapq
import math

class Grafo:
    def __init__(self):
        self.nos = {}  # Conjunto de nós do grafo
        self.coordenadas = {}  # Dicionário para armazenar as coordenadas dos nós

    def adicionar_no(self, nome, x=None, y=None):
        """Adiciona um nó ao grafo e opcionalmente define suas coordenadas."""
        self.nos[nome] = []
        if x is not None and y is not None:
            self.coordenadas[nome] = (x, y)

    def adicionar_aresta(self, origem, destino, custo, distancia, capacidade):
        """Adiciona uma aresta (duto) entre dois nós."""
        self.nos[origem].append((destino, custo, distancia, capacidade))
        self.nos[destino].append((origem, custo, distancia, capacidade))

    def heuristica(self, atual, fim):
        """Calcula a distância euclidiana se as coordenadas existirem, senão retorna 0."""
        if atual in self.coordenadas and fim in self.coordenadas:
            x1, y1 = self.coordenadas[atual]
            x2, y2 = self.coordenadas[fim]
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Distância Euclidiana
        return 0  # Se não houver coordenadas, não afeta a prioridade


     
    def a_star(self, inicio, fim):
        """Algoritmo A* para encontrar a rota mais eficiente."""
        fila_prioridade = []
        heapq.heappush(fila_prioridade, (0, inicio))
        custo_total = {inicio: 0}
        caminho = {inicio: None}

        while fila_prioridade:
            _, atual = heapq.heappop(fila_prioridade)

            if atual == fim:
                return self.reconstruir_caminho(caminho, fim)

            for vizinho, custo, distancia, capacidade in self.nos[atual]:
                novo_custo = custo_total[atual] + custo

                if vizinho not in custo_total or novo_custo < custo_total[vizinho]:
                    custo_total[vizinho] = novo_custo
                    prioridade = novo_custo + self.heuristica(vizinho, fim)
                    heapq.heappush(fila_prioridade, (prioridade, vizinho))
                    caminho[vizinho] = atual

        return None

    def reconstruir_caminho(self, caminho, fim):
        """Reconstrói o caminho do ponto final ao inicial."""
        rota = []
        atual = fim
        while atual is not None:
            rota.append(atual)
            atual = caminho[atual]
        rota.reverse()
        return rota
