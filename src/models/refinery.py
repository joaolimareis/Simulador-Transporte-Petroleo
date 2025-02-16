import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.utils.logger import get_logger
logger = get_logger(__name__)

class Refinery:
    """Classe que representa uma refinaria de petróleo."""

    def __init__(self, capacidade_processamento, eficiencia):
        """
        Inicializa a refinaria.

        :param capacidade_processamento: Capacidade de processamento de petróleo (m³/h)
        :param eficiencia: Eficiência da refinaria para transformar petróleo em produtos refinados
        """
        self.capacidade_processamento = capacidade_processamento
        self.eficiencia = eficiencia
        logger.info(f"🏭 Refinaria criada: Capacidade {capacidade_processamento} m³/h | Eficiência {eficiencia * 100:.1f}%")

    def processar_petroleo(self, quantidade_petroleo):
        """
        Processa o petróleo para produzir derivados.

        :param quantidade_petroleo: Quantidade de petróleo a ser processada (m³)
        :return: Produtos refinados
        """
        logger.info(f"🔄 Processando {quantidade_petroleo:.2f} m³ de petróleo")
        
        # Cálculo de produtos refinados com base na eficiência
        produtos = {
            "gasolina": 0.4 * quantidade_petroleo * self.eficiencia,   # 40% do petróleo vira gasolina
            "diesel": 0.35 * quantidade_petroleo * self.eficiencia,      # 35% vira diesel
            "querosene": 0.15 * quantidade_petroleo * self.eficiencia,    # 15% vira querosene
            "residuos": 0.1 * quantidade_petroleo * self.eficiencia       # 10% vira resíduos
        }

        logger.info(f"🛢️ Produtos refinados: {produtos}")
        return produtos

    def __str__(self):
        return f"Refinaria - Capacidade: {self.capacidade_processamento} m³/h | Eficiência: {self.eficiencia * 100:.1f}%"
