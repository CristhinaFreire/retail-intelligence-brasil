# Retail Intelligence Brasil

Uma plataforma de Engenharia de Dados construída sobre arquitetura Lakehouse para centralizar, padronizar e disponibilizar dados públicos brasileiros voltados à Inteligência de Mercado, Expansão de Varejo e Analytics Territorial.

---

## Objetivo

O projeto tem como objetivo construir uma plataforma unificada de dados públicos que permita responder perguntas estratégicas do varejo brasileiro através de uma arquitetura moderna baseada em Databricks, Delta Lake e Unity Catalog.

Exemplos de perguntas que a plataforma pretende responder:

- Onde abrir uma nova loja?
- Quais municípios apresentam maior potencial de consumo?
- Como evolui a população de determinada região?
- Como está distribuída a concorrência?
- Quais cidades apresentam crescimento econômico consistente?
- Qual o perfil socioeconômico de uma região?

---

## Arquitetura

O projeto utiliza arquitetura Lakehouse baseada na arquitetura Medallion.

```
Fontes Oficiais
        │
        ▼
     Bronze
        │
        ▼
     Silver
        │
        ▼
      Gold
```

---

## Tecnologias

- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog
- SQL
- Python
- Git
- GitHub

---

## Estrutura do Projeto

```
retail-intelligence-brasil/

docs/
notebooks/
sql/
scripts/
tests/
```

---

## Fontes de Dados

- IBGE
- Receita Federal
- CAGED
- RAIS
- Banco Central
- OpenStreetMap
- ANP
- DATASUS
- MEC

---

## Documentação

- [Arquitetura](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [Fontes de Dados](docs/data_sources.md)
- [Padrões](docs/naming_conventions.md)

---

## Licença

MIT License.