# Convenções

## Catálogo

```
retail_intelligence
```

---

## Schemas

```
bronze
silver
gold
metadata
sandbox
```

---

## Tabelas Bronze

```
ibge_populacao_raw

ibge_municipios_raw

caged_raw
```

---

## Dimensões

```
dim_estado

dim_municipio

dim_cnae
```

---

## Fatos

```
fato_populacao

fato_emprego

fato_pib
```

---

## Indicadores

```
indicador_potencial_consumo

indicador_expansao

indicador_competitividade
```

---

## Convenções Gerais

- snake_case
- nomes em português
- sem acentos
- sem espaços
- nomes descritivos
- tabelas dimensionais iniciam com dim_
- tabelas fato iniciam com fato_