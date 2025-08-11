# Aplicação Prática de Autovetores e Autovalores com PCA

Implementação prática da **Análise de Componentes Principais (PCA)** usando conceitos fundamentais de álgebra linear: autovetores e autovalores para redução de dimensionalidade.

## 🎯 Finalidade

Demonstrar na prática como PCA funciona através de:
- **3 implementações diferentes** do algoritmo PCA
- Redução de dimensionalidade (49 → 10 variáveis)
- Aplicação de conceitos matemáticos em Data Science
- Comparação entre implementação manual vs scikit-learn

## 🛠️ Tecnologias

- **Python 3.9+**
- **NumPy** - Operações matemáticas e álgebra linear
- **Pandas** - Manipulação de dados
- **Scikit-learn** - PCA implementado
- **IPython** - Visualização de imagens explicativas

## 📊 Dataset

- **40 alunos** respondendo quiz com **49 perguntas**
- Dados fictícios para demonstração
- Formato: matriz 40x49 (linhas=alunos, colunas=respostas)

## 🚀 Como Executar

### 1. Preparar Ambiente
```bash
# Criar ambiente conda
conda create -n pca-eigenvalues python=3.9
conda activate pca-eigenvalues

# Instalar dependências
pip install numpy pandas scikit-learn ipython
```

### 2. Executar o Código
```python
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

# Carregar dados
df_dsa = pd.read_csv("dataset.csv", index_col=0)
dsa_matrix = df_dsa.to_numpy()

# Versão 1: PCA Manual (básico)
pca_out_v1, eigenval_v1, _, _ = PCA_DSA_V1(dsa_matrix)

# Versão 2: PCA Manual (otimizado)
pca_out_v2, eigenval_v2, _, _ = PCA_DSA_V2(dsa_matrix)

# Versão 3: Scikit-learn
pca = PCA(n_components=10)
X_pca = pca.fit_transform(dsa_matrix)
```

## 📈 Resultados Principais

- **95.78%** da variância explicada com apenas **10 componentes** (de 49 originais)
- **Redução de 80%** na dimensionalidade mantendo a informação essencial
- Comparação entre 3 implementações diferentes do algoritmo

## 🔬 Conceitos Implementados

### Algoritmo PCA Passo a Passo:
1. **Centralização**: Subtrair média de cada variável
2. **Matriz de Covariância**: Calcular ZᵀZ
3. **Decomposição**: Encontrar autovetores e autovalores
4. **Ordenação**: Classificar por importância (autovalores)
5. **Transformação**: Projetar dados nos novos eixos
6. **Seleção**: Escolher componentes mais relevantes

### Matemática Aplicada:
- **Autovetores**: Direções principais de variação
- **Autovalores**: Magnitude/importância de cada direção
- **Matriz de Covariância**: Relacionamento entre variáveis
- **Variância Explicada**: Proporção de informação preservada

## 📁 Estrutura do Projeto

```
├── dataset.csv          # Dados dos 40 alunos
├── img/                 # Imagens explicativas do PCA
├── pca_analysis.py      # Implementações do algoritmo
└── README.md
```

## 🎓 Aplicações Práticas

- **Compressão de dados** sem perda significativa
- **Visualização** de dados multidimensionais
- **Pré-processamento** para Machine Learning
- **Detecção de padrões** em datasets complexos

---
*Projeto educacional de Matemática e Estatística aplicada para Data Science, Machine Learning e IA*