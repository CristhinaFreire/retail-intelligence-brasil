# Retail Intelligence Brasil

Plataforma de Engenharia de Dados desenvolvida sobre arquitetura Lakehouse para centralizar, padronizar e disponibilizar dados públicos brasileiros voltados à Inteligência de Mercado, Expansão de Varejo e Analytics Territorial.

O projeto utiliza Databricks, Apache Spark, Delta Lake e Unity Catalog para construir um ambiente escalável de ingestão, transformação e disponibilização de dados públicos.

---

# Objetivo

Construir uma plataforma unificada de dados públicos brasileiros para apoiar decisões de expansão do varejo, inteligência territorial e análises demográficas, utilizando uma arquitetura Lakehouse baseada no padrão Medallion.

Entre as principais perguntas que a plataforma busca responder estão:

- Onde abrir uma nova loja?
- Quais municípios apresentam maior potencial de consumo?
- Como evolui a população de uma determinada região?
- Como está distribuída a concorrência?
- Quais cidades apresentam crescimento econômico consistente?
- Qual o perfil socioeconômico de uma região?

---

# Arquitetura

A plataforma segue a arquitetura Lakehouse utilizando o padrão Medallion.

```text
                 Fontes Oficiais
                        │
                        ▼
              Landing (JSON)
                        │
                        ▼
             Bronze (Delta Lake)
                        │
                        ▼
             Silver (Curated)
                        │
                        ▼
            Gold (Analytics)
```

Atualmente encontram-se implementadas:

- Camada Landing para armazenamento dos arquivos brutos;
- Camada Bronze para persistência dos dados em Delta Lake;
- Integrações com a API de Localidades do IBGE;
- Integrações com a API SIDRA do IBGE.

As camadas Silver e Gold serão implementadas nas próximas etapas do projeto.

---

# Arquitetura de Ingestão

Todas as integrações seguem o mesmo padrão de processamento.

```text
API Pública
        │
        ▼
Landing (JSON)
        │
        ▼
Bronze (Delta Lake)
        │
        ▼
Silver (Curated)
        │
        ▼
Gold (Analytics)
```

Esse padrão garante consistência entre todas as fontes públicas integradas à plataforma.

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

# Estrutura do Projeto

```text
retail-intelligence-brasil/
│
├── docs/
│   ├── adr/
│   ├── diagrams/
│   ├── metadata/
│   ├── sources/
│   ├── architecture.md
│   ├── data_model.md
│   ├── data_sources.md
│   ├── naming_conventions.md
│   └── roadmap.md
│
├── 01_ingestion/
│   └── ibge/
│
├── sql/
├── scripts/
├── tests/
└── README.md
```

---

# Fontes de Dados

Atualmente encontram-se implementadas:

- IBGE Localidades
- IBGE SIDRA

Planejadas:

- Receita Federal
- CAGED
- RAIS
- Banco Central
- OpenStreetMap
- ANP
- DATASUS
- MEC

As integrações implementadas representam a primeira etapa da plataforma. Novas fontes públicas serão incorporadas conforme a evolução do projeto e das necessidades analíticas.

---

# Status do Projeto

## Concluído

- Arquitetura Lakehouse
- Unity Catalog
- Camada Landing implementada
- Camada Bronze implementada
- API IBGE Localidades
- API SIDRA
- Integração das tabelas SIDRA 4709, 9515 e 9514
- Padrão de ingestão
- Padrão de documentação
- Architecture Decision Records (ADRs)

## Em desenvolvimento

- Camada Silver
- Dimensões de negócio
- Modelagem analítica
- Indicadores de expansão
- Dashboards

---

# Documentação

A documentação do projeto encontra-se organizada nos seguintes documentos:

- Arquitetura
- Modelo de Dados
- Fontes de Dados
- Convenções de Nomenclatura
- Metadados
- Architecture Decision Records (ADRs)
- Roadmap

---

# Documentação Arquitetural

O projeto utiliza **Architecture Decision Records (ADRs)** para registrar decisões técnicas relevantes durante sua evolução.

Entre as principais decisões documentadas estão:

- Arquitetura Lakehouse;
- Padrão de ingestão de dados;
- Modelagem da camada Bronze;
- Estratégia de integração com a API SIDRA;
- Utilização das classificações da API SIDRA;
- Estratégia de particionamento para tabelas multidimensionais.

---

# Métricas do Projeto

Atualmente a plataforma possui:

- 2 APIs públicas integradas;
- 8 notebooks de ingestão;
- 3 tabelas SIDRA implementadas;
- 5 entidades da API de Localidades;
- documentação arquitetural baseada em ADRs;
- arquitetura Lakehouse utilizando Delta Lake e Unity Catalog.

---

# Integrações Implementadas

## API IBGE Localidades

Entidades atualmente implementadas:

- Estados
- Regiões
- Municípios
- Regiões Intermediárias
- Regiões Imediatas

## API SIDRA

| Tabela | Indicador |
|---------|-----------|
| 4709 | População residente, variação absoluta e taxa de crescimento geométrico |
| 9515 | Índice de envelhecimento, idade mediana e razão de sexo |
| 9514 | População residente por sexo e grupos de idade |

---

# Próximos Passos

- Implementação da camada Silver
- Modelagem dimensional
- Integração de novos indicadores do SIDRA
- Integração com Receita Federal
- Integração com RAIS
- Integração com CAGED
- Construção da camada Gold
- Desenvolvimento de dashboards analíticos

---

# Licença

Este projeto é distribuído sob a licença MIT.

MIT License.