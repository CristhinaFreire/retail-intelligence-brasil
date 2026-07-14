# Databricks notebook source
# ============================================================
# Retail Intelligence Brasil
# Notebook.......: 05_bronze_regioes_intermediarias
# Camada.........: Bronze
# Fonte..........: IBGE - API Localidades
# Objetivo.......: Persistir Regiões Geográficas Intermediárias
# Autor..........: Cristhina Freire
# ============================================================

# ============================================================
# 1. IMPORTS
# ============================================================

import requests
import json
from datetime import datetime

# ============================================================
# 2. CONFIGURAÇÃO
# ============================================================

CATALOG = "retail_intelligence"
SCHEMA = "bronze"

TABLE_NAME = "ibge_regioes_intermediarias_raw"

FULL_TABLE_NAME = f"{CATALOG}.{SCHEMA}.{TABLE_NAME}"

URL = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes-intermediarias"

TIMEOUT = 60

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y%m%d_%H%M%S")

VOLUME_PATH = (
    f"/Volumes/{CATALOG}/{SCHEMA}/landing/"
    f"ibge/regioes_intermediarias/{CURRENT_DATE}"
)

FILE_NAME = f"regioes_intermediarias_{CURRENT_TIME}.json"

FILE_PATH = f"{VOLUME_PATH}/{FILE_NAME}"

print("=" * 60)
print("BRONZE - IBGE REGIÕES INTERMEDIÁRIAS")
print("=" * 60)

# ============================================================
# 3. EXTRAÇÃO
# ============================================================

response = requests.get(URL, timeout=TIMEOUT)
response.raise_for_status()

landing_data = response.json()

print(f"Registros encontrados: {len(landing_data)}")

# ============================================================
# 4. PERSISTÊNCIA DO JSON ORIGINAL
# ============================================================

dbutils.fs.mkdirs(VOLUME_PATH)

dbutils.fs.put(
    FILE_PATH,
    json.dumps(landing_data, ensure_ascii=False, indent=2),
    overwrite=True
)

print(f"JSON salvo em:\n{FILE_PATH}")

# ============================================================
# 5. LEITURA DO JSON
# ============================================================

landing_df = (
    spark.read
         .option("multiline", "true")
         .json(FILE_PATH)
)

# ============================================================
# 6. BRONZE
# ============================================================

(
    landing_df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(FULL_TABLE_NAME)
)

# ============================================================
# 7. INSPEÇÃO
# ============================================================

bronze_df = spark.table(FULL_TABLE_NAME)

print(f"Total: {bronze_df.count()}")

bronze_df.printSchema()

display(bronze_df)

# ============================================================
# 8. ENCERRAMENTO
# ============================================================

print("=" * 60)
print("Pipeline finalizado com sucesso.")
print("=" * 60)