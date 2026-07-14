# Databricks notebook source
base = "/Volumes/retail_intelligence/bronze/landing/ibge"

dbutils.fs.mv(f"{base}/estados", f"{base}/localidades/estados")
dbutils.fs.mv(f"{base}/municipios", f"{base}/localidades/municipios")
dbutils.fs.mv(f"{base}/regioes", f"{base}/localidades/regioes")
dbutils.fs.mv(f"{base}/regioes_intermediarias", f"{base}/localidades/regioes_intermediarias")
dbutils.fs.mv(f"{base}/regioes_imediatas", f"{base}/localidades/regioes_imediatas")
dbutils.fs.mv(f"{base}/mesorregioes", f"{base}/localidades/mesorregioes")
dbutils.fs.mv(f"{base}/microrregioes", f"{base}/localidades/microrregioes")
dbutils.fs.mv(f"{base}/distritos", f"{base}/localidades/distritos")
dbutils.fs.mv(f"{base}/subdistritos", f"{base}/localidades/subdistritos")
dbutils.fs.mv(f"{base}/regioes_metropolitanas", f"{base}/localidades/regioes_metropolitanas")

# COMMAND ----------

dbutils.fs.mkdirs("/Volumes/retail_intelligence/bronze/landing/ibge/localidades")

# COMMAND ----------

base = "/Volumes/retail_intelligence/bronze/landing/ibge"

dbutils.fs.mkdirs(f"{base}/localidades")

pastas = [
    "estados",
    "municipios",
    "regioes",
    "regioes_intermediarias",
    "regioes_imediatas",
    "mesorregioes",
    "microrregioes",
    "distritos",
    "subdistritos",
    "regioes_metropolitanas"
]

for pasta in pastas:
    origem = f"{base}/{pasta}"
    destino = f"{base}/localidades/{pasta}"

    print(f"Movendo {pasta}...")
    dbutils.fs.mv(origem, destino, True)

print("Concluído.")

# COMMAND ----------

print("IBGE")
display(dbutils.fs.ls("/Volumes/retail_intelligence/bronze/landing/ibge"))

# COMMAND ----------

print("LOCALIDADES")
display(dbutils.fs.ls("/Volumes/retail_intelligence/bronze/landing/ibge/localidades"))