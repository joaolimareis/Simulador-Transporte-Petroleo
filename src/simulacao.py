import networkx as nx
import matplotlib.pyplot as plt
import simpy
import random

class Simulacao:
    def __init__(self, env, grafo):
        self.env = env
        self.grafo = grafo
        self.historico_fluxo = []  # 🔹 Adicionando o atributo
        self.tempo_falhas = []

    def _criar_grafo(self):
        """Cria um grafo direcionado representando a rede de transporte de petróleo."""
        # Adicionando nós (refinarias, portos, distribuidores)
        self.grafo.add_nodes_from(["Refinaria_A", "Refinaria_B", "Porto", "Distribuidora"])

        # Adicionando arestas com custo e capacidade
        self.grafo.add_edge("Refinaria_A", "Porto", custo=5, capacidade=80)
        self.grafo.add_edge("Porto", "Distribuidora", custo=7, capacidade=60)
        self.grafo.add_edge("Refinaria_B", "Porto", custo=4, capacidade=70)
        self.grafo.add_edge("Refinaria_B", "Distribuidora", custo=10, capacidade=90)

    def encontrar_melhor_rota(self, origem, destino):
        """Encontra a melhor rota entre dois pontos usando Dijkstra."""
        melhor_rota = nx.shortest_path(self.grafo, source=origem, target=destino, weight="custo")
        return melhor_rota

    def transportar_petroleo(self, origem, destino):
        """Simula o transporte de petróleo entre dois pontos usando SimPy."""
        while True:
            tempo_transporte = random.uniform(5, 15)  
            fluxo = random.uniform(70, 100)  # Fluxo normal
            self.historico_fluxo.append((self.env.now, fluxo))
            
            print(f"[{self.env.now:.1f}h] Iniciando transporte de petróleo de {origem} para {destino}...")
            yield self.env.timeout(tempo_transporte)  
            print(f"[{self.env.now:.1f}h] Transporte concluído!")

    def introduzir_falhas(self, origem, destino):
        """Simula falhas intermitentes no transporte e reduz fluxo."""
        while True:
            tempo_falha = random.uniform(10, 30)  
            yield self.env.timeout(tempo_falha)

            print(f"⚠️ [{self.env.now:.1f}h] Falha detectada entre {origem} e {destino}! Tentando recuperação...")
            fluxo = random.uniform(20, 50)  # Fluxo reduzido
            self.historico_fluxo.append((self.env.now, fluxo))
            self.tempo_falhas.append(self.env.now)  # Marca falha no tempo
            
            tempo_recuperacao = random.uniform(5, 10)  
            yield self.env.timeout(tempo_recuperacao)

            print(f"✅ [{self.env.now:.1f}h] Transporte normalizado entre {origem} e {destino}.")
            fluxo = random.uniform(70, 100)  # Fluxo normalizado
            self.historico_fluxo.append((self.env.now, fluxo))

    def gerar_grafico_fluxo(self):
        if not self.historico_fluxo:
            print("⚠️ Nenhum dado de fluxo registrado durante a simulação.")
            return None

        tempos, fluxos = zip(*self.historico_fluxo)
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(tempos, fluxos, 'r-o', label="Fluxo de Petróleo com Falhas")
        ax.set_xlabel("Tempo (unidades de simulação)")
        ax.set_ylabel("Fluxo (barris/hora)")
        ax.set_title("Variação do Fluxo de Petróleo")
        ax.legend()
        ax.grid(True)

        return fig  # Retorna a figura

    def desenhar_grafo(self):
        """Gera uma visualização do grafo."""
        pos = nx.spring_layout(self.grafo)
        labels = {(u, v): f"Custo: {d['custo']}" for u, v, d in self.grafo.edges(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(self.grafo, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
        plt.title("Mapa das Rotas de Transporte de Petróleo")
        plt.show()
