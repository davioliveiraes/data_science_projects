# Template de Projetos de Data Science: Análise de Sentimento em Avaliações de Usuários

## 🎯 Finalidade

Este projeto tem como objetivo desenvolver um sistema automatizado de análise de sentimento capaz de classificar avaliações de usuários como **positivas** ou **negativas** utilizando técnicas de Processamento de Linguagem Natural (NLP) e algoritmos de Machine Learning.

### Objetivos Principais

- **Classificação Automática**: Implementar modelos de Machine Learning para identificar automaticamente o sentimento expresso em textos de avaliações
- **Processamento de Linguagem Natural**: Aplicar técnicas de NLP para preparar e transformar dados textuais em features utilizáveis por algoritmos de ML
- **Comparação de Modelos**: Avaliar e comparar o desempenho de diferentes algoritmos probabilísticos (Naive Bayes) na tarefa de classificação de sentimento
- **Deploy de Modelo**: Preparar o melhor modelo para uso em produção, permitindo classificação em tempo real de novas avaliações

### Aplicações Práticas

- Análise de feedback de clientes em plataformas de e-commerce
- Monitoramento de reputação de marca em redes sociais
- Avaliação de satisfação do cliente em serviços
- Triagem automática de reclamações e elogios
- Suporte à tomada de decisão baseada em sentimento do cliente

---

## 🛠️ Tecnologias Utilizadas

### Linguagem de Programação
- **Python 3.x** - Linguagem principal do projeto

### Bibliotecas de Data Science e Machine Learning

#### Manipulação e Análise de Dados
- **NumPy** - Operações numéricas e manipulação de arrays
- **Pandas** - Análise e manipulação de dados estruturados

#### Processamento de Linguagem Natural (NLP)
- **NLTK (Natural Language Toolkit)** - Suite completa para processamento de texto
  - `stopwords` - Remoção de palavras irrelevantes
  - `word_tokenize` - Tokenização de textos
  - `SnowballStemmer` - Redução de palavras à raiz (stemming)

#### Machine Learning
- **Scikit-learn** - Framework principal de Machine Learning
  - `CountVectorizer` - Transformação de texto em vetores (Bag of Words)
  - `train_test_split` - Divisão de dados em treino e teste
  - `GaussianNB` - Modelo Naive Bayes Gaussiano
  - `MultinomialNB` - Modelo Naive Bayes Multinomial
  - `BernoulliNB` - Modelo Naive Bayes de Bernoulli
  - `accuracy_score` - Métrica de avaliação de acurácia
  - `roc_auc_score` - Métrica ROC-AUC para avaliação

#### Outras Ferramentas
- **Pickle** - Serialização e persistência de modelos
- **Re (Regex)** - Manipulação e limpeza de texto com expressões regulares
- **Watermark** - Versionamento e documentação do ambiente

---

## 🚀 Como Executar

```bash
# Clone o repositório (se aplicável)
git clone https://github.com/davioliveiraes/data_science_projects.git
cd data_science_projects/sentiment_analysis_template

# Crie um ambiente conda com Python 3.13
conda create --name sentiment_analysis_template python=3.13
conda activate sentiment_analysis_template

# Instale as bibliotecas necessárias
pip3 install -r requirements.txt

# Baixe os recursos do NLTK (execute no Python)
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

1. Certifique-se de que o arquivo `dataset.csv` está no mesmo diretório do notebook
2. O dataset deve conter avaliações de usuários com suas respectivas classificações de sentimento
3. Abra o arquivo sentiment_analysis_template.ipynb
4. Execute as células sequencialmente (Shift + Enter)

## 📚 Conceitos Aprendidos

### Processamento de Linguagem Natural (NLP)

#### 1. **Tokenização**
Processo de dividir textos em unidades menores (tokens/palavras) para análise individual. Facilita o processamento computacional de linguagem natural.

```python
# Exemplo: "I love this product" → ["I", "love", "this", "product"]
```

#### 2. **Remoção de Stopwords**
Eliminação de palavras muito comuns que não agregam significado semântico relevante (the, is, at, in, etc.). Reduz dimensionalidade e ruído nos dados.

#### 3. **Stemming**
Técnica para reduzir palavras à sua forma raiz, removendo prefixos e sufixos. Normaliza diferentes formas da mesma palavra.

```python
# Exemplo: "running", "runs", "ran" → "run"
```

#### 4. **Bag of Words (BoW)**
Representação vetorial de texto que conta a frequência de cada palavra no documento, ignorando ordem e gramática. Implementado via `CountVectorizer`.

### Algoritmos de Machine Learning - Família Naive Bayes

#### 1. **Gaussian Naive Bayes (GaussianNB)**
- Assume distribuição **normal (gaussiana)** dos dados
- Ideal para features **contínuas**
- Aplicado quando os valores seguem distribuição em curva de sino
- Melhor para dados numéricos normalmente distribuídos

#### 2. **Multinomial Naive Bayes (MultinomialNB)**
- Projetado para dados de **contagem/frequência**
- **Mais adequado para classificação de texto**
- Trabalha com frequências de palavras em documentos
- Assume distribuição multinomial das features
- **Recomendado para sentiment analysis com Bag of Words**

#### 3. **Bernoulli Naive Bayes (BernoulliNB)**
- Otimizado para features **binárias (0/1)**
- Considera apenas presença/ausência de palavras
- Usa distribuição de Bernoulli
- Útil quando apenas a ocorrência importa, não a frequência

### Teorema de Bayes

Todos os modelos Naive Bayes são baseados no **Teorema de Bayes**, que calcula a probabilidade de uma classe dado um conjunto de features:

```
P(Classe|Features) = P(Features|Classe) × P(Classe) / P(Features)
```

A suposição "ingênua" (naive) é que todas as features são **independentes** entre si.

### Pipeline de Ciência de Dados

#### Etapas Fundamentais Aplicadas

1. **Business Understanding** - Alinhamento com objetivos de negócio
2. **Data Understanding** - EDA e análise estatística
3. **Data Preparation** - Limpeza, transformação e feature engineering
4. **Modeling** - Treinamento de múltiplos algoritmos
5. **Evaluation** - Comparação usando métricas (acurácia, ROC-AUC)
6. **Deployment** - Preparação do modelo final para produção
7. **Communication** - Storytelling e visualização de insights

### Métricas de Avaliação

- **Acurácia (Accuracy)** - Proporção de predições corretas
- **ROC-AUC** - Área sob a curva ROC, mede capacidade de discriminação do modelo

### Boas Práticas em Data Science

- **Divisão treino-teste** - Evita overfitting e valida generalização
- **Persistência de modelos** - Salvamento com pickle para reutilização
- **Versionamento** - Documentação de versões de bibliotecas (watermark)
- **Documentação completa** - Cada etapa devidamente explicada
- **Reprodutibilidade** - Código organizado e reutilizável

---

## 📖 Referências

### Documentação Oficial

- **NLTK Documentation** - [https://www.nltk.org/](https://www.nltk.org/)
- **Scikit-learn User Guide** - [https://scikit-learn.org/stable/user_guide.html](https://scikit-learn.org/stable/user_guide.html)
- **Pandas Documentation** - [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
- **NumPy Documentation** - [https://numpy.org/doc/](https://numpy.org/doc/)

### Papers e Artigos Acadêmicos

- Jurafsky, D., & Martin, J. H. (2023). **Speech and Language Processing** (3rd ed.). Stanford University.
- Manning, C. D., Raghavan, P., & Schütze, H. (2008). **Introduction to Information Retrieval**. Cambridge University Press.
- Russell, S., & Norvig, P. (2020). **Artificial Intelligence: A Modern Approach** (4th ed.). Pearson.

### Tutoriais e Cursos

- **Scikit-learn Naive Bayes Tutorial** - [https://scikit-learn.org/stable/modules/naive_bayes.html](https://scikit-learn.org/stable/modules/naive_bayes.html)
- **NLTK Book** - [https://www.nltk.org/book/](https://www.nltk.org/book/)
- **Sentiment Analysis with Python** - Analytics Vidhya
- **Text Classification Tutorial** - Machine Learning Mastery

### Blogs e Recursos Complementares

- **Towards Data Science** - Artigos sobre NLP e Machine Learning
- **Analytics Vidhya** - Tutoriais práticos de Data Science
- **KDnuggets** - Recursos e novidades em ML/AI
- **Papers with Code** - Estado da arte em NLP e classificação de texto

### Datasets Populares para Sentiment Analysis

- **IMDB Movie Reviews** - 50k reviews de filmes
- **Amazon Product Reviews** - Reviews de produtos
- **Twitter Sentiment Analysis** - Sentimentos em tweets
- **Yelp Reviews** - Avaliações de restaurantes e serviços

---

**Desenvolvido como template educacional para projetos de Data Science e Machine Learning**