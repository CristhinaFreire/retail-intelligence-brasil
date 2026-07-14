# ADR-001

# Título

Adoção da arquitetura Lakehouse utilizando Databricks

---

# Status

Aceito

---

# Contexto

O projeto Retail Intelligence Brasil tem como objetivo integrar dados públicos provenientes de diferentes órgãos governamentais brasileiros para apoiar análises de Inteligência de Mercado, Expansão de Varejo e Analytics Territorial.

As fontes possuem características distintas, incluindo diferentes formatos, volumes, frequências de atualização e estruturas de dados. Era necessário definir uma arquitetura capaz de suportar ingestão escalável, armazenamento confiável, governança centralizada e evolução incremental das camadas analíticas.

---

# Decisão

Foi adotada uma arquitetura **Lakehouse** baseada nos seguintes componentes:

- Databricks como plataforma de processamento.
- Apache Spark para processamento distribuído.
- Delta Lake como formato de armazenamento das tabelas.
- Unity Catalog para governança dos ativos de dados.
- Arquitetura Medallion (Landing → Bronze → Silver → Gold).

A ingestão segue um padrão composto por duas etapas:

1. Download dos dados e armazenamento dos arquivos originais na camada Landing.
2. Conversão dos arquivos para tabelas Delta na camada Bronze.

Esse padrão será utilizado por todas as futuras integrações da plataforma.

---

# Consequências

## Positivas

- Arquitetura escalável.
- Separação entre ingestão e transformação.
- Preservação dos dados brutos para auditoria e reprocessamento.
- Governança centralizada por meio do Unity Catalog.
- Armazenamento transacional utilizando Delta Lake.
- Padronização dos pipelines de ingestão.
- Facilidade de evolução para as camadas Silver e Gold.

## Negativas

- Dependência da plataforma Databricks.
- Maior curva de aprendizado para novos desenvolvedores.
- Maior custo operacional quando comparado a soluções locais.

---

# Data

14/07/2026