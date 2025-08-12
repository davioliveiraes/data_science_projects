# PyVectorSpace - Sistema de Recomendações

Sistema de recomendação de filmes baseado em conceitos de **vetores** e **espaço vetorial**, aplicando matemática e estatística para Data Science e Machine Learning.

## 🎯 Finalidade

Construir um sistema de recomendação completo que utiliza:
- Processamento de linguagem natural (NLP)
- Vetorização de texto com CountVectorizer
- Cálculo de similaridade coseno
- Conceitos de álgebra linear aplicados

## 🛠️ Tecnologias

- **Python 3.9+**
- **pandas** - Manipulação de dados
- **numpy** - Computação numérica
- **scikit-learn** - Machine Learning e vetorização
- **nltk** - Processamento de linguagem natural
- **ast** - Processamento de estruturas de dados

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/davioliveiraes/data_science_projects.git
cd data_science_projects/py_vector_space
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
conda create -n py_vector_space python=3.12 -y

# Ativar ambiente
conda activate py_vector_space
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

**Execute o notebook/script:**
```python
# Carregar dados
df_dsa_filmes = pd.read_csv("dados/dataset_filmes.csv")
df_elenco = pd.read_csv("dados/dataset_elenco.csv")

# Usar o sistema de recomendação
sistema_recomendacao('Avengers: Age of Ultron')
# Output: The Avengers, Iron Man 2, Iron Man, Iron Man 3, Thor
```

## 📊 Exemplo de Uso

```python
# Recomendações para diferentes filmes
sistema_recomendacao('Jurassic World')
sistema_recomendacao('The Hobbit: The Battle of the Five Armies')
```

## 📁 Estrutura dos Dados

- `dataset_filmes.csv` - Informações dos filmes (gêneros, sinopse, etc.)
- `dataset_elenco.csv` - Informações do elenco e equipe

## 🔬 Conceitos Aplicados

- **Stemming** com PorterStemmer
- **Vetorização** com CountVectorizer (5000 features)
- **Similaridade Coseno** para calcular distâncias
- **Processamento AST** para parsing de dados JSON

---
*Projeto de Matemática e Estatística aplicada para Data Science, Machine Learning e IA*