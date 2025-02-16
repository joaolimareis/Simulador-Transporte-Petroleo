import random
import numpy as np
import simpy
import matplotlib.pyplot as plt

class Simulacao:
    def __init__(self, env, grafo):
        self.env = env
        self.grafo = grafo
        self.historico_fluxo = []
        self.tempo_falhas = []

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
        """Gera um gráfico mostrando o impacto das falhas no fluxo de petróleo."""
        tempos, fluxos = zip(*self.historico_fluxo)  

        plt.figure(figsize=(8, 5))
        plt.plot(tempos, fluxos, 'r-', label="Fluxo com falhas")

        # Adiciona marcação das falhas
        for t in self.tempo_falhas:
            plt.axvline(x=t, color='black', linestyle='--', alpha=0.7, label="Falha")

        plt.xlabel("Tempo (horas)")
        plt.ylabel("Fluxo de petróleo (m³/h)")
        plt.title("Impacto das Falhas no Fluxo de Petróleo")
        plt.legend()
        plt.grid()
        plt.show()
