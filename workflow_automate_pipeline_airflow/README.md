# Pipeline ETL Automatizado com Apache Airflow

Pipeline de dados automatizado para coleta, transformação e armazenamento de dados meteorológicos de cidades brasileiras utilizando Apache Airflow e Docker.

![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.8.1-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

---

## Índice

- [Finalidade](#-finalidade)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Executar](#-como-executar)
- [Conceitos Aprendidos](#-conceitos-aprendidos)
- [Referências](#-referências)

---

## Finalidade

Este projeto implementa um **pipeline ETL (Extract, Transform, Load)** automatizado que coleta dados meteorológicos em tempo real de diversas cidades brasileiras através da API OpenWeatherMap, processa essas informações e as armazena em um banco de dados SQLite para análises posteriores.

### Objetivos Principais

- **Automatizar** a coleta de dados meteorológicos de múltiplas cidades brasileiras
- **Orquestrar** tarefas de ETL utilizando Apache Airflow como ferramenta de workflow
- **Transformar** dados brutos da API (temperatura em Kelvin) para formato utilizável (Celsius)
- **Armazenar** dados processados de forma estruturada para análises futuras
- **Containerizar** toda a aplicação com Docker para facilitar deploy e reprodutibilidade

### Aplicações Práticas

| Aplicação | Descrição |
|-----------|-----------|
| **Análise Climática** | Monitoramento de tendências de temperatura e condições climáticas ao longo do tempo |
| **Business Intelligence** | Base de dados para dashboards e relatórios meteorológicos |
| **Machine Learning** | Dataset para modelos preditivos de previsão do tempo |
| **Alertas Automatizados** | Gatilho para notificações baseadas em condições climáticas específicas |
| **Planejamento Logístico** | Suporte à tomada de decisão em operações sensíveis ao clima |

---

## Tecnologias Utilizadas

### Orquestração e Pipeline

| Tecnologia | Versão | Finalidade |
|------------|--------|------------|
| **Apache Airflow** | 2.8.1 | Orquestração e agendamento de workflows |
| **Python** | 3.11 | Linguagem de programação principal |

### Infraestrutura

| Tecnologia | Versão | Finalidade |
|------------|--------|------------|
| **Docker** | Latest | Containerização da aplicação |
| **Docker Compose** | Latest | Orquestração de múltiplos containers |
| **PostgreSQL** | 13 | Banco de dados do Airflow (metadados) |

### Armazenamento e APIs

| Tecnologia | Finalidade |
|------------|------------|
| **SQLite** | Armazenamento dos dados meteorológicos coletados |
| **OpenWeatherMap API** | Fonte de dados meteorológicos em tempo real |

### Bibliotecas Python

| Biblioteca | Finalidade |
|------------|------------|
| `requests` | Requisições HTTP para a API |
| `sqlite3` | Conexão e operações com banco SQLite |
| `datetime` | Manipulação de datas e timestamps |

---

## Como Executar

### Pré-requisitos

- [Docker](https://www.docker.com/products/docker-desktop) instalado
- [Docker Compose](https://docs.docker.com/compose/install/) instalado
- Conta no [OpenWeatherMap](https://openweathermap.org/) (gratuita)
- Mínimo de 4GB de RAM disponível para o Docker

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/davioliveiraes/data_science_projects.git
cd data_science_projects/workflow_automate_pipeline_airflow
```

### Passo 2: Obtenha a API Key

1. Acesse [OpenWeatherMap](https://openweathermap.org/api)
2. Crie uma conta gratuita
3. Vá em **My API Keys** e copie sua chave
4. Aguarde ~10 minutos para a chave ser ativada

### Passo 3: Configure as Variáveis de Ambiente

```bash
# Crie o arquivo .env
cat > .env << EOF
AIRFLOW_UID=$(id -u)
_AIRFLOW_WWW_USER_USERNAME=airflow
_AIRFLOW_WWW_USER_PASSWORD=airflow
API_KEY=sua_api_key_aqui
EOF
```

### Passo 4: Inicialize o Airflow

```bash
# Inicializa o banco de dados e cria o usuário admin
docker compose up airflow-init
```

### Passo 5: Inicie os Serviços

```bash
# Inicia todos os containers em background
docker compose up -d
```

### Passo 6: Acesse o Airflow

1. Abra o navegador: [http://localhost:8080](http://localhost:8080)
2. Faça login:
   - **Usuário:** `airflow`
   - **Senha:** `airflow`

### Passo 7: Execute a DAG

1. Localize a DAG `pipeline_etl_clima`
2. Ative o toggle (OFF → ON)
3. Clique em ▶️ para executar manualmente ou aguarde o agendamento

### Comandos Úteis

```bash
# Ver status dos containers
docker compose ps

# Ver logs em tempo real
docker compose logs -f

# Parar os serviços
docker compose down

# Parar e remover volumes (apaga dados)
docker compose down -v

# Reiniciar serviços
docker compose restart

# Acessar o banco SQLite
docker compose exec airflow-scheduler bash
sqlite3 /opt/airflow/dags/previsao_tempo.db
```

### Consultas SQL Úteis

```sql
-- Ver todos os registros
SELECT * FROM previsao_tempo;

-- Contar registros por cidade
SELECT cidade, COUNT(*) as total 
FROM previsao_tempo 
GROUP BY cidade;

-- Média de temperatura por cidade
SELECT cidade, ROUND(AVG(temperatura_celsius), 2) as temp_media 
FROM previsao_tempo 
GROUP BY cidade 
ORDER BY temp_media DESC;

-- Últimas coletas
SELECT cidade, temperatura_celsius, data_coleta 
FROM previsao_tempo 
ORDER BY created_at DESC 
LIMIT 10;
```

---

## Conceitos Aprendidos

### Apache Airflow

| Conceito | Descrição |
|----------|-----------|
| **DAG** | Directed Acyclic Graph - Grafo direcionado acíclico que define o fluxo de tarefas |
| **Task** | Unidade individual de trabalho dentro de uma DAG |
| **Operator** | Define o tipo de tarefa a ser executada (PythonOperator, BashOperator, etc.) |
| **XCom** | Mecanismo de comunicação entre tasks para troca de dados |
| **Schedule Interval** | Expressão cron que define a frequência de execução |
| **Catchup** | Controle de execuções retroativas de DAGs |

### ETL (Extract, Transform, Load)

| Etapa | Descrição | Implementação |
|-------|-----------|---------------|
| **Extract** | Coleta dados de fontes externas | Requisições à API OpenWeatherMap |
| **Transform** | Processa e limpa os dados | Conversão Kelvin → Celsius, formatação |
| **Load** | Armazena dados processados | Inserção no banco SQLite |

### Docker

| Conceito | Descrição |
|----------|-----------|
| **Container** | Ambiente isolado para execução de aplicações |
| **Image** | Template imutável para criação de containers |
| **Volume** | Persistência de dados entre execuções |
| **Docker Compose** | Orquestração de múltiplos containers |
| **Network** | Comunicação entre containers |

### Cron Expressions

```
┌───────────── minuto (0 - 59)
│ ┌───────────── hora (0 - 23)
│ │ ┌───────────── dia do mês (1 - 31)
│ │ │ ┌───────────── mês (1 - 12)
│ │ │ │ ┌───────────── dia da semana (0 - 6)
│ │ │ │ │
* * * * *
```

| Expressão | Significado |
|-----------|-------------|
| `*/10 * * * *` | A cada 10 minutos |
| `0 * * * *` | A cada hora |
| `0 6 * * *` | Todo dia às 6h |
| `0 0 * * 0` | Todo domingo à meia-noite |

---

## Referências

### Documentação Oficial

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Airflow with Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

### Tutoriais e Guias

- [Airflow Tutorial - Official](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html)
- [ETL Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)


---

## Estrutura do Projeto

```
workflow_automate_pipeline_airflow/
├── dags/
│   └── pipeline_etl_clima.py    # Script da DAG (pipeline ETL)
├── config/                       # Configurações do Airflow
├── logs/                         # Logs de execução
├── plugins/                      # Plugins customizados
├── docker-compose.yaml           # Configuração dos containers
├── .env                          # Variáveis de ambiente
└── README.md                     # Documentação do projeto
```

---

## Arquitetura do Pipeline

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  OpenWeatherMap │────▶│    Airflow      │────▶│     SQLite      │
│      API        │     │   (ETL Tasks)   │     │    Database     │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        │                       │                       │
   [EXTRACT]              [TRANSFORM]              [LOAD]
   Coleta dados           Converte temp           Armazena
   de 10 cidades          K → °C                  registros
```

---

<p align="center">
  Desenvolvido por Davi Oliveira como prática de estudo de Ciência de Dados.
</p>