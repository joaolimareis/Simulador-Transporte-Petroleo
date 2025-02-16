import logging
import numpy as np
import matplotlib.pyplot as plt
from src.models.pipeline import Pipeline
from src.models.refinery import Refinery
from src.models.transport import Transport
from src.visualizacao import plot_fluxo_tempo, plot_custos_dutos

logger = logging.getLogger(__name__)

def main():
    """Função principal para rodar a simulação do fluxo de petróleo."""

    # Parâmetros do duto
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

    # Criar duto
    pipeline = Pipeline(**parametros_duto)

    # Simulação do fluxo de petróleo
    tempo = np.linspace(0, 24, 50)  # Simulação de 24h
    fluxo = np.sin(tempo / 4) * 10 + parametros_duto["capacidade_maxima"]  # Simulação de variação

    vazao_duto = pipeline.calcular_fluxo(parametros_duto["capacidade_maxima"])
    logger.info(f"📌 Simulação do duto:\nVazão do Duto: {vazao_duto:.2f} m³/h\n")

    # 🟢 Gráfico: Fluxo de petróleo ao longo do tempo
    plot_fluxo_tempo(tempo, fluxo)

    # Criar refinaria
    refinaria = Refinery(capacidade_processamento=200000, eficiencia=0.9)

    # Processamento do petróleo bruto
    produtos_refinados = refinaria.processar_petroleo(vazao_duto)
    logger.info(f"📌 Processamento na Refinaria:\nProdutos refinados: {produtos_refinados}\n")

    # Criar transporte
    transporte = Transport(capacidade_caminhao=350000, distancia=150, eficiencia_transporte=0.9)

    # Transporte dos produtos refinados
    transporte_gasolina = transporte.transportar_produto("gasolina", produtos_refinados["gasolina"])
    transporte_diesel = transporte.transportar_produto("diesel", produtos_refinados["diesel"])
    transporte_querosene = transporte.transportar_produto("querosene", produtos_refinados["querosene"])

    logger.info(f"📌 Transporte de Produtos Refinados:\n"
                f"Gasolina transportada: {transporte_gasolina:.2f} m³\n"
                f"Diesel transportado: {transporte_diesel:.2f} m³\n"
                f"Querosene transportado: {transporte_querosene:.2f} m³\n")

    # 🟢 Gráfico: Comparação dos produtos refinados
    produtos = list(produtos_refinados.keys())
    quantidades = list(produtos_refinados.values())
    plt.figure(figsize=(8, 5))
    plt.bar(produtos, quantidades, color=['red', 'blue', 'green'])
    plt.xlabel("Produtos Refinados")
    plt.ylabel("Quantidade (m³)")
    plt.title("Distribuição de Produtos Refinados")
    plt.grid(axis="y")
    plt.show()

    print("✅ Simulação concluída! Verifique o arquivo de log para detalhes.")

if __name__ == "__main__":
    main()
