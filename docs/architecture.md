# Arquitetura

## Visão Geral

A plataforma Retail Intelligence Brasil foi desenvolvida utilizando a arquitetura Lakehouse, adotando o padrão Medallion para organizar o ciclo de vida dos dados.

O objetivo é centralizar dados públicos brasileiros, padronizar sua ingestão e disponibilizar informações confiáveis para aplicações de Business Intelligence, Analytics, Ciência de Dados e Inteligência Territorial.

A plataforma utiliza Databricks, Apache Spark, Delta Lake e Unity Catalog como base para armazenamento, processamento e governança dos dados.

---

# Arquitetura Geral

```
                    Fontes Públicas

     IBGE • Receita Federal • CAGED • RAIS
 Banco Central • OpenStreetMap • Outras APIs
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
     Dashboards • Analytics • Estudos
```

---

# Fluxo de Ingestão

Cada fonte segue um processo padronizado de ingestão composto por duas etapas.

1. Download dos dados da fonte oficial e armazenamento do arquivo bruto na Landing.

2. Leitura do arquivo bruto, criação do DataFrame Spark e persistência em tabelas Delta na camada Bronze.

Esse padrão garante reprodutibilidade, rastreabilidade e desacoplamento entre extração e processamento.

---

# Landing

A Landing é responsável por armazenar os arquivos exatamente como foram disponibilizados pelas fontes oficiais.

Características:

- Arquivos JSON originais
- Organização por fonte e data de carga
- Sem qualquer transformação
- Base para reprocessamentos
- Auditoria das cargas

Exemplo:

```
/Volumes/retail_intelligence/
└── bronze
    └── landing
        └── ibge
            ├── estados/
            ├── municipios/
            ├── regioes/
            ├── regioes_intermediarias/
            └── regioes_imediatas/
```

---

# Bronze

A Bronze representa a primeira camada estruturada do Lakehouse.

Nessa etapa os arquivos da Landing são convertidos para tabelas Delta, preservando integralmente os dados de origem.

Características:

- Dados brutos
- Sem regras de negócio
- Schema definido
- Persistência em Delta Lake
- Histórico das cargas
- Base para construção da Silver

Atualmente encontram-se implementadas as tabelas:

- ibge_estados_raw
- ibge_municipios_raw
- ibge_regioes_raw
- ibge_regioes_intermediarias_raw
- ibge_regioes_imediatas_raw

---

# Silver

A Silver será responsável pela padronização e integração dos dados provenientes da Bronze.

Principais atividades:

- Limpeza
- Conversão de tipos
- Padronização
- Deduplicação
- Enriquecimento
- Criação de dimensões
- Integração entre diferentes fontes

---

# Gold

A Gold disponibilizará os produtos analíticos consumidos pelas aplicações de negócio.

Serão disponibilizados:

- Data Marts
- Indicadores
- Métricas
- Views Analíticas
- Camadas para Business Intelligence

---

# Organização do Unity Catalog

```
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
- Python
- SQL

---

# Princípios Arquiteturais

A arquitetura foi construída seguindo os seguintes princípios:

- Fonte única da verdade (Single Source of Truth)
- Reprodutibilidade
- Escalabilidade
- Governança de dados
- Versionamento das cargas
- Baixo acoplamento entre etapas
- Alta rastreabilidade
- Padronização da ingestão