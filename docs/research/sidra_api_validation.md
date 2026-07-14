# Validação Técnica - API SIDRA

## Objetivo

Validar o funcionamento da API SIDRA (API de Agregados do IBGE) antes da implementação dos pipelines da camada Bronze.

O objetivo deste estudo foi compreender a estrutura das requisições, identificar o formato das respostas e validar a viabilidade técnica da ingestão automatizada dos indicadores estatísticos.

---

# Data

14/07/2026

---

# Escopo

Primeira validação utilizando a tabela:

| Item | Valor |
|------|--------|
| Tabela SIDRA | 4709 |
| Indicador | População residente |
| Fonte | Censo Demográfico 2022 |

---

# Descobertas

## URL Base

```
https://apisidra.ibge.gov.br
```

---

## Estrutura da API

As consultas seguem o padrão:

```
https://apisidra.ibge.gov.br/values/
t/{tabela}/
n{nivel}/{localidade}/
v/{variavel}/
p/{periodo}
```

Onde:

| Parâmetro | Descrição |
|------------|-----------|
| t | Código da tabela SIDRA |
| n | Nível territorial |
| all | Todas as localidades do nível informado |
| v | Variável |
| p | Período |

---

# Consulta Validada

```
https://apisidra.ibge.gov.br/values/t/4709/n6/all/v/93/p/2022
```

---

# Significado dos Parâmetros

| Parâmetro | Valor |
|------------|--------|
| Tabela | 4709 |
| Variável | 93 |
| Período | 2022 |
| Nível Territorial | Município |
| Localidades | Todos os municípios |

---

# Resultado da Consulta

Status HTTP

```
200 OK
```

Total de registros retornados

```
5571
```

Observação

A primeira posição do JSON contém apenas o cabeçalho da resposta.

Os dados iniciam no índice 1.

```
dados[0] -> Cabeçalho

dados[1:] -> Dados
```

---

# Estrutura do JSON

Campos identificados

| Campo | Descrição |
|---------|-----------|
| NC | Código do nível territorial |
| NN | Nome do nível territorial |
| MC | Código da unidade de medida |
| MN | Unidade de medida |
| V | Valor do indicador |
| D1C | Código IBGE do Município |
| D1N | Nome do Município |
| D2C | Código da variável |
| D2N | Nome da variável |
| D3C | Código do período |
| D3N | Nome do período |

---

# Conclusões

A API SIDRA atende plenamente aos requisitos do projeto.

Foi possível validar:

- consumo via HTTP;
- retorno em JSON;
- cobertura nacional;
- disponibilidade do código IBGE;
- estrutura consistente da resposta;
- utilização do código oficial do município.

---

# Impacto na Arquitetura

Os pipelines da camada Bronze poderão seguir o mesmo padrão utilizado para a API de Localidades.

```
API SIDRA

↓

Landing (JSON)

↓

Spark

↓

Delta Lake

↓

Bronze
```

A única diferença será a construção dinâmica da URL utilizando:

- tabela;
- variável;
- período;
- nível territorial.

---

# Próximos Passos

- Implementar `14_bronze_sidra_populacao`.
- Generalizar a construção das URLs da API SIDRA.
- Catalogar as demais tabelas prioritárias para o projeto.