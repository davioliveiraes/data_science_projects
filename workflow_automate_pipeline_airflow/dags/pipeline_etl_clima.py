import os
import requests
import sqlite3
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

# Configurações
API_KEY = os.getenv("API_KEY", "SUA_API_KEY_AQUI")

URL_BASE = os.getenv("URL_BASE", "https://api.openweathermap.org/data/2.5/weather?")

DB_PATH = os.getenv("DB_PATH", "/opt/airflow/dags/previsao_tempo.db")

CITIES = [
    "Fortaleza", "Morada Nova", "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Curitiba", "Manaus", "Recife", "Brasília"
]

DB_PATH=os.getenv("DB_PATH")

# Argumentos Padrão da DAG
default_args = {
    "owner": "Davi",
    "depends_on_past": False,
    "start_date": datetime(2026, 1, 23),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2)
}

# Criação da DAG
dag = DAG(
    dag_id= "pipeline_etl_clima",
    default_args=default_args,
    description="Pipeline ETL para coleta de dados meteorológicos",
    schedule_interval="*/10 * * * *", # type: ignore
    catchup=False,
    tags=["etl", "clima", "openweathermap", "davi"]
)

# Funções do Pipeline ETL

# Extract - Extração
def extract_data(**kwargs):
    print("=" * 60)
    print("INICIANDO EXTRAÇÃO DE DADOS")
    print("=" * 60)

    extracted_data = []

    for city in CITIES:
        try:
            url = f"{URL_BASE}q={city}, BR&appid={API_KEY}&lang=pt-br"
            print(f"Buscando dados: {city}")
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()
            extracted_data.append(data)

            print(f"Sucesso: {city} - Temp: {data['main']['temp']}K")

        except requests.exceptions.RequestException as e:
            print(f" Erro aoa buscar {city}: {str(e)}")
            continue

    print(f"\n Total de cidades coletadas: {len(extracted_data)}")
    
    kwargs['ti'].xcom_push(key='dados_brutos', value=extracted_data)

    return extracted_data

# Transform - Transformação
def transform_data(**kwargs):
    print("=" * 60)
    print("INICIANDO TRANSFORMAÇÃO DE DADOS")
    print("=" * 60)

    ti = kwargs['ti']
    raw_data = ti.xcom_pull(key='dados_brutos', task_ids='extrair_dados')

    if not raw_data:
        print("Nenhum dado recebido para transformação!")
        return []
    
    transformed_data = []

    for registry in raw_data:
        try:
            processed_data = {
                "cidade": registry['name'],
                "pais": registry['sys']['country'],
                "data_coleta": datetime.utcfromtimestamp(registry['dt']).strftime('%Y-%m-%d %H:%M:%S'),
                "temperatura_celsius": round(registry['main']['temp'] - 273.15, 2),
                "sensacao_termica": round(registry['main']['feels_like'] - 273.15, 2),
                "temp_minima": round(registry['main']['temp_min'] - 273.75, 2),
                "temp_maxima": round(registry['main']['temp_max'] - 273.15, 2),
                "umidade": registry['main']['humidity'],
                "pressao": registry['main']['pressure'],
                "descricao_clima": registry['weather'][0]['description'],
                "velocidade_vento": registry['wind']['speed'],
                "timestamp_processamento": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            transformed_data.append(processed_data)

            print(f"Transformado: {processed_data['cidade']} -> {processed_data['temperatura_celsius']}°C")
        except KeyError as e:
            print(f"Erro ao processar registro: Campo {e} não encontrado")
            continue

    print(f"\n Total de registros transformados: {len(transformed_data)}")

    ti.xcom_push(key='dados_processados', value=transformed_data)

    return transformed_data

# Load - Carregar
def load_data(**kwargs):
    print("=" * 60)
    print("INICIANDO CARREGAMENTO DE DADOS")
    print("=" * 60)

    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(key='dados_processados', task_ids='transformar_dados')

    if not transformed_data:
        print("Nenhum dado recebido para carregamento!")
        return
    
    conn = sqlite3.connect(DB_PATH) # type: ignore
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS previsao_tempo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade TEXT NOT NULL,
            pais TEXT,
            data_coleta TEXT,
            temperatura_celsius REAL,
            sensacao_termica REAL,
            temp_minima REAL,
            temp_maxima REAL,
            umidade INTEGER,
            pressao INTEGER,
            descricao_clima TEXT,
            velocidade_vento REAL,
            timestamp_processamento TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Inserir Dados
    entry_records = 0

    for data in transformed_data:
        try:
            cursor.execute('''
                INSERT INTO previsao_tempo (
                    cidade, pais, data_coleta, temperatura_celsius,
                    sensacao_termica, temp_minima, temp_maxima, umidade,
                    pressao, descricao_clima, velocidade_vento, timestamp_processamento
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                data['cidade'],
                data['pais'],
                data['data_coleta'],
                data['temperatura_celsius'],
                data['sensacao_termica'],
                data['temp_minima'],
                data['temp_maxima'],
                data['umidade'],
                data['pressao'],
                data['descricao_clima'],
                data['velocidade_vento'],
                data['timestamp_processamento']
            ))
            entry_records += 1
            print(f"Inserido: {data['cidade']}")

        except sqlite3.Error as e:
            print(f"Erro ao inserir {data['cidade']}: {str(e)}")
            continue
    
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM previsao_tempo")
    total_records = cursor.fetchone()[0]

    print("\n Carregamento concluído")
    print(f"Registros inseridos nesta execução: {entry_records}")
    print(f"Total de registros no banco: {total_records}")

    conn.close()

# Definição  das Tasks (Tarefas)

# Task 1 - Extração
task_extract = PythonOperator(
    task_id='extrair_dados',
    python_callable=extract_data,
    provide_context=True,
    dag=dag
)

# Task 2 - Transformação
task_transform = PythonOperator(
    task_id='transformar_dados',
    python_callable=transform_data,
    provide_context=True,
    dag=dag
)

# Task 3 - Carregamento
task_load = PythonOperator(
    task_id='carregar_dados',
    python_callable=load_data,
    provide_context=True,
    dag=dag
)

# Definição do Fluxo (DEPENDÊNCIA)

task_extract >> task_transform >> task_load # type: ignore
