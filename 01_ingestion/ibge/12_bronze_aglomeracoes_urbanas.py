# Databricks notebook source
# ============================================================
# Retail Intelligence Brasil
# Notebook.......: 12_bronze_aglomeracoes_urbanas
# Camada.........: Bronze
# Fonte..........: IBGE - API Localidades
# Objetivo.......: Persistir aglomerações urbanas do IBGE na Bronze
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

TABLE_NAME = "ibge_aglomeracoes_urbanas_raw"

FULL_TABLE_NAME = f"{CATALOG}.{SCHEMA}.{TABLE_NAME}"

URL = "https://servicodados.ibge.gov.br/api/v1/localidades/aglomeracoes-urbanas"

TIMEOUT = 60

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y%m%d_%H%M%S")

VOLUME_PATH = (
    f"/Volumes/{CATALOG}/{SCHEMA}/landing/"
    f"ibge/localidades/aglomeracoes_urbanas/{CURRENT_DATE}"
)

FILE_NAME = f"aglomeracoes_urbanas_{CURRENT_TIME}.json"

FILE_PATH = f"{VOLUME_PATH}/{FILE_NAME}"

print("=" * 60)
print("BRONZE - IBGE AGLOMERAÇÕES URBANAS")
print("=" * 60)

# ============================================================
# 3. EXTRAÇÃO
# ============================================================

print("Consumindo API...")

response = requests.get(
    URL,
    timeout=TIMEOUT
)

response.raise_for_status()

landing_data = response.json()

print(f"Aglomerações urbanas encontradas: {len(landing_data)}")

# ============================================================
# 4. PERSISTÊNCIA DO JSON ORIGINAL
# ============================================================

dbutils.fs.mkdirs(VOLUME_PATH)

dbutils.fs.put(
    FILE_PATH,
    json.dumps(
        landing_data,
        ensure_ascii=False,
        indent=2
    ),
    overwrite=True
)

print(f"JSON salvo em:\n{FILE_PATH}")

# ============================================================
# 5. LEITURA DO JSON DO VOLUME
# ============================================================

print("Lendo JSON salvo no Volume...")

landing_df = (
    spark.read
         .option("multiline", "true")
         .json(FILE_PATH)
)

print("Leitura concluída.")

# ============================================================
# 6. PERSISTÊNCIA NA BRONZE
# ============================================================

(
    landing_df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(FULL_TABLE_NAME)
)

print("Tabela Bronze criada.")

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
print("Pipeline finalizado com sucesso.")
print("=" * 60)