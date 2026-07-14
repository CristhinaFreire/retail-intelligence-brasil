# Fontes de Dados

Este documento cataloga as fontes públicas utilizadas pela plataforma Retail Intelligence Brasil, indicando o domínio de informação e o estágio de implementação de cada integração.

| Fonte | Domínio | Forma de Acesso | Status |
|--------|----------|-----------------|--------|
| IBGE | Demografia, Divisão Territorial e Indicadores Estatísticos | API REST | Implementado |
| Receita Federal | Empresas | Base Pública | Planejado |
| CAGED | Emprego | Download de Arquivos | Planejado |
| RAIS | Mercado de Trabalho | Download de Arquivos | Planejado |
| Banco Central | Economia | API REST | Planejado |
| OpenStreetMap | Geoespacial | API / Download | Planejado |
| DATASUS | Saúde | Download de Arquivos | Planejado |
| MEC | Educação | API / Download | Planejado |
| ANP | Energia | Download de Arquivos | Planejado |

---

# Fonte Implementada

## IBGE

Atualmente a plataforma possui integração implementada com duas APIs públicas do IBGE:

- API de Localidades
- API SIDRA

Os dados são obtidos por meio de chamadas HTTP, armazenados inicialmente na camada Landing em formato JSON e posteriormente persistidos na Bronze em tabelas Delta.

---

## API de Localidades

Responsável pelas informações territoriais utilizadas como dimensões da plataforma.

### Entidades implementadas

| Entidade | Endpoint | Tabela Bronze |
|----------|----------|---------------|
| Estados | `/localidades/estados` | `ibge_estados_raw` |
| Regiões | `/localidades/regioes` | `ibge_regioes_raw` |
| Municípios | `/localidades/municipios` | `ibge_municipios_raw` |
| Regiões Intermediárias | `/localidades/regioes-intermediarias` | `ibge_regioes_intermediarias_raw` |
| Regiões Imediatas | `/localidades/regioes-imediatas` | `ibge_regioes_imediatas_raw` |

---

## API SIDRA

Responsável pelos indicadores demográficos utilizados nas análises de expansão do varejo.

### Tabelas implementadas

| Tabela SIDRA | Descrição | Tabela Bronze |
|--------------|-----------|---------------|
| 4709 | População residente, variação absoluta e taxa de crescimento geométrico | `ibge_sidra_populacao_raw` |
| 9515 | Índice de envelhecimento, idade mediana e razão de sexo | `ibge_sidra_indicadores_demograficos_raw` |
| 9514 | População residente por sexo e grupos de idade | `ibge_sidra_populacao_sexo_idade_raw` |

---

# Próximas Fontes

As demais integrações serão implementadas conforme o roadmap do projeto.

Cada nova fonte deverá possuir documentação própria contendo:

- objetivo;
- origem dos dados;
- forma de acesso;
- periodicidade;
- granularidade;
- estrutura dos dados;
- pipeline de ingestão;
- dicionário de dados;
- casos de uso.