# Fontes de Dados

Este documento cataloga as fontes públicas utilizadas pela plataforma Retail Intelligence Brasil, indicando o domínio de informação e o estágio de implementação de cada integração.

| Fonte | Domínio | Forma de Acesso | Status |
|--------|----------|-----------------|--------|
| IBGE | Demografia e Divisão Territorial | API REST | Implementado |
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

Atualmente a plataforma possui integração implementada com a API de Localidades do IBGE.

Os dados são obtidos por meio de chamadas HTTP, armazenados inicialmente na camada Landing em formato JSON e posteriormente persistidos na Bronze em tabelas Delta.

### Entidades implementadas

| Entidade | Endpoint | Tabela Bronze |
|----------|----------|---------------|
| Estados | `/localidades/estados` | `ibge_estados_raw` |
| Regiões | `/localidades/regioes` | `ibge_regioes_raw` |
| Municípios | `/localidades/municipios` | `ibge_municipios_raw` |
| Regiões Intermediárias | `/localidades/regioes-intermediarias` | `ibge_regioes_intermediarias_raw` |
| Regiões Imediatas | `/localidades/regioes-imediatas` | `ibge_regioes_imediatas_raw` |

---

# Próximas Fontes

As demais integrações serão implementadas conforme o roadmap do projeto. Cada fonte possuirá documentação específica contendo:

- Objetivo
- Origem dos dados
- Forma de acesso
- Periodicidade
- Granularidade
- Estrutura dos dados
- Dicionário de Dados
- Pipeline de ingestão
- Casos de uso