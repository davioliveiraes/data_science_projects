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

### 2. Instalar Anaconda (Se não tiver instalado)
```bash
# Linux/WSL
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
bash Anaconda3-2023.09-0-Linux-x86_64.sh

# Windows: Baixe o instalador em https://www.anaconda.com/download
# macOS: Baixe o instalador em https://www.anaconda.com/download
```

### 3. Criar e ativar ambiente conda
```bash
# Criar ambiente
conda create -n deep_learning_matrices python=3.12 -y

# Ativar ambiente
conda activate deep_learning_matrices
```

### 4. Instale as dependências
```bash
pip install numpy jupyter
```

### 5. Execute o notebook
```bash
jupyter notebook deep_learning_matrices.ipynb
```

### 6. Execute as células em ordem
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