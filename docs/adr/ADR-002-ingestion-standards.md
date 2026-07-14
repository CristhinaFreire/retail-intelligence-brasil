# ADR-002 - Padrões de Ingestão de Dados

## Status

Aceito

---

## Data

04/06/2026

---

## Contexto

O projeto **Retail Intelligence Brasil** tem como objetivo construir uma plataforma de dados escalável para centralizar informações públicas relevantes ao varejo brasileiro.

As fontes de dados possuem características distintas, incluindo:

- APIs REST
- Arquivos CSV
- Arquivos TXT
- Arquivos ZIP
- Parquet
- Dados Geoespaciais
- FTP

Era necessário definir um padrão único de ingestão para garantir consistência arquitetural, facilitar a manutenção dos pipelines e reduzir a complexidade do projeto ao longo do tempo.

---

# Decisão

Foram definidos os seguintes padrões oficiais para ingestão de dados.

## Linguagem

Toda a implementação será realizada utilizando **PySpark**.

Não serão utilizados como padrão do projeto:

- Pandas
- Polars
- DuckDB
- SQLite

Exceções poderão ocorrer apenas para pequenos utilitários ou scripts administrativos que não façam parte dos pipelines de dados.

---

## Fonte dos Dados

A prioridade para obtenção dos dados será:

1. API Oficial
2. Arquivos Oficiais
3. FTP Oficial
4. Web Scraping (somente quando não existir outra alternativa)

Sempre que existir uma API oficial, ela deverá ser utilizada.

Downloads manuais deverão ser evitados.

---

## Formato de Entrada

A camada de Landing deverá preservar exatamente o formato disponibilizado pela fonte.

Exemplos:

| Fonte | Formato |
|--------|----------|
| IBGE | JSON |
| Banco Central | JSON |
| Receita Federal | ZIP |
| CAGED | CSV |
| RAIS | TXT |
| OpenStreetMap | PBF |

---

## Camadas da Arquitetura

Todos os pipelines deverão seguir obrigatoriamente o fluxo abaixo.

```
Fonte Oficial
        │
        ▼
Landing
        │
        ▼
Validação
        │
        ▼
Bronze
        │
        ▼
Transformação
        │
        ▼
Silver
        │
        ▼
Modelagem
        │
        ▼
Gold
```

---

## Landing

A camada Landing representa o momento em que os dados foram obtidos da fonte oficial, mas ainda não sofreram qualquer transformação.

Nesta etapa serão realizadas apenas validações estruturais, como:

- disponibilidade da fonte;
- quantidade de registros;
- formato do arquivo;
- estrutura do JSON;
- campos obrigatórios.

---

## Bronze

A camada Bronze deverá preservar integralmente os dados da fonte.

Não serão aplicadas regras de negócio.

Alterações permitidas:

- conversão para Delta Lake;
- inclusão de metadados técnicos;
- controle de carga.

---

## Silver

A camada Silver será responsável por:

- limpeza;
- padronização;
- deduplicação;
- enriquecimento;
- tipagem;
- normalização.

---

## Gold

A camada Gold conterá exclusivamente produtos analíticos.

Exemplos:

- dimensões;
- fatos;
- indicadores;
- data marts;
- tabelas para consumo analítico.

---

## Formato de Armazenamento

Todas as tabelas persistidas na plataforma deverão utilizar **Delta Lake**.

Não serão persistidas tabelas em:

- CSV
- JSON
- XLSX

Esses formatos existirão apenas como origem dos dados.

---

## Estrutura dos Pipelines

Cada notebook deverá possuir apenas uma responsabilidade.

Exemplo:

```
01_download_estados

↓

02_bronze_estados

↓

03_silver_dim_estado

↓

04_quality_dim_estado

↓

05_gold_indicadores
```

Nenhum notebook deverá executar múltiplas etapas da arquitetura.

---

## Benefícios

A adoção deste padrão proporciona:

- maior escalabilidade;
- padronização dos pipelines;
- facilidade de manutenção;
- reutilização de código;
- governança;
- reprodutibilidade;
- alinhamento com arquiteturas Lakehouse modernas.

---

## Consequências

### Positivas

- Código consistente entre todas as fontes.
- Redução da complexidade.
- Facilidade para automação.
- Maior facilidade de onboarding de novos colaboradores.
- Evolução simplificada da plataforma.

### Negativas

- Maior quantidade de notebooks.
- Curva de aprendizado inicial mais elevada.
- Algumas cargas simples podem exigir mais etapas do que o estritamente necessário.

---

## Referências

- Databricks Lakehouse Architecture
- Delta Lake Documentation
- Apache Spark Documentation
- Medallion Architecture
