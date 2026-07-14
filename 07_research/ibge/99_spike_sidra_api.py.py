# Databricks notebook source
import requests

BASE_URL = "https://apisidra.ibge.gov.br"

print("Conexão configurada.")

# COMMAND ----------

url = f"{BASE_URL}/values/t/{TABLE}"

print(url)

response = requests.get(url)

print(response.status_code)
print(response.text[:500])

# COMMAND ----------

url = f"{BASE_URL}/values/t/{TABLE}/n6"

print(url)

response = requests.get(url)

print(response.status_code)
print(response.text[:1000])

# COMMAND ----------

url = BASE_URL

response = requests.get(url)

print(response.status_code)
print(response.text[:1000])

# COMMAND ----------

url = f"{BASE_URL}/values"

response = requests.get(url)

print(response.status_code)
print(response.text[:1500])

# COMMAND ----------

url = f"{BASE_URL}/values/"

response = requests.get(url)

print(response.status_code)
print(response.text[:1500])

# COMMAND ----------

url = (
    f"{BASE_URL}/values/"
    f"t/{TABLE}/"
    f"n6/all/"
    f"v/93/"
    f"p/2022"
)

print(url)

response = requests.get(url)

print(response.status_code)

dados = response.json()

print(type(dados))
print(len(dados))

print(dados[:3])