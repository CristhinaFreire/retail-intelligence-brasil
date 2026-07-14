# ADR-004 — Estratégia de Extração da Tabela SIDRA 9514

## Status

Aceito

---

## Contexto

A tabela SIDRA 9514 (População residente por sexo, idade e forma de declaração da idade) foi selecionada para compor a camada Bronze do projeto Retail Intelligence Brasil.

Durante a fase de pesquisa (Spikes Técnicos) foram realizados testes de consumo da API do SIDRA para compreender sua estrutura e limitações.

Foram identificadas as seguintes classificações da tabela:

| Classificação | Código |
|---------------|--------|
| Sexo | C2 |
| Idade | C287 |
| Forma de declaração da idade | C286 |

Também foi validado que a API permite expandir classificações utilizando o parâmetro:

```
c{codigo}/all
```

Exemplo:

```
https://apisidra.ibge.gov.br/values/t/9514/n6/all/c2/all
```

retornando:

- Total
- Homens
- Mulheres

---

## Problema

Ao solicitar todas as categorias da classificação de idade:

```
https://apisidra.ibge.gov.br/values/t/9514/n6/all/c287/all
```

a API retorna o erro:

```
Quantidade de valores solicitados: 746380 excedeu o limite: 50000
```

O limite operacional da API impede a extração completa em uma única requisição.

---

## Alternativas avaliadas

### Opção 1

Extrair todas as idades individuais (0 até 100+).

**Vantagens**

- Máxima granularidade.

**Desvantagens**

- Aproximadamente 746 mil registros.
- Excede o limite da API.
- Grande número de requisições.
- Complexidade desnecessária para o objetivo do projeto.

---

### Opção 2

Extrair apenas os grupos quinquenais (5 em 5 anos).

Exemplo:

- 0 a 4 anos
- 5 a 9 anos
- 10 a 14 anos
- ...
- 95 a 99 anos
- 100 anos ou mais

**Vantagens**

- Aproximadamente 22 categorias.
- Requisições pequenas.
- Não excede o limite da API.
- Modelo adequado para análises de varejo.

**Desvantagens**

- Perde a granularidade por idade individual.

---

## Decisão

A tabela 9514 será extraída utilizando apenas as faixas etárias agregadas (grupos quinquenais).

Cada faixa etária será consultada individualmente através da API do SIDRA.

Após a extração, todos os resultados serão consolidados em uma única tabela Bronze.

A classificação Sexo será expandida utilizando:

```
c2/all
```

A classificação Idade será consultada utilizando apenas os códigos correspondentes aos grupos quinquenais.

---

## Justificativa

O objetivo do projeto é apoiar análises de expansão de varejo.

Para esse cenário, indicadores como:

- população jovem;
- população economicamente ativa;
- população idosa;
- distribuição por sexo;

são mais relevantes do que a população em cada idade individual.

A utilização de grupos quinquenais reduz significativamente o volume de dados sem perda relevante para os casos de uso previstos.

Além disso, essa abordagem respeita as limitações operacionais da API SIDRA e simplifica o processamento nas camadas Bronze, Silver e Gold.

---

## Impacto

A Bronze armazenará dados no formato:

| Município | Ano | Sexo | Faixa Etária | População |
|------------|------|--------|----------------|------------|

Esse modelo facilitará a construção de indicadores demográficos utilizados na priorização de municípios para expansão de lojas e demais análises do projeto Retail Intelligence Brasil.

---

## Evidências

Spike realizado:

- 99_spike_sidra_9514

Principais validações:

- consumo da API;
- descoberta das classificações;
- expansão da classificação Sexo;
- validação do limite de 50.000 registros da API;
- definição da estratégia de particionamento por grupos etários.