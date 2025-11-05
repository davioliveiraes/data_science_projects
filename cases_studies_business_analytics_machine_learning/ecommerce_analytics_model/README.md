# E-commerce Analytics Model - Portal Konoha

Data Warehouse para análise de vendas de e-commerce de eletrônicos e eletrodomésticos, implementado em PostgreSQL com processos ETL em PL/pgSQL.

---

## 📊 O que o modelo analisa

**Processos ETL implementados:**

- **Clientes** - Distribuição geográfica e perfil demográfico (Brasil, EUA)
- **Distribuidores** - Cadeia de suprimentos e cobertura geográfica
- **Produtos** - Catálogo, precificação e categorização
- **Vendas** - Faturamento, quantidade vendida e custo de frete
- **Data** - Dimensão temporal (2022-2025) para análises de sazonalidade

Todos os processos são **Functions PL/pgSQL parametrizáveis** para controle de volume de dados.

---

## 🚀 Quick Start

### 1. Configurar Ambiente
```bash
# Clone o repositório
git clone <seu-repo>
cd ecommerce-analytics-model

# Configure as variáveis
cp .env.example .env

# Suba o container
docker-compose up -d

# Verifique o status
docker-compose ps
```

### 2. Conectar ao Banco

**Via pgAdmin:**
- Host: `localhost`
- Port: `5437`
- Database: `ecommerce_db`
- User: `postgres`
- Password: `mypassword123`

**Via psql:**
```bash
docker-compose exec postgres psql -U postgres -d ecommerce_db
```

### 3. Executar Scripts SQL

Execute nesta ordem:
1. `modelo_fisico.sql`
2. `processos_etl_data.sql`
3. `processos_etl_clientes.sql`
4. `processos_etl_distribuidores.sql`
5. `processos_etl_produtos.sql`
6. `processos_etl_vendas.sql`

---

## 🛠️ Comandos Úteis
```bash
# Gerenciar container
docker-compose down              # Parar
docker-compose restart           # Reiniciar
docker-compose logs -f postgres  # Ver logs

# Backup e restauração
docker-compose exec -T postgres pg_dump -U postgres ecommerce_db > backup.sql
docker-compose exec -T postgres psql -U postgres ecommerce_db < backup.sql
```

---

## 📁 Estrutura do Projeto
```
ecommerce-analytics-model/
├── .env.example                    # Template de configuração
├── docker-compose.yml              # Configuração Docker
├── modelo_fisico.sql               # Estrutura do banco
├── processos_etl_clientes.sql      # ETL de clientes
├── processos_etl_data.sql          # ETL de dimensão temporal
├── processos_etl_distribuidores.sql
├── processos_etl_produtos.sql
└── processos_etl_vendas.sql
```

---

## 📚 Stack Tecnológica

- PostgreSQL 16.1
- Docker & Docker Compose
- PL/pgSQL
- pgAdmin 4

---

## 📝 Pré-requisitos

- Docker Desktop
- Docker Compose
- pgAdmin 4 (opcional)

Para instalar pgAdmin no Linux:
```bash
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list'
sudo apt update && sudo apt install pgadmin4-desktop
```