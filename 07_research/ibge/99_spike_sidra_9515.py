# Databricks notebook source
# ============================================================
# Retail Intelligence Brasil
# Notebook.......: 99_spike_sidra_9515
# Tipo...........: Spike Técnico
# Fonte..........: IBGE - SIDRA
# Objetivo.......: Validar a API da tabela 9515
# Autor..........: Cristhina Freire
# ============================================================

# ============================================================
# 1. IMPORTS
# ============================================================

import requests
import json

# ============================================================
# 2. CONFIGURAÇÃO
# ============================================================

BASE_URL = "https://apisidra.ibge.gov.br"

SIDRA_TABLE_ID = 9515

TIMEOUT = 60

print("=" * 60)
print("SPIKE - SIDRA - TABELA 9515")
print("=" * 60)

print(f"Tabela SIDRA: {SIDRA_TABLE_ID}")

# COMMAND ----------

# ============================================================
# 3. VALIDAR TABELA
# ============================================================

url = f"{BASE_URL}/values/t/{SIDRA_TABLE_ID}"

print(url)

response = requests.get(
    url,
    timeout=TIMEOUT
)

print("=" * 60)
print("STATUS")
print("=" * 60)

print(response.status_code)

print("=" * 60)
print("RESPOSTA")
print("=" * 60)

print(response.text[:1000])

# COMMAND ----------

# ============================================================
# 4. TESTE NÍVEL TERRITORIAL
# ============================================================

url = (
    f"{BASE_URL}/values/"
    f"t/{SIDRA_TABLE_ID}/"
    f"n6/all"
)

print(url)

response = requests.get(
    url,
    timeout=TIMEOUT
)

print("=" * 60)
print("STATUS")
print("=" * 60)

print(response.status_code)

print("=" * 60)
print("RESPOSTA")
print("=" * 60)

print(response.text[:1000])

# COMMAND ----------

# ============================================================
# 5. DESCOBRIR VARIÁVEL
# ============================================================

url = (
    f"{BASE_URL}/values/"
    f"t/{SIDRA_TABLE_ID}/"
    f"n6/all"
)

response = requests.get(
    url,
    timeout=TIMEOUT
)

print(response.status_code)

print(response.text)

# COMMAND ----------

# ============================================================
# 6. URL VALIDADA
# ============================================================

URL = (
    f"{BASE_URL}/values/"
    f"t/{SIDRA_TABLE_ID}/"
    f"n6/all/"
    f"v/XXXX/"
    f"p/XXXX"
)

print(URL)

# COMMAND ----------

# ============================================================
# 7. RESULTADO
# ============================================================

response = requests.get(
    URL,
    timeout=TIMEOUT
)

print(response.status_code)

dados = response.json()

print(type(dados))

print(f"Total de registros: {len(dados)}")

print("=" * 60)

print("Cabeçalho")

print(dados[0])

print("=" * 60)

print("Primeiro Registro")

print(dados[1])