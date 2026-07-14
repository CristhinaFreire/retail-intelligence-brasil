# Roadmap

Este documento apresenta a evolução planejada da plataforma Retail Intelligence Brasil.

---

# Fase 1 — Fundação da Plataforma

**Status:** Concluído

## Entregas

- Estrutura do repositório
- Configuração do Databricks
- Configuração do Unity Catalog
- Organização das camadas do Lakehouse
- Definição da arquitetura Medallion
- Criação da documentação técnica
- Definição dos padrões de nomenclatura
- Estrutura inicial dos ADRs

---

# Fase 2 — Ingestão de Dados (Bronze)

**Status:** Concluído

## API IBGE Localidades

### Entidades implementadas

- Estados
- Regiões
- Municípios
- Regiões Intermediárias
- Regiões Imediatas

## API SIDRA

### Tabelas implementadas

- 4709 — População residente, variação absoluta e taxa de crescimento geométrico
- 9515 — Índice de envelhecimento, idade mediana e razão de sexo
- 9514 — População residente por sexo e grupos de idade

### Entregas

- Consumo de APIs REST
- Persistência dos arquivos JSON na Landing
- Conversão para DataFrames Spark
- Persistência em tabelas Delta
- Padronização dos notebooks
- Padronização das estruturas Bronze
- Estratégia de ingestão para tabelas multidimensionais
- Validação das cargas
- Documentação arquitetural utilizando ADRs

---

# Fase 3 — Camada Silver

**Status:** Planejado

## Objetivos

- Padronização dos nomes das colunas
- Conversão de tipos de dados
- Normalização das estruturas
- Criação de chaves substitutas (Surrogate Keys)
- Integração entre Localidades e SIDRA
- Criação das dimensões
- Criação das tabelas fato
- Tratamento de qualidade dos dados

---

# Fase 4 — Novas Fontes

**Status:** Planejado

## Integrações previstas

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

**Status:** Planejado

## Objetivos

- Data Marts
- Modelo dimensional
- Indicadores demográficos
- Indicadores socioeconômicos
- Indicadores econômicos
- Indicadores de expansão do varejo
- Views analíticas

---

# Fase 6 — Analytics

**Status:** Planejado

## Entregas

- Dashboards Power BI
- Estudos de expansão comercial
- Inteligência territorial
- Análises geoespaciais
- Casos de uso para varejo
- Modelos preditivos para expansão de lojas

---

# Próximas Implementações

As próximas tabelas priorizadas para integração via SIDRA são:

- População por grupos de idade (1522)
- População por situação do domicílio
- População por cor ou raça
- Pessoas com deficiência
- População diagnosticada com autismo

Essas integrações ampliarão o conjunto de indicadores demográficos utilizados pela plataforma para análises de potencial de mercado e expansão do varejo.