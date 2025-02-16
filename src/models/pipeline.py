import sys
import os
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.utils.logger import get_logger

logger = get_logger(__name__)

class Pipeline:
    """Classe que representa um duto de transporte de petróleo."""

    def __init__(self, diametro, comprimento, rugosidade, viscosidade, pressao_inicial, pressao_final, perda_carga, capacidade_maxima):
        """
        Inicializa o duto com base nos dados reais do Oleoduto Candeias-Mataripe.

        :param diametro: Diâmetro interno do duto (m)
        :param comprimento: Comprimento do duto (m)
        :param rugosidade: Rugosidade do duto (m)
        :param viscosidade: Viscosidade do petróleo (Pa.s)
        :param pressao_inicial: Pressão inicial no duto (Pa)
        :param pressao_final: Pressão final no duto (Pa)
        :param perda_carga: Perda de carga no duto (m/m)
        :param capacidade_maxima: Capacidade máxima do duto (m³/h)
        """
        self.diametro = diametro
        self.comprimento = comprimento
        self.rugosidade = rugosidade
        self.viscosidade = viscosidade
        self.pressao_inicial = pressao_inicial
        self.pressao_final = pressao_final
        self.perda_carga = perda_carga
        self.capacidade_maxima = capacidade_maxima  # Limite de vazão

        # Calcula a perda por km (percentual)
        self.perda_por_km = self.perda_carga / self.comprimento

        logger.info(f"🛠️ Duto criado: Capacidade {capacidade_maxima} m³/h | Comprimento {comprimento / 1000} km | Perda {self.perda_por_km*100:.2f}%/km")

    def calcular_fluxo(self, entrada_petroleo):
        """
        Calcula a vazão final considerando perdas no percurso.

        :param entrada_petroleo: Quantidade inicial de petróleo (m³)
        :return: Quantidade final após transporte (m³)
        """
        logger.info(f"⛽ Iniciando transporte: {entrada_petroleo:.2f} m³")

        # Garantir que não ultrapasse a capacidade máxima do duto
        if entrada_petroleo > self.capacidade_maxima:
            logger.warning(f"⚠️ Capacidade do duto excedida! Fluxo ajustado para {self.capacidade_maxima} m³/h.")
            entrada_petroleo = self.capacidade_maxima

        # Cálculo da perda total ao longo do percurso
        perda_total = entrada_petroleo * self.perda_por_km * (self.comprimento / 1000)  # Ajustado para km
        logger.debug(f"📉 Perda por km: {self.perda_por_km * 100:.2f}% | Comprimento do duto: {self.comprimento / 1000} km")
        logger.debug(f"📉 Perda total calculada: {perda_total:.2f} m³")

        # Garante que o fluxo final nunca seja negativo
        fluxo_final = max(entrada_petroleo - perda_total, 0)

        logger.info(f"📉 Perda total: {perda_total:.2f} m³ | Fluxo final: {fluxo_final:.2f} m³")
        return fluxo_final

    def calcular_vazao_darcy_weisbach(self, densidade_petroleo):
        """
        Calcula a vazão volumétrica do duto utilizando a equação de Darcy-Weisbach.

        :param densidade_petroleo: Densidade do petróleo (kg/m³)
        :return: Vazão volumétrica (m³/h)
        """
        # Área da seção transversal do duto
        area = math.pi * (self.diametro / 2) ** 2

        # Diferença de pressão
        pressao_diferencial = self.pressao_inicial - self.pressao_final

        # Cálculo da vazão baseado na equação de Darcy-Weisbach
        vazao = (pressao_diferencial / (self.viscosidade * self.perda_carga)) * area
        vazao_m3_h = vazao * 3600  # Converter para m³/h

        # Limita a vazão à capacidade máxima do duto
        vazao_m3_h = min(vazao_m3_h, self.capacidade_maxima)

        logger.info(f"🔬 Cálculo de vazão pelo modelo de Darcy-Weisbach: {vazao_m3_h:.2f} m³/h (Máx: {self.capacidade_maxima} m³/h)")
        return vazao_m3_h

    def __str__(self):
        return f"Duto - Capacidade: {self.capacidade_maxima} m³/h | Comprimento: {self.comprimento / 1000} km | Perda/km: {self.perda_por_km*100:.2f}%"
