# Manutenção Preditiva de Máquinas Industriais com Machine Learning

Projeto de Machine Learning para prever a necessidade de manutenção em máquinas industriais através de dados coletados por sensores IoT (Internet of Things).

---

## Finalidade

Este projeto tem como finalidade desenvolver um modelo de Machine Learning capaz de prever se uma máquina industrial necessita ou não de manutenção, utilizando dados históricos coletados de 178 sensores IoT.

### Objetivos Principais

- Construir um modelo preditivo para classificação binária (necessita manutenção: Sim/Não)
- Comparar diferentes algoritmos de Machine Learning para identificar o mais eficaz
- Aplicar técnicas de pré-processamento e balanceamento de dados
- Otimizar hiperparâmetros para maximizar a performance do modelo
- Disponibilizar um modelo treinado pronto para uso em produção

### Aplicações Práticas

- **Indústria 4.0**: Monitoramento inteligente de equipamentos industriais
- **Redução de Custos**: Prevenção de paradas não programadas e manutenções corretivas emergenciais
- **Aumento de Produtividade**: Planejamento otimizado de manutenções preventivas
- **Gestão de Ativos**: Prolongamento da vida útil de máquinas e equipamentos
- **Segurança**: Prevenção de falhas que podem causar acidentes de trabalho

---

## Tecnologias Utilizadas

| Tecnologia | Versão | Finalidade |
|------------|--------|------------|
| Python | 3.11+ | Linguagem principal |
| Pandas | - | Manipulação e análise de dados |
| NumPy | - | Operações numéricas |
| Scikit-learn | - | Algoritmos de ML e métricas |
| XGBoost | - | Algoritmo de Gradient Boosting |
| Matplotlib | - | Visualização de dados |
| Seaborn | - | Visualização estatística |
| Pickle | - | Serialização de modelos |

### Algoritmos Implementados

- **Regressão Logística** - Modelo linear para classificação
- **Gaussian Naive Bayes** - Modelo probabilístico
- **XGBoost Classifier** - Árvore de decisão com boosting (melhor performance)

---

## Como Executar

### Pré-requisitos

- Python 3.11 ou superior
- Anaconda ou Miniconda (recomendado)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/davioliveiraes/data_science_projects.git
cd data_science_projects/predictive-maintenance-ml
```

2. Crie e ative o ambiente virtual:
```bash
conda create -n predictive_maintenance python=3.11
conda activate predictive_maintenance
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Execução

1. Inicie o Jupyter Notebook:
```bash
jupyter notebook
```

2. Abra o arquivo `predictive_maintenance_ml_template.ipynb`

3. Execute as células sequencialmente (Shift + Enter)

### Usando o Modelo Treinado

```python
import pickle
import pandas as pd

# Carregar o modelo e o scaler
modelo = pickle.load(open("melhor_modelo_mmi.pkl", "rb"))
scaler = pickle.load(open("scaler.sav", "rb"))

# Carregar novos dados de sensores (178 features)
novos_dados = pd.read_csv("novos_dados.csv")

# Pré-processar e fazer previsão
dados_scaled = scaler.transform(novos_dados)
previsao = modelo.predict(dados_scaled)

# Resultado: 0 = Não precisa manutenção | 1 = Precisa manutenção
print(f"Previsão: {'Manutenção Necessária' if previsao[0] == 1 else 'Máquina OK'}")
```

---

## Conceitos Aprendidos

### Processo de Machine Learning

1. **Definição do Problema**: Classificação binária para manutenção preditiva
2. **Compreensão dos Dados**: Análise exploratória de 11.500 registros com 178 features
3. **Pré-processamento**: Limpeza, normalização com StandardScaler
4. **Divisão dos Dados**: Split em treino (70%), validação (15%) e teste (15%)
5. **Balanceamento de Classes**: Técnica de undersampling para equilibrar classes desbalanceadas
6. **Treinamento**: Comparação de múltiplos algoritmos
7. **Avaliação**: Métricas de AUC-ROC, Acurácia, Precisão, Recall e Especificidade
8. **Otimização**: GridSearchCV para tuning de hiperparâmetros
9. **Deploy**: Serialização do modelo com Pickle

### Métricas de Avaliação

| Métrica | Descrição |
|---------|-----------|
| **AUC-ROC** | Área sob a curva ROC - capacidade de discriminação do modelo |
| **Acurácia** | Proporção de previsões corretas |
| **Precisão** | Proporção de positivos previstos que são realmente positivos |
| **Recall** | Proporção de positivos reais que foram identificados corretamente |
| **Especificidade** | Proporção de negativos reais identificados corretamente |

### Resultados do Melhor Modelo (XGBoost Otimizado)

| Conjunto | AUC | Acurácia | Recall | Precisão |
|----------|-----|----------|--------|----------|
| Validação | 0.993 | 96.5% | 95.3% | 88.1% |
| Teste | ~0.99 | ~96% | ~95% | ~88% |

### Técnicas de Balanceamento

- **Undersampling**: Redução da classe majoritária para igualar à minoritária
- **Oversampling**: Replicação/geração sintética de dados da classe minoritária (conceito abordado)

---

## 📖 Referências

- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Data Science Academy](https://www.datascienceacademy.com.br/)
- [PEP 668 - Python Virtual Environments](https://peps.python.org/pep-0668/)

---
