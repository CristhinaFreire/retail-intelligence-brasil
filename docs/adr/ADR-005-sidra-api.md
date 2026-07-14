# ADR-005 — Padrão de Consumo da API SIDRA

## Status

Aceito

---

## Contexto

O projeto Retail Intelligence Brasil utiliza a API pública do SIDRA (Sistema IBGE de Recuperação Automática) como fonte oficial para obtenção de indicadores estatísticos do IBGE.

Antes da implementação dos notebooks de ingestão, foram realizados Spikes Técnicos para validar a estrutura da API, seus parâmetros de consulta, limitações e boas práticas de utilização.

---

## Problema

A documentação da API apresenta a estrutura geral das URLs, porém não demonstra claramente todas as combinações possíveis entre tabelas, classificações e categorias.

Além disso, algumas consultas retornam erros quando parâmetros obrigatórios não são informados corretamente.

Era necessário estabelecer um padrão único de consumo para todo o projeto.

---

## Decisão

Todas as integrações com a API SIDRA seguirão o padrão abaixo.

URL base:

```
https://apisidra.ibge.gov.br
```

Estrutura de consulta:

```
/values/
t/{tabela}
/n{nivel}/{localidade}
/v/{variavel}
/p/{periodo}
/c{classificacao}/{categoria}
```

Os parâmetros opcionais (`v`, `p`, `c`) somente serão utilizados quando necessários para cada tabela.

---

## Níveis territoriais

Os seguintes níveis territoriais foram validados:

| Código | Nível |
|---------|--------|
| n1 | Brasil |
| n2 | Grandes Regiões |
| n3 | Unidade da Federação |
| n24 | Região Geográfica Intermediária |
| n25 | Região Geográfica Imediata |
| n33 | Concentração Urbana |
| n6 | Município |

Para o projeto Retail Intelligence Brasil, o nível padrão será:

```
n6/all
```

permitindo a extração dos dados para todos os municípios brasileiros.

---

## Comportamento da API

Durante os testes foram observados os seguintes comportamentos.

### Consulta sem nível territorial

Exemplo:

```
/values/t/4709
```

Retorno:

```
400

Pelo menos um parâmetro no formato Nnnnn deve ser especificado.
```

---

### Nível territorial inválido

Exemplo:

```
n6
```

sem informar a localidade.

Retorno:

```
400

Parâmetro N6 mal especificado.
```

---

### Consulta válida

Exemplo:

```
https://apisidra.ibge.gov.br/values/t/4709/n6/all
```

Retorno:

```
200
```

com dados em formato JSON.

---

## Estrutura da resposta

Todas as respostas da API apresentam:

- primeira posição contendo o cabeçalho;
- demais posições contendo os registros.

Exemplo:

```
[
   { cabeçalho },
   { registro 1 },
   { registro 2 },
   ...
]
```

Por esse motivo, todos os notebooks removem o primeiro elemento antes da persistência.

Exemplo:

```python
header = response_json[0]

landing_data = response_json[1:]
```

---

## Estratégia de ingestão

O padrão adotado é:

```
API SIDRA
        │
        ▼
requests.get()
        │
        ▼
response.json()
        │
        ▼
remoção do cabeçalho
        │
        ▼
Landing (JSON)
        │
        ▼
Spark Read JSON
        │
        ▼
Bronze Delta (RAW)
```

---

## Tratamento de erros

Toda requisição deverá validar o código HTTP retornado pela API.

Consultas diferentes de HTTP 200 deverão interromper o processamento.

Também deverá ser utilizado timeout padrão de 60 segundos.

---

## Justificativa

A definição de um padrão único reduz a duplicação de código, facilita a manutenção dos notebooks e garante consistência entre todas as integrações do SIDRA realizadas pelo projeto.

---

## Evidências

Spikes realizados:

- 99_spike_sidra_api
- 99_spike_sidra_4709
- 99_spike_sidra_9515
- 99_spike_sidra_9514

Principais validações:

- URL base da API;
- estrutura das requisições;
- obrigatoriedade do nível territorial;
- estrutura do JSON retornado;
- remoção do cabeçalho;
- persistência na Landing;
- persistência RAW na Bronze.