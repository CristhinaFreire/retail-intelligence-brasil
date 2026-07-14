# Arquitetura

## Visão Geral

A plataforma **Retail Intelligence Brasil** foi desenvolvida utilizando arquitetura **Lakehouse**, adotando o padrão **Medallion** para organizar o ciclo de vida dos dados.

O objetivo é centralizar dados públicos brasileiros, padronizar sua ingestão e disponibilizar informações confiáveis para aplicações de Business Intelligence, Analytics, Ciência de Dados e Inteligência Territorial.

A plataforma utiliza **Databricks**, **Apache Spark**, **Delta Lake**, **Unity Catalog** e **Databricks Volumes** como base para armazenamento, processamento e governança dos dados.

---

# Arquitetura Geral

```text
                    Fontes Públicas

         IBGE Localidades • IBGE SIDRA
 Receita Federal • CAGED • RAIS • Banco Central
 OpenStreetMap • DATASUS • MEC • ANP
                        │
                        ▼
               Landing (Volumes)
             Arquivos JSON brutos
                        │
                        ▼
             Bronze (Delta Lake)
          Dados brutos estruturados
                        │
                        ▼
           Silver (Curated Layer)
      Dados limpos e padronizados
                        │
                        ▼
           Gold (Business Layer)
      Data Marts e Produtos Analíticos
                        │
                        ▼
 Business Intelligence • Analytics • Ciência de Dados
```

---

# Fluxo de Ingestão

Todas as fontes públicas seguem um processo padronizado composto por duas etapas.

## 1. Extração

Os dados são consumidos diretamente da fonte oficial e armazenados na camada Landing em formato bruto (JSON).

## 2. Persistência

Os arquivos da Landing são lidos pelo Apache Spark e persistidos em tabelas Delta na camada Bronze, preservando a estrutura original da fonte.

Esse padrão garante:

- reprodutibilidade;
- rastreabilidade;
- desacoplamento entre extração e processamento;
- facilidade de reprocessamento.

---

# Landing

A Landing é responsável por armazenar os arquivos exatamente como foram disponibilizados pelas fontes oficiais.

## Características

- Arquivos JSON originais
- Organização por fonte e data de carga
- Sem transformações
- Base para reprocessamentos
- Auditoria das cargas

### Estrutura

```text
/Volumes/retail_intelligence/
└── bronze/
    └── landing/
        └── ibge/
            ├── localidades/
            │   ├── estados/
            │   ├── municipios/
            │   ├── regioes/
            │   ├── regioes_intermediarias/
            │   └── regioes_imediatas/
            │
            └── sidra/
                └── demografia/
                    ├── populacao/
                    ├── indicadores_demograficos/
                    └── populacao_sexo_idade/
```

---

# Bronze

A Bronze representa a primeira camada estruturada do Lakehouse.

Nessa etapa os arquivos da Landing são convertidos para tabelas Delta preservando integralmente os dados de origem.

## Características

- Dados RAW
- Sem regras de negócio
- Estrutura idêntica à origem
- Persistência em Delta Lake
- Base para construção da Silver

## Tabelas implementadas

### API IBGE Localidades

- ibge_estados_raw
- ibge_regioes_raw
- ibge_municipios_raw
- ibge_regioes_intermediarias_raw
- ibge_regioes_imediatas_raw

### API SIDRA

- ibge_sidra_populacao_raw
- ibge_sidra_indicadores_demograficos_raw
- ibge_sidra_populacao_sexo_idade_raw

---

# Silver

A camada Silver será responsável pela padronização e integração dos dados provenientes da Bronze.

Principais responsabilidades:

- Conversão de tipos
- Padronização de nomenclaturas
- Limpeza dos dados
- Deduplicação
- Integração entre APIs
- Criação de dimensões
- Criação das tabelas fato
- Aplicação de regras de negócio

---

# Gold

A Gold disponibilizará os produtos analíticos consumidos pelas aplicações de negócio.

Serão disponibilizados:

- Data Marts
- Indicadores
- Métricas
- Views Analíticas
- Modelos dimensionais
- Produtos para Business Intelligence

---

# Organização do Unity Catalog

```text
retail_intelligence

├── bronze
│   ├── Tables
│   └── Volumes
│       └── landing
│
├── silver
│
├── gold
│
├── metadata
│
└── sandbox
```

---

# Tecnologias

- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog
- Databricks Volumes
- Python
- SQL
- REST APIs
- Git
- GitHub

---

# Princípios Arquiteturais

A arquitetura foi construída seguindo os seguintes princípios:

- Fonte única da verdade (Single Source of Truth)
- Arquitetura Medallion
- Reprodutibilidade
- Escalabilidade
- Governança de dados
- Versionamento das cargas
- Baixo acoplamento entre etapas
- Alta rastreabilidade
- Padronização da ingestão
- Preservação dos dados RAW na Bronze
- Separação entre ingestão, transformação e consumo