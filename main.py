import logging
import simpy
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from src.models.pipeline import Pipeline
from src.models.refinery import Refinery
from src.visualizacao import plot_fluxo_tempo
from src.simulacao import Simulacao
from matplotlib.backends.backend_pdf import PdfPages

logger = logging.getLogger(__name__)

def simular_fluxo(usar_simpy=True):
    """Função para rodar a simulação do fluxo de petróleo e otimização de rotas."""
    
    # 🔹 Parâmetros do duto
    parametros_duto = {
        "diametro": 0.2032,
        "comprimento": 27000,
        "rugosidade": 0.0001,
        "viscosidade": 0.05,
        "pressao_inicial": 3500000,
        "pressao_final": 2500000,
        "perda_carga": 0.02,
        "capacidade_maxima": 83.3  
    }
    
    pipeline = Pipeline(**parametros_duto)
    tempo = np.linspace(0, 24, 50)
    fluxo = np.sin(tempo / 4) * 10 + parametros_duto["capacidade_maxima"]
    vazao_duto = pipeline.calcular_fluxo(parametros_duto["capacidade_maxima"])
    
    logger.info(f"Vazão do Duto: {vazao_duto:.2f} m³/h")

    # 🔹 Criando gráfico do fluxo de petróleo
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(tempo, fluxo, 'bo-', label="Fluxo de Petróleo")
    ax1.set_xlabel("Tempo (horas)")
    ax1.set_ylabel("Fluxo (barris/hora)")
    ax1.set_title("Variação do Fluxo de Petróleo no Duto")
    ax1.legend()
    ax1.grid(True)
    
    refinaria = Refinery(capacidade_processamento=200000, eficiencia=0.9)
    produtos_refinados = refinaria.processar_petroleo(vazao_duto)
    
    logger.info(f"Produtos refinados: {produtos_refinados}")

    # 🔹 Criando gráfico dos produtos refinados
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    produtos = list(produtos_refinados.keys())
    quantidades = list(produtos_refinados.values())
    ax2.bar(produtos, quantidades, color=['red', 'blue', 'green'])
    ax2.set_xlabel("Produtos Refinados")
    ax2.set_ylabel("Quantidade (m³)")
    ax2.set_title("Distribuição de Produtos Refinados")
    ax2.grid(axis="y")

    # 🔹 Criando a estrutura do Grafo com NetworkX
    grafo = nx.DiGraph()
    grafo.add_edge("Refinaria_A", "Porto", custo=5, capacidade=80)
    grafo.add_edge("Porto", "Distribuidora", custo=7, capacidade=60)
    grafo.add_edge("Refinaria_B", "Porto", custo=4, capacidade=70)
    grafo.add_edge("Refinaria_B", "Distribuidora", custo=10, capacidade=90)

    melhor_rota = nx.shortest_path(grafo, source="Refinaria_A", target="Distribuidora", weight="custo")
    logger.info(f"📍 Melhor Rota para transporte de petróleo: {melhor_rota}")
    
    if usar_simpy:
        env = simpy.Environment()
        simulacao = Simulacao(env, grafo)
        
        env.process(simulacao.transportar_petroleo("Refinaria_A", "Distribuidora"))
        env.process(simulacao.introduzir_falhas("Refinaria_A", "Porto"))

        env.run(until=50)  # Tempo da simulação

        simulacao.gerar_grafico_fluxo()  # Mostra o gráfico com falhas após a simulação

    # 🔹 Salvando os gráficos em PDF
    with PdfPages("graficos_fluxo_petroleo.pdf") as pdf:
        pdf.savefig(fig1)  # Gráfico de fluxo
        pdf.savefig(fig2)  # Gráfico de produtos refinados

    plt.show()
    print("✅ Simulação e otimização concluídas!")

if __name__ == "__main__":
    print("Rodando Simulação Normal...")
    simular_fluxo(usar_simpy=False)
    print("\nRodando Simulação com Falhas...")
    simular_fluxo(usar_simpy=True)
