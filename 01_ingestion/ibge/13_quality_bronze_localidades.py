# Databricks notebook source
# ============================================================
# Retail Intelligence Brasil
# Notebook.......: 13_quality_bronze_localidades
# Camada.........: Quality
# Fonte..........: IBGE - Localidades
# Objetivo.......: Validar tabelas Bronze do domínio Localidades
# Autor..........: Cristhina Freire
# ============================================================

from pyspark.sql.functions import col

CATALOG = "retail_intelligence"
SCHEMA = "bronze"

TABLES = [
    "ibge_regioes_raw",
    "ibge_estados_raw",
    "ibge_mesorregioes_raw",
    "ibge_microrregioes_raw",
    "ibge_regioes_intermediarias_raw",
    "ibge_regioes_imediatas_raw",
    "ibge_municipios_raw",
    "ibge_distritos_raw",
    "ibge_subdistritos_raw",
    "ibge_regioes_metropolitanas_raw",
    "ibge_aglomeracoes_urbanas_raw"
]