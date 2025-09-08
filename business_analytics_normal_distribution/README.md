# Distribuições de Probabilidade para Análise de Negócios

## 📊 Sobre o Projeto

Este projeto demonstra como aplicar distribuições de probabilidade de variáveis contínuas para responder perguntas de negócios importantes. Através de análises estatísticas e visualizações, o projeto aborda cenários práticos como controle de qualidade, análise de durabilidade de produtos e gerenciamento de riscos.

## 🎯 Objetivos

- Aplicar conceitos de estatística e probabilidade em contextos empresariais
- Visualizar distribuições de probabilidade para facilitar a tomada de decisões
- Calcular probabilidades específicas para cenários de negócios
- Demonstrar o uso prático da **Distribuição Normal**, **Distribuição Uniforme** e **Distribuição Exponencial**

## 🔧 Tecnologias Utilizadas

### Linguagem
- **Python 3.x**

### Bibliotecas Principais
- **NumPy**: Computação numérica e arrays
- **SciPy**: Funções estatísticas e distribuições de probabilidade
- **Matplotlib**: Criação de gráficos e visualizações
- **SciPy.stats**: Distribuições estatísticas (normal, uniforme, exponencial)
- **SciPy.integrate**: Cálculo de integrais numéricas

## 📈 Conceitos Abordados

### 1. Distribuição Normal
- **Aplicação**: Análise da vida útil de lâmpadas LED
- **Parâmetros**: μ = 10.000 horas, σ = 1.200 horas
- **Questões de Negócio**:
  - Probabilidade de uma lâmpada durar mais de 12.000 horas
  - Probabilidade de duração entre 9.000 e 11.000 horas
  - Probabilidade de duração inferior a 7.500 horas
  - Aplicação da Regra Empírica (68-95-99.7%)

### 2. Distribuição Uniforme
- **Aplicação**: Controle de qualidade no comprimento de peças
- **Parâmetros**: Intervalo [5.2, 15.7] cm
- **Questões de Negócio**:
  - Probabilidade de produzir uma peça com comprimento específico
  - Análise de variabilidade na produção

### 3. Distribuição Exponencial
- **Aplicação**: Análise de incidentes e tempo entre eventos
- **Questões de Negócio**:
  - Probabilidade de ocorrência de pelo menos um incidente em determinado período

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter Python 3.x instalado em seu sistema. Você pode verificar executando:

```bash
python --version
```

### Instalação das Dependências

1. **Clone ou baixe o projeto**

```bash
git clone https://github.com/davioliveiraes/data_science_projects.git
cd data_science_projects/business_analytics_normal_distribution
```

2. **Crie e ative o ambiente Conda**:

```bash
# Criar ambiente conda com Python 3.13
conda create -n business_analytics_normal_distribution python=3.13 -y

# Ativar o ambiente
conda activate business_analytics_normal_distribution
```

3. **Instale as bibliotecas necessárias**:

```bash
pip install -r requirements.txt
```

### Execução

1. **Execute as células do arquivo principal**:

```bash
business_analytcs_normal_distribution.ipynb
```

2. **O programa irá gerar**:
   - Gráficos das distribuições de probabilidade
   - Cálculos de probabilidades específicas
   - Visualizações das áreas sob as curvas
   - Resultados numéricos impressos no console

## 📊 Exemplos de Saída

### Gráficos Gerados
- Distribuição Normal Padrão com área sombreada
- Distribuição Uniforme com região de interesse
- Distribuição Normal da vida útil das lâmpadas
- Visualização da Regra Empírica (±1σ, ±2σ, ±3σ)

### Resultados Calculados
```
Probabilidade de lâmpada durar > 12.000 horas: X.XX%
Probabilidade de duração entre 9.000-11.000 horas: X.XX%
Probabilidade de duração < 7.500 horas: X.XX%
Probabilidade de produzir peça de 6.5 cm: X.XX%
Probabilidade de pelo menos 1 incidente na próxima hora: X.XX%
```

## 🔍 Casos de Uso Empresariais

### Manufatura
- **Controle de Qualidade**: Análise de variabilidade na produção
- **Planejamento de Manutenção**: Previsão de falhas em equipamentos

### Gestão de Produtos
- **Garantia**: Definição de períodos de garantia baseados em probabilidade
- **Estoque**: Planejamento de reposição baseado em vida útil

### Análise de Riscos
- **Incidentes**: Probabilidade de ocorrência de eventos adversos
- **Seguros**: Cálculo de prêmios baseados em distribuições de risco

## 📚 Fundamentos Teóricos

### Função Densidade de Probabilidade (PDF)
Representa a probabilidade relativa de uma variável contínua assumir um valor específico.

### Função Distribuição Acumulada (CDF)
Representa a probabilidade de uma variável assumir um valor menor ou igual a um determinado ponto.

### Regra Empírica (68-95-99.7%)
- 68% dos dados estão dentro de ±1 desvio padrão da média
- 95% dos dados estão dentro de ±2 desvios padrão da média
- 99.7% dos dados estão dentro de ±3 desvios padrão da média

## 📝 Estrutura do Código

```
├── business_analytics_normal_distribution.ipynb    # Script principal
├── requirements.txt                  # Dependências do projeto
├── README.md                        # Este arquivo
└── img_graphics/                        # Pasta para salvar gráficos (opcional)
```

## 🤝 Contribuições

Este projeto é ideal para:
- Estudantes de estatística e ciência de dados
- Analistas de negócios
- Profissionais de controle de qualidade
- Pesquisadores em análise de riscos

Sinta-se à vontade para contribuir com melhorias, novos exemplos ou correções!
