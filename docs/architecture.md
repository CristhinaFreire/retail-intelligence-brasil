# Arquitetura

## Visão Geral

A plataforma Retail Intelligence Brasil foi concebida seguindo o paradigma Lakehouse.

O objetivo é centralizar dados públicos brasileiros e disponibilizá-los em uma camada analítica consistente para aplicações de Business Intelligence, Ciência de Dados e Inteligência Territorial.

---

## Arquitetura Geral

```
                  Fontes Públicas

     IBGE
     Receita Federal
     CAGED
     RAIS
     Banco Central
     OpenStreetMap
              │
              ▼
        Ingestion Layer
              │
              ▼
           Bronze Layer
              │
              ▼
           Silver Layer
              │
              ▼
            Gold Layer
              │
              ▼
 Dashboards • Analytics • Estudos
```

---

## Bronze

Objetivo

Armazenar os dados exatamente como disponibilizados pelas fontes oficiais.

Características

- Sem regras de negócio
- Dados históricos
- Auditoria
- Rastreabilidade

---

## Silver

Objetivo

Padronizar e integrar os dados.

Atividades

- Limpeza
- Conversão de tipos
- Padronização
- Deduplicação
- Enriquecimento
- Criação das dimensões

---

## Gold

Objetivo

Disponibilizar produtos analíticos.

Contém

- Data Marts
- Indicadores
- Métricas
- Views Analíticas

---

## Unity Catalog

```
retail_intelligence

bronze

silver

gold

metadata

sandbox
```

---

## Princípios Arquiteturais

- Fonte única da verdade
- Reprodutibilidade
- Escalabilidade
- Governança
- Versionamento
- Baixo acoplamento
- Alta rastreabilidade