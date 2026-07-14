# Convenções de Nomenclatura

Este documento define os padrões de nomenclatura adotados no projeto Retail Intelligence Brasil.

---

# Catálogo

```
retail_intelligence
```

---

# Schemas

```
bronze
silver
gold
metadata
sandbox
```

---

# Camadas

```
Landing
Bronze
Silver
Gold
```

---

# Convenções para Tabelas

## Bronze

As tabelas da camada Bronze representam os dados brutos provenientes das fontes oficiais.

Padrão:

```
<fonte>_<entidade>_raw
```

Exemplos implementados:

```
ibge_estados_raw

ibge_municipios_raw

ibge_regioes_raw

ibge_regioes_intermediarias_raw

ibge_regioes_imediatas_raw
```

---

## Silver

As tabelas da Silver representam dados padronizados e integrados.

Padrão:

```
<dominio>_<entidade>
```

Exemplos:

```
municipios

estados

empresas

populacao
```

---

## Gold

A camada Gold disponibiliza estruturas analíticas.

### Dimensões

Padrão:

```
dim_<entidade>
```

Exemplos:

```
dim_estado

dim_municipio

dim_cnae
```

### Fatos

Padrão:

```
fato_<processo>
```

Exemplos:

```
fato_populacao

fato_emprego

fato_pib
```

### Indicadores

Padrão:

```
indicador_<nome>
```

Exemplos:

```
indicador_potencial_consumo

indicador_expansao

indicador_competitividade
```

---

# Convenções para Notebooks

Os notebooks seguem a sequência de execução do pipeline.

```
01_download_<entidade>

02_bronze_<entidade>

03_silver_<entidade>

04_gold_<produto>
```

Exemplos:

```
01_download_estados

02_bronze_estados

01_download_municipios

02_bronze_municipios
```

---

# Convenções para Landing

Os arquivos brutos são armazenados em Volumes do Unity Catalog.

Padrão:

```
/Volumes/retail_intelligence/
    bronze/
        landing/
            <fonte>/
                <entidade>/
```

Exemplo:

```
/Volumes/retail_intelligence/
    bronze/
        landing/
            ibge/
                estados/
                municipios/
                regioes/
                regioes_intermediarias/
                regioes_imediatas/
```

---

# Convenções Gerais

- Utilizar `snake_case`.
- Utilizar nomes em português sempre que possível.
- Não utilizar acentos.
- Não utilizar espaços.
- Utilizar nomes descritivos.
- Utilizar letras minúsculas.
- Utilizar o sufixo `_raw` para tabelas da Bronze.
- Utilizar o prefixo `dim_` para dimensões.
- Utilizar o prefixo `fato_` para tabelas fato.
- Utilizar o prefixo `indicador_` para indicadores.
- Manter consistência entre nomes de notebooks, tabelas e diretórios.