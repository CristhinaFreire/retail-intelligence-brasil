# Roadmap

Este documento apresenta a evolução planejada da plataforma Retail Intelligence Brasil.

---

# Fase 1 — Fundação da Plataforma

Status: Concluído

- Estrutura do repositório
- Configuração do Databricks
- Configuração do Unity Catalog
- Organização das camadas do Lakehouse
- Criação da documentação técnica
- Definição dos padrões de nomenclatura

---

# Fase 2 — Ingestão de Dados (Bronze)

Status: Concluído

## IBGE

- Estados
- Municípios
- Regiões
- Regiões Intermediárias
- Regiões Imediatas

### Funcionalidades

- Download via API REST
- Persistência dos arquivos JSON na Landing
- Conversão para DataFrames Spark
- Persistência em tabelas Delta
- Padronização dos notebooks
- Validação das cargas

---

# Fase 3 — Camada Silver

Status: Em desenvolvimento

Objetivos:

- Padronização dos dados
- Normalização das estruturas
- Criação de chaves técnicas
- Tratamento de duplicidades
- Integração entre fontes públicas
- Criação das primeiras dimensões

---

# Fase 4 — Novas Fontes

Status: Planejado

Integração com:

- Receita Federal
- CAGED
- RAIS
- Banco Central
- OpenStreetMap
- DATASUS
- MEC
- ANP

---

# Fase 5 — Camada Gold

Status: Planejado

Desenvolvimento de:

- Data Marts
- Indicadores de mercado
- Indicadores socioeconômicos
- Indicadores de expansão
- Modelo dimensional
- Views analíticas

---

# Fase 6 — Analytics

Status: Planejado

- Dashboards em Power BI
- Estudos de expansão comercial
- Análises geoespaciais
- Inteligência territorial
- Casos de uso para varejo