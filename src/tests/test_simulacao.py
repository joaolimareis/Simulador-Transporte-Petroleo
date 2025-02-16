import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.models.pipeline import Pipeline
from src.models.refinery import Refinery
from src.models.transport import Transport

class TestSimulacao(unittest.TestCase):

    def test_pipeline(self):
    # Ajuste para evitar perdas muito grandes
        duto = Pipeline(0.2032, 27000, 0.0001, 0.05, 3500000, 2500000, 0.02, 83.3)
        vazao = duto.calcular_fluxo(850)
        self.assertLessEqual(vazao, 83.3, "A vazão deve respeitar o limite do duto")


    def test_refinery(self):
        refinaria = Refinery(500, 0.9)
        produtos = refinaria.processar_petroleo(100)
        self.assertGreater(produtos["gasolina"], 0, "A refinaria deve produzir gasolina")

    def test_transport(self):
        # Corrigir a criação do objeto Transport e usar o método correto
        caminhao = Transport(capacidade_caminhao=50000, distancia=1000, eficiencia_transporte=0.9)
        quantidade_transportada = caminhao.transportar_produto(produto="gasolina", quantidade=50000)
        self.assertGreater(quantidade_transportada, 0, "A quantidade transportada deve ser positiva")


        
if __name__ == "__main__":
    unittest.main()
