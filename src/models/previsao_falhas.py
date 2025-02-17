import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from src.simulacao import Simulacao

class SimulacaoML(Simulacao):
    def treinar_modelo_falhas(self):
        """Treina um modelo de Machine Learning para prever falhas no transporte."""
        dados = []
        for tempo, fluxo in self.historico_fluxo:
            falha = 1 if tempo in self.tempo_falhas else 0  # Define se houve falha naquele tempo
            dados.append([tempo, fluxo, falha])
        
        df = pd.DataFrame(dados, columns=["tempo", "fluxo", "falha"])
        
        X = df[["tempo", "fluxo"]]  # Features
        y = df["falha"]  # Target (1 = falha, 0 = normal)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        modelo = RandomForestClassifier(n_estimators=100, random_state=42)
        modelo.fit(X_train, y_train)
        
        previsoes = modelo.predict(X_test)
        acuracia = accuracy_score(y_test, previsoes)
        print(f"🔍 Precisão do Modelo de Previsão de Falhas: {acuracia:.2f}")

        return modelo
    
    def prever_falha(self, modelo, tempo, fluxo):
        """Usa o modelo treinado para prever se haverá falha no transporte."""
        previsao = modelo.predict([[tempo, fluxo]])[0]
        if previsao == 1:
            print(f"⚠️ ALERTA! Possível falha detectada no tempo {tempo:.1f}h!")
        else:
            print(f"✅ Transporte seguro no tempo {tempo:.1f}h.")
