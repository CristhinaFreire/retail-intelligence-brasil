# Data Lineage

Este documento descreve o fluxo dos dados desde a origem até as camadas analíticas da plataforma Retail Intelligence Brasil.

---

# Visão Geral

A plataforma segue a arquitetura Lakehouse utilizando o padrão Medallion. Cada dado percorre um fluxo padronizado desde sua origem até as camadas analíticas.

```
             Fonte Oficial
                  │
                  ▼
        Landing (Volumes / JSON)
                  │
                  ▼
        Bronze (Delta Lake)
                  │
                  ▼
      Silver (Dados Tratados)
                  │
                  ▼
     Gold (Produtos Analíticos)
                  │
                  ▼
      Dashboards e Analytics
```

---

# Pipeline de Ingestão

Cada entidade segue o mesmo padrão de processamento.

```
01_download_<entidade>
        │
        ▼
Landing (JSON)
        │
        ▼
02_bronze_<entidade>
        │
        ▼
Tabela Delta
```

---

# Lineage da Fonte IBGE

## Estados

```
API IBGE
    │
    ▼
/landing/ibge/estados
    │
    ▼
ibge_estados_raw
```

---

## Municípios

```
API IBGE
    │
    ▼
/landing/ibge/municipios
    │
    ▼
ibge_municipios_raw
```

---

## Regiões

```
API IBGE
    │
    ▼
/landing/ibge/regioes
    │
    ▼
ibge_regioes_raw
```

---

## Regiões Intermediárias

```
API IBGE
    │
    ▼
/landing/ibge/regioes_intermediarias
    │
    ▼
ibge_regioes_intermediarias_raw
```

---

## Regiões Imediatas

```
API IBGE
    │
    ▼
/landing/ibge/regioes_imediatas
    │
    ▼
ibge_regioes_imediatas_raw
```

---

# Próximas Camadas

Atualmente o fluxo está implementado até a camada Bronze.

As próximas etapas contemplam:

```
Bronze
    │
    ▼
Silver
    │
    ▼
Gold
```

A camada Silver será responsável pela padronização, integração e enriquecimento dos dados, enquanto a camada Gold disponibilizará modelos dimensionais, indicadores e produtos analíticos.

---

# Princípios

Todos os pipelines da plataforma seguem os seguintes princípios:

- Separação entre extração e processamento.
- Persistência dos arquivos brutos na Landing.
- Armazenamento estruturado em Delta Lake.
- Rastreabilidade completa entre origem e destino.
- Reprocessamento a partir da Landing quando necessário.
- Padronização da estrutura dos notebooks de ingestão.