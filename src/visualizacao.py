import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def plot_fluxo_tempo(tempo, fluxo):
    """Gera um gráfico do fluxo de petróleo ao longo do tempo."""
    plt.figure(figsize=(10, 5))
    plt.plot(tempo, fluxo, marker='o', linestyle='-', color='b', label="Fluxo de Petróleo")
    plt.xlabel("Tempo (horas)")
    plt.ylabel("Fluxo (barris/hora)")
    plt.title("Variação do Fluxo de Petróleo no Duto")
    plt.legend()
    plt.grid()
    plt.show()

def plot_mapa_dutos(edges):
    """Gera um mapa de dutos usando NetworkX."""
    G = nx.Graph()
    G.add_edges_from(edges)

    plt.figure(figsize=(6, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=12)
    plt.title("Mapa da Rede de Dutos")
    plt.show()

def plot_custos_dutos(dutos, custos):
    """Gera um gráfico de barras comparando os custos dos dutos."""
    plt.figure(figsize=(8, 5))
    plt.bar(dutos, custos, color=['red', 'blue', 'green', 'purple'])
    plt.xlabel("Dutos")
    plt.ylabel("Custo ($)")
    plt.title("Comparação de Custos entre Diferentes Dutos")
    plt.grid(axis="y")
    plt.show()

