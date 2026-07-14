# Databricks notebook source
# ============================================================
# Retail Intelligence Brasil
# Notebook.......: 00_project_setup
# Camada.........: Configuração
# Objetivo.......: Configuração global do projeto
# Autor..........: Cristhina Freire
# ============================================================

# ============================================================
# CONFIGURAÇÕES
# ============================================================

PROJECT_NAME = "Retail Intelligence Brasil"
PROJECT_VERSION = "1.0.0"

CATALOG = "retail_intelligence"

SCHEMA_BRONZE = "bronze"
SCHEMA_SILVER = "silver"
SCHEMA_GOLD = "gold"
SCHEMA_METADATA = "metadata"
SCHEMA_SANDBOX = "sandbox"

# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def bronze_table(table_name: str) -> str:
    return f"{CATALOG}.{SCHEMA_BRONZE}.{table_name}"


def silver_table(table_name: str) -> str:
    return f"{CATALOG}.{SCHEMA_SILVER}.{table_name}"


def gold_table(table_name: str) -> str:
    return f"{CATALOG}.{SCHEMA_GOLD}.{table_name}"


def metadata_table(table_name: str) -> str:
    return f"{CATALOG}.{SCHEMA_METADATA}.{table_name}"


# ============================================================
# VALIDAÇÃO DO AMBIENTE
# ============================================================

spark.sql(f"USE CATALOG {CATALOG}")

print("=" * 60)
print(PROJECT_NAME)
print("=" * 60)
print(f"Versão........: {PROJECT_VERSION}")
print(f"Catálogo......: {CATALOG}")
print(f"Bronze........: {SCHEMA_BRONZE}")
print(f"Silver........: {SCHEMA_SILVER}")
print(f"Gold..........: {SCHEMA_GOLD}")
print(f"Metadata......: {SCHEMA_METADATA}")
print(f"Sandbox.......: {SCHEMA_SANDBOX}")
print("=" * 60)

print("\nExemplo de tabelas:")

print(bronze_table("ibge_estados_raw"))
print(silver_table("dim_estado"))
print(gold_table("indicador_expansao"))