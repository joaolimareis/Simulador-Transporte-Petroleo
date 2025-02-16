import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.utils.logger import get_logger
logger = get_logger(__name__)

class Transport:
    """Classe que representa o transporte de derivados."""

    def __init__(self, capacidade_caminhao, distancia, eficiencia_transporte):
        """
        Inicializa o transporte de derivados.

        :param capacidade_caminhao: Capacidade máxima de transporte (m³)
        :param distancia: Distância do transporte (km)
        :param eficiencia_transporte: Eficiência do transporte (0 a 1)
        """
        self.capacidade_caminhao = capacidade_caminhao
        self.distancia = distancia
        self.eficiencia_transporte = eficiencia_transporte
        logger.info(f"🚚 Caminhão criado: Capacidade {capacidade_caminhao} m³ | Distância {distancia} km | Eficiência {eficiencia_transporte * 100:.1f}%")

    def transportar_produto(self, produto, quantidade):
        """
        Transporta o produto refinado.

        :param produto: Nome do produto a ser transportado
        :param quantidade: Quantidade do produto (m³)
        :return: Quantidade transportada
        """
        logger.info(f"🚚 Transportando {quantidade:.2f} m³ de {produto}")
        
        # A quantidade transportada não pode ser maior que a capacidade do caminhão
        quantidade_transportada = min(quantidade, self.capacidade_caminhao)
        
        # Ajuste pela eficiência do transporte
        quantidade_transportada *= self.eficiencia_transporte
        
        logger.info(f"🔄 Quantidade transportada de {produto}: {quantidade_transportada:.2f} m³")
        return quantidade_transportada

    def __str__(self):
        return f"Transporte - Capacidade: {self.capacidade_caminhao} m³ | Distância: {self.distancia} km | Eficiência: {self.eficiencia_transporte * 100:.1f}%"
