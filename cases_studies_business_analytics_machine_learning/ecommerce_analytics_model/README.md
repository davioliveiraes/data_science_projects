# E-commerce Analytics Model

## 📋 Sobre o Estudo de Caso

Este estudo de caso implementa um **Data Warehouse robusto e eficiente** para análise de dados de um portal de e-commerce chamado **Konoha**. O objetivo é extrair métricas de vendas, operação e comportamento de compra dos clientes através de um modelo de dados escalável e flexível.

### Contexto do Negócio

O Konoha é um portal de e-commerce que comercializa produtos eletrônicos e eletrodomésticos. O projeto envolve:

- Análise detalhada das necessidades de negócio
- Definição de entidades-chave (produtos, usuários, pedidos, transações)
- Desenvolvimento de modelos de dados (Conceitual, Dimensional, Lógico e Físico)
- Implementação em sistema de banco de dados PostgreSQL
- Foco em performance, segurança e integridade dos dados.

### 📊 O que o modelo permite analisar:

**Processos ETL implementados:**

- **Clientes** (`etl_clientes`): Gera dados de clientes com nome, endereço, cidade e país. Permite análise de distribuição geográfica e perfil demográfico dos clientes em diferentes regiões (Brasil, EUA).

- **Distribuidores** (`etl_distribuidores`): Cria registros de distribuidores com localização geográfica (Brasil, EUA, Portugal, Espanha). Possibilita análise de cadeia de suprimentos e cobertura geográfica.

- **Produtos** (`etl_produtos`): Gera catálogo de produtos com nome, descrição, preço e categoria. Permite análise de precificação, categorização e composição do portfólio.

- **Vendas** (`etl_vendas`): Cria registros de transações conectando clientes, produtos e distribuidores. Permite análise de faturamento, quantidade vendida, custo de frete e performance de vendas.

- **Data** (`gerar_datas`): Popula dimensão temporal (2022-2025) com dia, mês, ano e dia da semana. Possibilita análises temporais, sazonalidade e tendências ao longo do período.

Todos os processos ETL foram desenvolvidos como **Functions PL/pgSQL** parametrizáveis, permitindo controle sobre o volume de dados gerados para testes e simulações.

---

## 🐳 Configuração do Ambiente

### Pré-requisitos

- Docker Desktop instalado
- Sistema operacional Linux (Ubuntu/Debian)

### 1. Criar o Container PostgreSQL

Execute o comando abaixo no terminal para criar o container Docker:
```bash
docker run --name my_ecommerce_db \
  -p 5432:5432 \
  -e POSTGRES_DB=ecommerce_db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=mypassword123 \
  -v ecommerce_data:/var/lib/postgresql/data \
  -d postgres:16.1
```

**Parâmetros:**
- `--name`: Nome do container
- `-p 5432:5432`: Mapeamento de porta (host:container)
- `-e`: Variáveis de ambiente do PostgreSQL
- `-v`: Volume para persistência de dados
- `-d`: Execução em background
- `postgres:16.1`: Imagem e versão do PostgreSQL

**Verificar se o container está rodando:**
```bash
docker ps
```

**Comandos úteis:**
```bash
# Parar o container
docker stop my_ecommerce_db

# Iniciar o container
docker start my_ecommerce_db

# Ver logs
docker logs my_ecommerce_db

# Fazer backup dos dados
docker exec -t my_ecommerce_db pg_dumpall -c -U postgres > backup_$(date +%Y%m%d).sql
```

---

## 🔧 Instalação do pgAdmin (Linux - Versão Desktop)

### Passo 1: Instalar a chave pública do repositório
```bash
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
```

### Passo 2: Adicionar o repositório
```bash
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list'
```

### Passo 3: Atualizar os pacotes
```bash
sudo apt update
```

### Passo 4: Instalar pgAdmin Desktop
```bash
sudo apt install pgadmin4-desktop
```

---

## 🔐 Configuração do pgAdmin

### Primeiro Acesso

Ao abrir o pgAdmin pela primeira vez, defina uma **Master Password**:
```
Master Password: sua_senha_master
```

### Criar Nova Conexão com o Banco de Dados

1. Clique com botão direito em **Servers** → **Register** → **Server**

2. Na aba **General**:
   - **Name**: `My Ecommerce Database`

3. Na aba **Connection**:
   - **Host name/address**: `localhost`
   - **Port**: `5432`
   - **Maintenance database**: `ecommerce_db`
   - **Username**: `postgres`
   - **Password**: `mypassword123`
   - ☑️ **Save password**

4. Clique em **Save**

---

## 📁 Estrutura do Projeto
```
ecommerce-analytics-model/
│
├── README.md
├── modelo_fisico.sql
├── processos_etl_clientes.sql
├── processos_etl_data.sql
├── processos_etl_distribuidores.sql
├── processos_etl_produtos.sql
└── processos_etl_vendas.sql
```

---

## 🚀 Como Executar

1. **Inicie o container Docker**
2. **Conecte-se ao pgAdmin**
3. **Execute o modelo físico** (`modelo_fisico.sql`) para criar a estrutura do banco
4. **Execute os processos ETL** na seguinte ordem:
   - `processos_etl_data.sql`
   - `processos_etl_clientes.sql`
   - `processos_etl_distribuidores.sql`
   - `processos_etl_produtos.sql`
   - `processos_etl_vendas.sql`

---

## 📚 Tecnologias Utilizadas

- **PostgreSQL 16.1**: Sistema de gerenciamento de banco de dados
- **Docker**: Containerização da aplicação
- **pgAdmin 4**: Interface gráfica para administração do banco
- **SQL**: Linguagem de consulta e manipulação de dados