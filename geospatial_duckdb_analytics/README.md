# 🗺️ Geospatial DuckDB Analytics

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/DuckDB-1.4.3-yellow?logo=duckdb&logoColor=white" alt="DuckDB">
  <img src="https://img.shields.io/badge/GeoPandas-1.1.2-green" alt="GeoPandas">
</p>

<p align="center">
  <strong>Análise Geoespacial de Edifícios com Python e DuckDB</strong><br>
  Data Warehousing Analytics para processamento de dados geoespaciais em larga escala
</p>

---

## 📋 Índice

- [Finalidade](#-finalidade)
- [Objetivos Principais](#-objetivos-principais)
- [Aplicações Práticas](#-aplicações-práticas)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Executar](#-como-executar)
- [Conceitos Aprendidos](#-conceitos-aprendidos)
- [Resultados Esperados](#-resultados-esperados)
- [Referências](#-referências)

---

## 🎯 Finalidade

Este projeto realiza **análise geoespacial de dados de edifícios** utilizando o dataset **Google-Microsoft Open Buildings**, que contém informações de mais de **2,5 bilhões de edifícios** mapeados por inteligência artificial em todo o mundo.

O projeto demonstra como processar grandes volumes de dados geoespaciais de forma eficiente, utilizando **DuckDB** como engine analítico e técnicas de otimização como:

- **Filtragem espacial por bounding box** durante a ingestão de dados
- **Banco de dados persistente** para evitar reprocessamento
- **Operações espaciais SQL** para análises geográficas

### Áreas de Análise

| País/Região | Edifícios | Descrição |
|-------------|-----------|-----------|
| 🇺🇾 **Uruguai** | ~3,1 milhões | Fluxo completo de análise com país de menor volume |
| 🇧🇷 **Ceará, Brasil** | ~6,4 milhões | Análise focada em estado brasileiro com filtragem espacial |
| 🏙️ **Montevidéu** | ~585 mil | Análise de área metropolitana (clipping) |
| 🏙️ **Fortaleza** | ~1 milhão | Análise de área metropolitana (clipping) |

---

## 🏆 Objetivos Principais

### 1. Processamento Eficiente de Big Data Geoespacial
- Carregar e processar milhões de registros geoespaciais do formato GeoParquet
- Aplicar filtros espaciais por bounding box para reduzir volume de dados
- Utilizar banco de dados persistente (DuckDB) para cache e reuso

### 2. Análise Estatística de Edifícios
- Quantificar edifícios por fonte de dados (Google vs Microsoft)
- Calcular estatísticas descritivas: área, confiança, distribuição
- Analisar densidade de construções por região (partições S2)
- Categorizar edifícios por faixas de confiança e área

### 3. Operações Geoespaciais Avançadas
- **Clipping**: Recortar geometrias por área de interesse (AOI)
- **Interseção espacial**: Identificar sobreposições entre datasets
- **Análise comparativa**: Encontrar edifícios exclusivos de cada fonte

### 4. Exportação de Resultados
- Gerar arquivos em formato **FlatGeobuf** (.fgb) para visualização em SIG
- Criar datasets filtrados para análises específicas

---

## 💼 Aplicações Práticas

| Área | Aplicação | Exemplo |
|------|-----------|---------|
| **Planejamento Urbano** | Mapeamento de crescimento urbano | Identificar áreas de expansão em Fortaleza |
| **Gestão de Desastres** | Estimativa de edificações em risco | Contar edifícios em áreas de inundação |
| **Censo e Estatística** | Estimativa populacional | Correlacionar densidade de construções com população |
| **Energia e Infraestrutura** | Planejamento de redes | Dimensionar cobertura de serviços por região |
| **Seguros** | Avaliação de risco | Precificação baseada em densidade urbana |
| **Logística** | Otimização de entregas | Planejamento de rotas por concentração de edificações |
| **Mercado Imobiliário** | Análise de mercado | Identificar regiões com potencial de desenvolvimento |
| **Pesquisa Acadêmica** | Estudos urbanos | Comparar padrões de urbanização entre regiões |

---

## 🛠️ Tecnologias Utilizadas

### Linguagem e Ambiente

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| Python | 3.13+ | Linguagem principal |
| Jupyter Notebook | 7.0+ | Ambiente de desenvolvimento interativo |
| Conda | - | Gerenciamento de ambiente virtual |

### Bibliotecas Principais

| Biblioteca | Versão | Função |
|------------|--------|--------|
| **DuckDB** | 1.4.3 | Banco de dados analítico em processo, otimizado para OLAP |
| **GeoPandas** | 1.1.2 | Manipulação de dados geoespaciais em Python |
| **PyArrow** | 14.0+ | Leitura eficiente de arquivos Parquet |
| **Pandas** | 2.3+ | Manipulação de dados tabulares |

### Extensões DuckDB

| Extensão | Função |
|----------|--------|
| **httpfs** | Leitura direta de arquivos em S3/HTTP sem download local |
| **spatial** | Funções geoespaciais (ST_Intersects, ST_Intersection, ST_Read) |

### Fonte de Dados

| Dataset | Descrição |
|---------|-----------|
| **Google-Microsoft Open Buildings** | Dataset combinado com 2.5B+ edifícios globais |
| **Formato** | GeoParquet particionado por país e grade S2 |
| **Armazenamento** | AWS S3 (Source Cooperative) |
| **Acesso** | Público, sem autenticação |

---

## 📁 Estrutura do Projeto

```
geospatial_duckdb_analytics/
├── 📂 data/                                # Dados gerados (não versionado)
│   ├── ceara_bbox.geojson                 # Bounding box do Ceará
│   ├── fortaleza_aoi.geojson              # Área de interesse - Fortaleza
│   ├── montevideo_aoi.geojson             # Área de interesse - 
│
└── 📂 outputs/                             # Arquivos exportados (não │versionado)
│    ├── fortaleza_buildings.fgb            # Edifícios de Fortaleza (~238MB)
│    ├── fortaleza_microsoft_exclusivos.fgb # Edifícios exclusivos Microsoft
│    ├── montevideo_buildings.fgb            # Edíficios de Montevideo
│    └── montevideo_microsoft_exclusivos.fgb # Edifícios exclusivos │Microsoft
├── 🚫 .gitignore                           # Arquivos ignorados pelo Git
├── geospatial_analytics.duckdb        # Banco de dados persistente (~1.7GB)
├── 📓 geospatial_duckdb_analytics.ipynb   # Notebook principal com análises
├── 📖 README.md                            # Documentação do projeto
└── 📋 requirements.txt                     # Dependências Python
```

### Arquivos Ignorados pelo Git

O arquivo `.gitignore` exclui:
- Banco de dados DuckDB (`*.duckdb`) - ~1.7GB
- Arquivos FlatGeobuf (`*.fgb`) - até 238MB cada
- Arquivos GeoJSON gerados (`*.geojson`)
- Ambientes virtuais Python
- Caches e arquivos temporários

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.12 ou superior
- 8GB+ de RAM disponível
- 5GB+ de espaço em disco
- Conexão com internet (para download inicial dos dados)

### Passo 1: Clonar o Repositório

```bash
git clone git clone https://github.com/davioliveiraes/data_science_projects.git
cd data_science_projetos/geospatial_duckdb_analytics
```

### Passo 2: Criar Ambiente Virtual

```bash
# Com conda (recomendado)
conda create -n geospatial_duckdb_analytics python=3.13
conda activate geospatial_duckdb_analytics

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Executar o Notebook

```bash
jupyter notebook geospatial_duckdb_analytics.ipynb
```

### Passo 5: Primeira Execução

Na **primeira execução**, o notebook irá:

1. ⏳ Baixar dados do Uruguai do S3 (~1-2 minutos)
2. ⏳ Baixar dados do Ceará do S3 (~3-5 minutos)
3. 💾 Salvar tudo em banco persistente (`geospatial_analytics.duckdb`)

**Nas próximas execuções**, os dados serão carregados do cache instantaneamente!

### Estrutura de Execução do Notebook

| Seção | Descrição | Tempo Estimado |
|-------|-----------|----------------|
| 1-3 | Configuração e conexão | < 1 min |
| 4-11 | Análise Uruguai + Montevidéu | 2-3 min (primeira vez) |
| 12-19 | Análise Ceará + Fortaleza | 3-5 min (primeira vez) |
| 20 | Resumo e métricas | < 1 min |

---

## 📚 Conceitos Aprendidos

### 1. Data Warehousing Analítico
- **DuckDB como Data Warehouse**: Banco colunar otimizado para consultas analíticas (OLAP)
- **Persistência de dados**: Estratégias de cache para evitar reprocessamento
- **Particionamento S2**: Grades espaciais hierárquicas para otimização de consultas

### 2. Processamento de Dados Geoespaciais
- **Bounding Box**: Filtragem espacial retangular para delimitar áreas de interesse
- **Formatos Geoespaciais**: GeoParquet (entrada), GeoJSON (AOI), FlatGeobuf (saída)
- **Sistemas de Coordenadas**: Trabalho com coordenadas geográficas (WGS84)

### 3. Operações Espaciais com SQL
```sql
-- Verificação de interseção
ST_Intersects(geometry_a, geometry_b)

-- Cálculo de área de sobreposição
ST_Intersection(geometry_a, geometry_b)

-- Leitura de arquivos geoespaciais
ST_Read('arquivo.geojson')
```

### 4. Análise Estatística de Edifícios
- **Métricas de Confiança**: Score do modelo de ML (0 a 1)
- **Análise por Fonte**: Comparação entre datasets Google e Microsoft
- **Densidade Urbana**: Distribuição de edificações por região

### 5. Otimização de Performance
- **Pushdown de filtros**: Filtragem na fonte durante ingestão
- **Banco persistente vs memória**: Trade-offs de cada abordagem
- **Configuração de recursos**: Ajuste de memória e threads

### 6. Exportação e Interoperabilidade
- **FlatGeobuf**: Formato otimizado para streaming de dados geoespaciais
- **Integração com SIG**: Compatibilidade com QGIS, ArcGIS, kepler.gl

---

## 📊 Resultados Esperados

### Volumetria de Dados

| Dataset | Registros | Armazenamento |
|---------|-----------|---------------|
| Uruguai (total) | 3.100.386 | ~500 MB |
| Ceará (total) | 6.430.541 | ~1.2 GB |
| Montevidéu (clipped) | 584.929 | ~120 MB |
| Fortaleza (clipped) | 1.014.323 | ~238 MB |

### Distribuição por Fonte

| Região | Google | Microsoft |
|--------|--------|-----------|
| Uruguai | 97.63% | 2.37% |
| Ceará | ~99% | ~1% |

### Comparativo de Otimização

| Métrica | Brasil Completo | Ceará + Uruguai |
|---------|-----------------|-----------------|
| Registros | ~141 milhões | ~9.5 milhões |
| Armazenamento | ~22 GB | ~1.7 GB |
| Tempo de carga | 20-40 min | 3-5 min |
| RAM necessária | 32+ GB | 8-16 GB |
| **Redução** | - | **~13x menor** |

### Arquivos de Saída

| Arquivo | Tamanho | Descrição |
|---------|---------|-----------|
| `fortaleza_buildings.fgb` | 238.37 MB | Todos edifícios de Fortaleza |
| `montevideo_buildings.fgb` | ~120 MB | Todos edifícios de Montevidéu |
| `*_microsoft_exclusivos.fgb` | ~1 MB | Edifícios detectados apenas pela Microsoft |

---

## 📖 Referências

### Datasets

- [Google-Microsoft Open Buildings](https://source.coop/repositories/vida/google-microsoft-open-buildings) - Source Cooperative
- [Google Open Buildings V3](https://sites.research.google/open-buildings/) - Google Research
- [Microsoft Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) - Microsoft

### Documentação Técnica

- [DuckDB Documentation](https://duckdb.org/docs/)
- [DuckDB Spatial Extension](https://duckdb.org/docs/extensions/spatial.html)
- [GeoParquet Specification](https://geoparquet.org/)
- [S2 Geometry Library](https://s2geometry.io/)
- [FlatGeobuf Format](https://flatgeobuf.org/)

### Ferramentas de Visualização

- [QGIS](https://qgis.org/) - Software GIS open source
- [kepler.gl](https://kepler.gl/) - Visualização geoespacial web
- [Felt](https://felt.com/) - Mapas colaborativos online

### Tutoriais Relacionados

- [Working with GeoParquet](https://guide.cloudnativegeo.org/geoparquet/)
- [DuckDB Geospatial Tutorial](https://duckdb.org/docs/extensions/spatial.html)

---

## 👨‍💻 Autor

**Davi** - Software Engineer

---

**⭐ Se este projeto foi útil, considere dar uma estrela no repositório!**
