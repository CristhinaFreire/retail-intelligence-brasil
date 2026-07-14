# Databricks notebook source
# ============================================================
# Retail Intelligence Brasil
# Notebook.......: 01_download_estados
# Camada.........: Landing
# Fonte..........: IBGE - API Localidades
# Objetivo.......: Consumir a API de Estados do IBGE e salvar
#                  o JSON bruto na Landing
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

URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

TIMEOUT = 30

DATA_CARGA = datetime.now().strftime("%Y-%m-%d")
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

LANDING_PATH = (
    f"/Volumes/retail_intelligence/bronze/landing/ibge/"
    f"estados/{DATA_CARGA}"
)

FILE_NAME = f"estados_{TIMESTAMP}.json"

print("=" * 60)
print("DOWNLOAD - ESTADOS (IBGE)")
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

print("API consumida com sucesso.")
print(f"Total de registros: {len(landing_data)}")

# ============================================================
# 5. SALVAR JSON NA LANDING
# ============================================================

dbutils.fs.mkdirs(LANDING_PATH)

JSON_PATH = f"{LANDING_PATH}/{FILE_NAME}"

dbutils.fs.put(
    JSON_PATH,
    json.dumps(
        landing_data,
        ensure_ascii=False,
        indent=2
    ),
    overwrite=True
)

print(f"\nJSON salvo em:")
print(JSON_PATH)

# ============================================================
# 6. CONVERTER PARA SPARK
# ============================================================

landing_df = spark.createDataFrame(landing_data)

print("\nSchema:")

landing_df.printSchema()

print("\nPrévia dos dados:")

display(landing_df)

# ============================================================
# 7. ENCERRAMENTO
# ============================================================

print("=" * 60)
print("Download concluído com sucesso.")
print("=" * 60)