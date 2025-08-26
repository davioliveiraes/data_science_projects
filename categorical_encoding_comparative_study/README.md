# Estudo Comparativo de Codificação de Variáveis Categóricas

## 📋 Sobre o Projeto

Este projeto apresenta um estudo comparativo abrangente sobre diferentes técnicas de codificação de variáveis categóricas e seu impacto na performance de modelos de machine learning. O foco está na análise prática de como diferentes métodos de encoding afetam a eficácia preditiva de algoritmos estatísticos.

## 🎯 Objetivos

- **Primário**: Comparar a performance de diferentes técnicas de codificação categórica em tarefas de classificação e regressão
- **Secundário**: Fornecer insights práticos sobre quando usar cada técnica de encoding
- **Terciário**: Analisar trade-offs entre performance, interpretabilidade e custo computacional

## 🧪 Metodologia

### Técnicas de Codificação Avaliadas

| Técnica | Descrição | Casos de Uso |
|---------|-----------|--------------|
| **One-Hot Encoding** | Criação de variáveis dummy binárias | Categóricas nominais com baixa cardinalidade |
| **Ordinal Encoding** | Mapeamento para valores inteiros sequenciais | Categóricas ordinais |
| **Target Encoding** | Substituição pela média da variável target | Alta cardinalidade com relação com target |
| **Count Encoding** | Frequência de cada categoria | Cardinalidade média/alta |
| **Binary Encoding** | Representação binária das categorias | Cardinalidade muito alta |
| **Hash Encoding** | Função hash para reduzir dimensionalidade | Cardinalidade extremamente alta |

### Modelos de Machine Learning

#### Modelos ATI (Affine Transformation on Input)
- Regressão Linear/Logística
- Redes Neurais MLP
- SVM Linear

#### Modelos Baseados em Árvore
- Random Forest
- XGBoost
- LightGBM
- Decision Trees

### Métricas de Avaliação

- **Classificação**: F1-Score, Accuracy, Precision, Recall
- **Regressão**: RMSE, MAE, R²
- **Performance**: Tempo de codificação e treinamento
- **Escalabilidade**: Comportamento com diferentes níveis de cardinalidade

## 📊 Datasets

O estudo utiliza múltiplos datasets com diferentes características:

| Dataset | Tipo | Features Categóricas | Cardinalidade | Target |
|---------|------|---------------------|---------------|--------|
| Titanic | Classificação | 3 | Baixa-Média | Sobrevivência |
| Adult Income | Classificação | 8 | Baixa-Alta | Renda >50K |
| House Prices | Regressão | 43 | Baixa-Alta | Preço |
| Mushrooms | Classificação | 22 | Baixa | Venenoso/Comestível |

## 🔧 Tecnologias Utilizadas

```python
# Principais bibliotecas
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
category-encoders==2.6.0
xgboost==1.7.6
lightgbm==4.0.0
matplotlib==3.7.2
seaborn==0.12.2
plotly==5.15.0
```

## 🚀 Como Executar

### 1. Clone o Repositório
```bash
git clone https://github.com/davioliveiraes/data_science_projects.git
cd data_science_projects/categorical_encoding_comparative_study
```

### 1. Crie e Ative o Ambiente Conda
```bash
# Criar ambiente conda com Python 3.13
conda create -n categorical_encoding_comparative_study python=3.13 -y

# Ativar o ambiente
conda activate categorical_encoding_comparative_study
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o Notebook Principal
```bash
jupyter notebook categorical_encoding_comparative_study.ipynb
```

## 📈 Principais Descobertas

### Insights Gerais

1. **One-Hot Encoding** se mostrou superior para modelos lineares e redes neurais
2. **Target Encoding** apresentou melhor performance em datasets com alta cardinalidade
3. **Modelos baseados em árvore** são mais robustos à escolha do encoder
4. **Trade-off** entre performance e interpretabilidade varia por domínio

### Performance por Tipo de Modelo

| Modelo | Melhor Encoder | F1-Score Médio | Tempo (s) |
|--------|---------------|----------------|-----------|
| Regressão Logística | One-Hot | 0.847 | 2.3 |
| Random Forest | Target | 0.892 | 15.7 |
| XGBoost | Count | 0.901 | 8.4 |
| MLP | One-Hot | 0.834 | 45.2 |

### Recomendações Práticas

#### Para Baixa Cardinalidade (< 10 categorias)
- ✅ **One-Hot Encoding** para todos os modelos
- ✅ **Ordinal Encoding** se há ordem natural

#### Para Média Cardinalidade (10-100 categorias)  
- ✅ **Target Encoding** para modelos baseados em árvore
- ✅ **Binary Encoding** para modelos lineares

#### Para Alta Cardinalidade (> 100 categorias)
- ✅ **Hash Encoding** com dimensionalidade controlada
- ✅ **Target Encoding** com validação cruzada

## 📚 Fundamentação Teórica

### Por que One-Hot é Universal para Modelos ATI?

Modelos que aplicam transformações afins nos dados de entrada (como regressão linear e redes neurais) se beneficiam do One-Hot Encoding porque:

1. **Preserva a independência** entre categorias
2. **Evita ordinação artificial** de variáveis nominais
3. **Permite aprendizado otimizado** de pesos para cada categoria

### Vantagens dos Modelos Baseados em Árvore

Decision Trees e algoritmos derivados são mais flexíveis com encoding porque:

1. **Particionam** o espaço de features naturalmente
2. **Lidam bem com variáveis ordinais** sem preparação especial
3. **São robustos** a diferentes escalas e distribuições

## 🔍 Análise de Complexidade

### Complexidade Computacional por Encoder

| Encoder | Tempo | Espaço | Cardinalidade |
|---------|-------|--------|---------------|
| One-Hot | O(n×k) | O(k) | Problemático para k > 100 |
| Ordinal | O(n) | O(1) | Escalável |
| Target | O(n) | O(k) | Escalável |
| Hash | O(n) | O(h) | Muito escalável |
