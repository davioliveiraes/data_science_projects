# Análise RFM e Dashboard Interativo Para Marketing

Projeto de **Business Analytics e Machine Learning** aplicado à segmentação de clientes usando a metodologia RFM (Recency, Frequency, Monetary Value).

## 🎯 Finalidade

Realizar análise RFM de dados de e-commerce brasileiro para segmentar clientes e gerar insights estratégicos para a área de marketing, incluindo:

- Classificação de clientes em segmentos (VIP, Leais, Perdidos, etc.)
- Identificação de padrões de comportamento de compra
- Recomendações personalizadas de ações de marketing
- Visualização interativa dos resultados através de dashboard

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Pandas** - Manipulação e análise de dados
- **Scikit-learn** - Pré-processamento (LabelEncoder)
- **Matplotlib & Seaborn** - Visualizações estáticas
- **Plotly** - Dashboard interativo
- **Squarify** - Gráficos treemap

## ▶️ Como Executar

1. **Clone o repositório**
```bash
git clone https://github.com/davioliveiraes/data_science_projects.git
cd data_science_projects/rfm_customer_segmentation
```

2. **Crie um ambiente conda com Python 3.13**
```bash
conda create -name rfm_customer_segmentation python=3.13
conda activate rfm_customer_segmentation
```

3. **Instale as dependências**
```bash
pip3 install -r requirements.txt
```

4. **Execute o notebook**
```bash
jupyter notebook rfm_customer_segmentation.ipynb
```

5. **Dataset necessário**: `dataset.csv` (dados de e-commerce brasileiro)
