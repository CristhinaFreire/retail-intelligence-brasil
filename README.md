# Retail Intelligence Brasil

Plataforma de Engenharia de Dados desenvolvida sobre arquitetura Lakehouse para centralizar, padronizar e disponibilizar dados públicos brasileiros voltados à Inteligência de Mercado, Expansão de Varejo e Analytics Territorial.

O projeto utiliza Databricks, Apache Spark, Delta Lake e Unity Catalog para construir um ambiente escalável de ingestão, transformação e disponibilização de dados públicos.

---

# Objetivo

Construir uma plataforma unificada de dados públicos capaz de apoiar análises estratégicas para o varejo brasileiro por meio de uma arquitetura moderna baseada no padrão Lakehouse.

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

```
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

Atualmente a camada **Bronze** encontra-se implementada, realizando a ingestão dos dados públicos, armazenamento dos arquivos brutos na Landing e persistência em tabelas Delta no Unity Catalog.

---

# Tecnologias

- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog
- Python
- SQL
- Git
- GitHub

---

# Estrutura do Projeto

```
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
├── notebooks/
├── sql/
├── scripts/
├── tests/
└── README.md
```

---

# Fontes de Dados

Atualmente o projeto contempla integração com as seguintes fontes públicas:

- IBGE
- Receita Federal
- CAGED
- RAIS
- Banco Central
- OpenStreetMap
- ANP
- DATASUS
- MEC

Novas fontes poderão ser incorporadas conforme a evolução da plataforma.

---

# Status do Projeto

### Concluído

- Estrutura do Lakehouse
- Unity Catalog
- Camada Landing
- Camada Bronze
- Padrão de ingestão
- Padronização dos notebooks
- Documentação técnica

### Em desenvolvimento

- Camada Silver
- Camada Gold
- Modelagem analítica
- Dashboards e casos de negócio

---

# Documentação

- Arquitetura
- Modelo de Dados
- Fontes de Dados
- Convenções de Nomenclatura
- Metadados
- ADRs (Architecture Decision Records)
- Roadmap

---

# Licença

MIT License.