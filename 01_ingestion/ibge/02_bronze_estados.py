# Databricks notebook source
# ============================================================
# Retail Intelligence Brasil
# Notebook.......: 02_bronze_estados
# Camada.........: Bronze
# Fonte..........: IBGE - API Localidades
# Objetivo.......: Persistir os estados brasileiros na camada Bronze
# Autor..........: Cristhina Freire
# ============================================================

# ============================================================
# 1. IMPORTS
# ============================================================

import requests

# ============================================================
# 2. CONFIGURAÇÃO
# ============================================================

CATALOG = "retail_intelligence"
SCHEMA = "bronze"

TABLE_NAME = "ibge_estados_raw"

FULL_TABLE_NAME = f"{CATALOG}.{SCHEMA}.{TABLE_NAME}"

URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

TIMEOUT = 30

print("=" * 60)
print("BRONZE - IBGE ESTADOS")
print("=" * 60)

# ============================================================
# 3. EXTRAÇÃO
# ============================================================

print("Consumindo API do IBGE...")

response = requests.get(
    url=URL,
    timeout=TIMEOUT
)

# ============================================================
# 4. VALIDAÇÃO
# ============================================================

if response.status_code != 200:
    raise Exception(
        f"Erro ao consumir API. Status Code: {response.status_code}"
    )

landing_data = response.json()

if len(landing_data) == 0:
    raise Exception("A API retornou uma lista vazia.")

print(f"Registros encontrados: {len(landing_data)}")

# ============================================================
# 5. CONVERSÃO PARA SPARK
# ============================================================

landing_df = spark.createDataFrame(landing_data)

# ============================================================
# 6. PERSISTÊNCIA NA BRONZE
# ============================================================

print(f"Gravando tabela {FULL_TABLE_NAME}...")

(
    landing_df.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable(FULL_TABLE_NAME)
)

print("Tabela gravada com sucesso.")

# ============================================================
# 7. INSPEÇÃO
# ============================================================

bronze_df = spark.table(FULL_TABLE_NAME)

print(f"Total de registros: {bronze_df.count()}")

bronze_df.printSchema()

display(bronze_df)

# ============================================================
# 8. ENCERRAMENTO
# ============================================================

print("=" * 60)
print("Pipeline Bronze finalizado com sucesso.")
print("=" * 60)