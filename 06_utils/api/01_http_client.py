# Databricks notebook source
# ============================================================
# Retail Intelligence Brasil
# Notebook.......: 01_http_client
# Camada.........: Utils
# Objetivo.......: Cliente HTTP reutilizável
# Autor..........: Cristhina Freire
# ============================================================

# ============================================================
# 1. IMPORTS
# ============================================================

import requests

# ============================================================
# 2. FUNÇÕES
# ============================================================

def get_json(
    url: str,
    timeout: int = 60
):
    """
    Consome uma API REST e retorna o JSON da resposta.

    Parameters
    ----------
    url : str
        Endpoint da API.

    timeout : int
        Timeout da requisição.

    Returns
    -------
    list | dict
        JSON retornado pela API.
    """

    print(f"Consumindo API: {url}")

    response = requests.get(
        url=url,
        timeout=timeout
    )

    response.raise_for_status()

    json_data = response.json()

    print("API consumida com sucesso.")

    if isinstance(json_data, list):
        print(f"Quantidade de registros: {len(json_data)}")

    return json_data