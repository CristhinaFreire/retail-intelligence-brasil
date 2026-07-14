# IBGE

## Visão Geral

O Instituto Brasileiro de Geografia e Estatística (IBGE) é a principal fonte de dados geográficos, territoriais, demográficos e estatísticos utilizada pela plataforma Retail Intelligence Brasil.

Atualmente, a integração utiliza a API de Localidades do IBGE para obter informações sobre a divisão político-administrativa do território brasileiro.

---

# Fonte

| Propriedade | Valor |
|-------------|-------|
| Instituição | Instituto Brasileiro de Geografia e Estatística (IBGE) |
| Tipo | API REST |
| Formato | JSON |
| Autenticação | Não requerida |
| Frequência | Sob demanda |

---

# API Utilizada

Base URL

```
https://servicodados.ibge.gov.br/api/v1/localidades
```

---

# Endpoints Implementados

| Entidade | Endpoint |
|----------|----------|
| Estados | `/estados` |
| Municípios | `/municipios` |
| Regiões | `/regioes` |
| Regiões Intermediárias | `/regioes-intermediarias` |
| Regiões Imediatas | `/regioes-imediatas` |

---

# Pipeline

Cada entidade segue o mesmo padrão de ingestão.

```
API IBGE
      │
      ▼
01_download_<entidade>
      │
      ▼
Landing (JSON)
      │
      ▼
02_bronze_<entidade>
      │
      ▼
Tabela Delta
```

---

# Tabelas Geradas

| Tabela Bronze | Descrição |
|---------------|-----------|
| ibge_estados_raw | Estados brasileiros |
| ibge_municipios_raw | Municípios brasileiros |
| ibge_regioes_raw | Regiões brasileiras |
| ibge_regioes_intermediarias_raw | Regiões intermediárias |
| ibge_regioes_imediatas_raw | Regiões imediatas |

---

# Estrutura de Armazenamento

## Landing

```
/Volumes/retail_intelligence/
    bronze/
        landing/
            ibge/
```

## Bronze

```
retail_intelligence.bronze
```

---

# Qualidade dos Dados

Durante a ingestão são realizadas as seguintes validações:

- Disponibilidade da API.
- Status HTTP 200.
- Conversão da resposta para JSON.
- Persistência do arquivo na Landing.
- Conversão para Spark DataFrame.
- Escrita em Delta Lake.

---

# Casos de Uso

Os dados do IBGE serão utilizados como base para:

- Expansão de lojas.
- Inteligência territorial.
- Enriquecimento de dados.
- Modelagem dimensional.
- Construção de indicadores geográficos.
- Integração com outras bases públicas.