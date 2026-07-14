# ADR-001

## Título

Adoção de arquitetura Lakehouse utilizando Databricks.

---

## Status

Aceito

---

## Contexto

O projeto necessita integrar grandes volumes de dados públicos provenientes de diversas fontes oficiais brasileiras.

As fontes possuem diferentes formatos, frequências de atualização e níveis de granularidade.

Era necessário definir uma arquitetura que permitisse escalabilidade, governança e baixo custo de manutenção.

---

## Decisão

Adotar arquitetura Lakehouse baseada em:

- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog
- Arquitetura Medallion

---

## Consequências

### Positivas

- Escalabilidade
- Governança
- Versionamento
- Performance
- Flexibilidade

### Negativas

- Maior curva de aprendizado
- Dependência do ambiente Databricks

---

## Data

14/07/2026