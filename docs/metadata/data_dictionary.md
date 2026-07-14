# Dicionário de Dados

Este documento apresenta o catálogo das tabelas existentes na plataforma **Retail Intelligence Brasil**, indicando a camada, a fonte de origem, a finalidade de cada tabela e seu estágio de implementação.

O detalhamento de colunas, tipos de dados, regras de negócio e relacionamentos será documentado individualmente para cada tabela.

---

# Camada Landing

A Landing armazena os arquivos originais exatamente como disponibilizados pelas fontes oficiais, preservando os dados brutos para auditoria, rastreabilidade e reprocessamento.

| Origem | Formato | Descrição | Status |
|---------|----------|-----------|--------|
| ibge/estados | JSON | Estados brasileiros | Implementado |
| ibge/municipios | JSON | Municípios brasileiros | Implementado |
| ibge/regioes | JSON | Regiões geográficas | Implementado |
| ibge/regioes_intermediarias | JSON | Regiões intermediárias | Implementado |
| ibge/regioes_imediatas | JSON | Regiões imediatas | Implementado |

---

# Camada Bronze

A camada Bronze armazena os dados brutos provenientes das fontes públicas em tabelas Delta, preservando a estrutura original das informações.

| Tabela | Fonte | Descrição | Formato | Status |
|---------|--------|-----------|---------|--------|
| ibge_estados_raw | IBGE | Estados brasileiros | Delta | Implementado |
| ibge_municipios_raw | IBGE | Municípios brasileiros | Delta | Implementado |
| ibge_regioes_raw | IBGE | Regiões geográficas do Brasil | Delta | Implementado |
| ibge_regioes_intermediarias_raw | IBGE | Regiões intermediárias do IBGE | Delta | Implementado |
| ibge_regioes_imediatas_raw | IBGE | Regiões imediatas do IBGE | Delta | Implementado |

---

# Camada Silver

A camada Silver armazenará os dados padronizados, tratados e integrados provenientes da Bronze.

| Tabela | Descrição | Status |
|---------|-----------|--------|
| dim_estado | Dimensão dos estados brasileiros | Planejado |
| dim_municipio | Dimensão dos municípios brasileiros | Planejado |
| dim_regiao | Dimensão das regiões brasileiras | Planejado |
| dim_regiao_intermediaria | Dimensão das regiões intermediárias | Planejado |
| dim_regiao_imediata | Dimensão das regiões imediatas | Planejado |

---

# Camada Gold

A camada Gold disponibilizará estruturas analíticas voltadas ao consumo por aplicações de Business Intelligence e Analytics.

## Tabelas Fato

| Tabela | Descrição | Status |
|---------|-----------|--------|
| fato_populacao | Indicadores populacionais | Planejado |
| fato_pib | Indicadores econômicos | Planejado |
| fato_emprego | Indicadores de emprego | Planejado |
| fato_empresas | Indicadores empresariais | Planejado |

## Indicadores

| Tabela | Descrição | Status |
|---------|-----------|--------|
| indicador_potencial_consumo | Potencial de consumo por município | Planejado |
| indicador_expansao | Índice de expansão para varejo | Planejado |
| indicador_competitividade | Indicador de competitividade regional | Planejado |
| indicador_desenvolvimento | Indicador de desenvolvimento socioeconômico | Planejado |

---

# Próximas Fontes

As próximas integrações ampliarão o catálogo de dados da plataforma.

| Fonte | Domínio | Status |
|--------|----------|--------|
| Receita Federal | Empresas | Planejado |
| CAGED | Emprego | Planejado |
| RAIS | Mercado de Trabalho | Planejado |
| Banco Central | Economia | Planejado |
| OpenStreetMap | Geoespacial | Planejado |
| DATASUS | Saúde | Planejado |
| MEC | Educação | Planejado |
| ANP | Energia | Planejado |

---

# Observações

- A camada **Landing** armazena os arquivos originais em formato JSON utilizando Volumes do Unity Catalog.
- A camada **Bronze** armazena os dados em tabelas Delta, preservando a estrutura disponibilizada pelas fontes oficiais.
- O detalhamento técnico de cada tabela (colunas, tipos de dados, chaves, relacionamentos e regras de negócio) será documentado em arquivos específicos à medida que novas entidades forem implementadas.