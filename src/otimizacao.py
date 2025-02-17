import heapq
import math

class OtimizadorRotas:
    def __init__(self):
        self.nos = {}
        self.coordenadas = {}
    
    def adicionar_no(self, nome, x=None, y=None):
        self.nos[nome] = []
        if x is not None and y is not None:
            self.coordenadas[nome] = (x, y)
    
    def adicionar_aresta(self, origem, destino, custo, distancia, capacidade):
        self.nos[origem].append((destino, custo, distancia, capacidade))
        self.nos[destino].append((origem, custo, distancia, capacidade))
    
    def heuristica(self, atual, fim, peso_distancia=1, peso_capacidade=0.5):
        if atual in self.coordenadas and fim in self.coordenadas:
            x1, y1 = self.coordenadas[atual]
            x2, y2 = self.coordenadas[fim]
            distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            return peso_distancia * distancia 
        return 0
    
    def a_star(self, inicio, fim, criterio='custo'):
        fila_prioridade = []
        heapq.heappush(fila_prioridade, (0, inicio))
        custo_total = {inicio: 0}
        caminho = {inicio: None}
        
        while fila_prioridade:
            _, atual = heapq.heappop(fila_prioridade)
            if atual == fim:
                return self.reconstruir_caminho(caminho, fim)
            
            for vizinho, custo, distancia, capacidade in self.nos[atual]:
                if criterio == 'custo':
                    novo_custo = custo_total[atual] + custo
                elif criterio == 'distancia':
                    novo_custo = custo_total[atual] + distancia
                elif criterio == 'capacidade':
                    novo_custo = custo_total[atual] - capacidade 
                
                if vizinho not in custo_total or novo_custo < custo_total[vizinho]:
                    custo_total[vizinho] = novo_custo
                    prioridade = novo_custo + self.heuristica(vizinho, fim)
                    heapq.heappush(fila_prioridade, (prioridade, vizinho))
                    caminho[vizinho] = atual
        
        return None
    
    def reconstruir_caminho(self, caminho, fim):
        rota = []
        atual = fim
        while atual is not None:
            rota.append(atual)
            atual = caminho[atual]
        rota.reverse()
        return rota
