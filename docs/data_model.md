# Modelo de Dados

Este documento apresenta o modelo conceitual das tabelas atualmente implementadas na camada Bronze do projeto Retail Intelligence Brasil.

A camada Bronze preserva os dados em formato RAW, mantendo a estrutura original das fontes públicas.

---

# API IBGE Localidades

As tabelas da API de Localidades representam a base territorial utilizada pelas demais integrações.

```text
                 ibge_regioes_raw
                        │
                        │ codigo_regiao
                        ▼
                ibge_estados_raw
                        │
                        │ codigo_uf
                        ▼
               ibge_municipios_raw
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
ibge_regioes_intermediarias_raw   (município pertence a uma região intermediária)
            │
            ▼
ibge_regioes_imediatas_raw
```

---

## Tabelas

| Tabela | Descrição |
|---------|-----------|
| ibge_regioes_raw | Grandes Regiões do Brasil |
| ibge_estados_raw | Unidades da Federação |
| ibge_municipios_raw | Municípios brasileiros |
| ibge_regioes_intermediarias_raw | Regiões Geográficas Intermediárias |
| ibge_regioes_imediatas_raw | Regiões Geográficas Imediatas |

---

# API SIDRA

As tabelas SIDRA armazenam indicadores estatísticos associados aos municípios brasileiros.

```text
                 ibge_municipios_raw
                         │
         codigo_municipio (IBGE)
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
ibge_sidra_populacao_raw
ibge_sidra_indicadores_demograficos_raw
ibge_sidra_populacao_sexo_idade_raw
```

---

## Tabelas

| Tabela | Origem | Descrição |
|---------|---------|-----------|
| ibge_sidra_populacao_raw | SIDRA 4709 | População residente e crescimento populacional |
| ibge_sidra_indicadores_demograficos_raw | SIDRA 9515 | Índice de envelhecimento, idade mediana e razão de sexo |
| ibge_sidra_populacao_sexo_idade_raw | SIDRA 9514 | População residente por sexo e grupos de idade |

---

# Relacionamentos

Atualmente os relacionamentos são conceituais, pois a camada Bronze preserva os dados exatamente como retornados pelas APIs.

A integração física entre as tabelas será realizada na camada Silver utilizando os códigos oficiais do IBGE.

As principais chaves de integração serão:

- código da Região;
- código da Unidade da Federação;
- código do Município (IBGE).

---

# Evolução Esperada

Na camada Silver serão implementadas:

- Dimensão Região;
- Dimensão Estado;
- Dimensão Município;
- Dimensão Tempo;
- Dimensão Faixa Etária;
- Dimensão Sexo;
- Fatos Demográficos.

A camada Gold utilizará essas dimensões para construção dos modelos analíticos voltados à expansão do varejo.