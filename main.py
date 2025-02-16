import logging
import numpy as np
import matplotlib.pyplot as plt
import simpy
from src.models.pipeline import Pipeline
from src.models.refinery import Refinery
from src.visualizacao import plot_fluxo_tempo
from matplotlib.backends.backend_pdf import PdfPages

logger = logging.getLogger(__name__)

# Função para simulação do fluxo de petróleo com o SimPy
def fluxo_petroleo(env, pipeline, refinaria):
    """Processo de fluxo de petróleo com simulação de eventos discretos."""
    
    while True:
        # A cada intervalo de tempo, o petróleo flui pelo duto
        logger.info("Iniciando fluxo de petróleo...")
        fluxo = np.sin(env.now / 4) * 10 + pipeline.capacidade_maxima
        vazao_duto = pipeline.calcular_fluxo(fluxo)
        logger.info(f"Fluxo de petróleo no duto: {vazao_duto:.2f} m³/h")
        
        # Processamento do petróleo pela refinaria
        produtos_refinados = refinaria.processar_petroleo(vazao_duto)
        logger.info(f"Produtos refinados: {produtos_refinados}")
        
        # Simulação do intervalo até o próximo evento
        tempo_entre_eventos = np.random.exponential(1)  # Intervalo aleatório de chegada
        yield env.timeout(tempo_entre_eventos)  # Aguardar o tempo para o próximo evento

def simular_fluxo_petroleo():
    """Função para rodar a simulação com SimPy."""
    
    # Definindo parâmetros do duto
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
    refinaria = Refinery(capacidade_processamento=200000, eficiencia=0.9)

    # Criando o ambiente SimPy
    env = simpy.Environment()
    
    # Adicionando o processo de fluxo de petróleo ao ambiente
    env.process(fluxo_petroleo(env, pipeline, refinaria))

    # Rodando a simulação por um certo período (ex: 24 horas)
    env.run(until=24)

    print("✅ Simulação concluída!")

def main():
    """Função principal para rodar a simulação do fluxo de petróleo."""
    
    simular_fluxo_petroleo()

    # Exibir gráficos, como no seu código original
    tempo = np.linspace(0, 24, 50)
    fluxo = np.sin(tempo / 4) * 10 + 83.3  # Apenas para visualização, ajuste conforme necessário

    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(tempo, fluxo, 'bo-', label="Fluxo de Petróleo")
    ax1.set_xlabel("Tempo (horas)")
    ax1.set_ylabel("Fluxo (barris/hora)")
    ax1.set_title("Variação do Fluxo de Petróleo no Duto")
    ax1.legend()
    ax1.grid(True)

    fig2, ax2 = plt.subplots(figsize=(8, 5))
    produtos_refinados = {"Diesel": 150000, "Gasolina": 100000}  # Exemplo fictício
    produtos = list(produtos_refinados.keys())
    quantidades = list(produtos_refinados.values())
    ax2.bar(produtos, quantidades, color=['red', 'blue', 'green'])
    ax2.set_xlabel("Produtos Refinados")
    ax2.set_ylabel("Quantidade (m³)")
    ax2.set_title("Distribuição de Produtos Refinados")
    ax2.grid(axis="y")

    with PdfPages("graficos_fluxo_petroleo_simpy.pdf") as pdf:
        pdf.savefig(fig1)  # Salva o primeiro gráfico
        pdf.savefig(fig2)  # Salva o segundo gráfico

    # Exibir as duas figuras juntas
    plt.show()

if __name__ == "__main__":
    main()
