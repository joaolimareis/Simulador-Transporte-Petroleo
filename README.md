# **Documentação do Projeto: Simulação e Otimização no Transporte de Petróleo**

## **Visão geral**

Este projeto simula o fluxo de petróleo em dutos e otimiza rotas de transporte usando algoritmos de otimização. Ele incorpora aprendizado de máquina para prever falhas no processo de transporte e fornece ferramentas de visualização para analisar o fluxo de óleo e a eficiência do sistema de transporte.

## **Índice**

1. **Instalação**
2. **Uso**
3. **Estrutura do Projeto**
4. **Classes e funções**
5. **Teste**
6. **Log**
7. **Contribuindo**
8. **Licença**

## **Instalação**

Para configurar o projeto, certifique-se de ter o Python instalado (de preferência versão 3.6 ou superior). Em seguida, instale os pacotes necessários usando pip:

```
bashRunCopy code
1pip install -r requirements.txt

```

## **Uso**

Para executar a simulação, execute o arquivo. Isso simulará o fluxo de óleo e otimizará as rotas de transporte. Você pode optar por executar a simulação com ou sem cenários de falha.**`main.py`**

```
bashRunCopy code
1python main.py

```

## **Estrutura do Projeto**

O projeto está organizado da seguinte forma:

```
RunCopy code
1MultipleFiles/
2│
3├── src/
4│   ├── models/
5│   │   ├── pipeline.py
6│   │   ├── refinery.py
7│   │   ├── transport.py
8│   │   └── simulacao.py
9│   ├── utils/
10│   │   ├── logger.py
11│   │   └── visualizacao.py
12│   ├── otimizacao.py
13│   └── __init__.py
14│
15├── tests/
16│   ├── test_pipeline.py
17│   ├── test_simulacao.py
18│   └── test_transport.py
19│
20├── main.py
21├── requirements.txt
22├── README.md
23└── LICENSE

```

## **Classes e funções**

### **1. Oleoduto**

- **Descrição**: Representa um oleoduto para transporte de petróleo.
- **Métodos-chave**:
    - **`calcular_fluxo(entrada_petroleo)`**
        
        : Calcula o fluxo final considerando as perdas durante o transporte.
        
    - **`calcular_vazao_darcy_weisbach(densidade_petroleo)`**
        
        : Calcula o fluxo volumétrico usando a equação de Darcy-Weisbach.
        

### **2. Refinaria**

- **Descrição**: Representa uma refinaria de petróleo.
- **Métodos-chave**:
    - **`processar_petroleo(quantidade_petroleo)`**
        
        : Processa óleo para produzir produtos refinados.
        

### **3. Transporte**

- **Descrição**: Representa o transporte de produtos refinados.
- **Métodos-chave**:
    - **`transportar_produto(produto, quantidade)`**
        
        : Transporta uma quantidade especificada de um produto.
        

### **4. Simulação**

- **Descrição**: Simula o transporte de óleo usando um gráfico direcionado.
- **Métodos-chave**:
    - **`transportar_petroleo(origem, destino)`**
        
        : Simula o transporte de óleo entre dois pontos.
        
    - **`introduzir_falhas(origem, destino)`**
        
        : Simula falhas intermitentes no transporte.
        

### **5. OtimizadorRotas**

- **Descrição**: implementa o algoritmo A* para otimização de rotas.
- **Métodos-chave**:
    - **`a_star(inicio, fim, criterio)`**
        
        : Encontra a rota ideal com base no critério especificado (custo, distância, capacidade).
        

## **Teste**

O projeto inclui testes unitários para garantir a funcionalidade dos componentes principais. Os testes estão localizados no diretório. Para executar os testes, use o seguinte comando:**`tests`**

```
bashRunCopy code
1python -m unittest discover -s tests

```

## **Log**

O projeto usa um sistema de registro para rastrear eventos e erros. Os registros são salvos em um arquivo chamado . A configuração de log é definida em .**`simulacao.loglogger.py`**

## **Contribuindo**

Contribuições são bem-vindas! Faça um fork do repositório e envie uma solicitação de pull com suas alterações. Certifique-se de que seu código esteja de acordo com os padrões de codificação do projeto e inclua os testes apropriados.

## **Licença**

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
