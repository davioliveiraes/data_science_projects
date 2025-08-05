# Deep Learning Matrices - Detecção de Transações Suspeitas

Implementação de uma rede neural simples do zero usando apenas NumPy para detectar transações suspeitas. O projeto demonstra os conceitos fundamentais de deep learning através de álgebra linear pura.

## 🎯 O que faz

O projeto implementa um algoritmo de rede neural que:
- Classifica transações como suspeitas (1) ou normais (0)
- Usa função de ativação sigmoid
- Implementa backpropagation manual
- Treina com dados sintéticos de transações

## 🛠️ Tecnologias

- **Python 3.8+**
- **NumPy** - Operações matriciais

## 🚀 Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/davioliveiraes/data_science_projects.git
cd data_science_projects/deep-learning-matrices
```

### 2. Instale as dependências
```bash
pip install numpy jupyter
```

### 3. Execute o notebook
```bash
jupyter notebook main.ipynb
```

### 4. Execute as células em ordem
O notebook está dividido em 5 partes:
1. **Algoritmo** - Classe da rede neural
2. **Dados** - Preparação dos dados de treino/teste
3. **Treinamento** - Fit do modelo (1000 iterações)
4. **Avaliação** - Teste com dados separados
5. **Deploy** - Previsões em novos dados

## 📊 Exemplo de uso

```python
# Criar modelo
modelo = AlgoritmoNeuralNetworkDSA(taxa_aprendizado=0.01, num_interacoes=1000)

# Treinar
modelo.fit(X_treino, y_treino)

# Fazer previsões
previsoes = modelo.predict(X_test)
```

## 📈 Resultados

O modelo classifica transações baseado em 2 atributos:
- Entrada `[1, 2]` → Não suspeita (0)
- Entrada `[4, 5]` → Suspeita (1)

---