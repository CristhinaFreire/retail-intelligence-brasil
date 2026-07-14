# ADR-004 — Estratégia de Extração da Tabela SIDRA 9514

## Status

Aceito

---

## Contexto

A tabela SIDRA 9514 (População residente por sexo, idade e forma de declaração da idade) foi selecionada para compor a camada Bronze do projeto Retail Intelligence Brasil.

Durante a fase de pesquisa (Spikes Técnicos) foram realizados testes de consumo da API do SIDRA para compreender sua estrutura, parâmetros de consulta e limitações operacionais.

Foram identificadas as seguintes classificações da tabela:

| Classificação | Código |
|---------------|--------|
| Sexo | C2 |
| Grupo de idade | C287 |
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

Ao solicitar todas as categorias da classificação Grupo de idade:

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

Realizar o particionamento utilizando os grupos etários.

Exemplo:

- 0 a 4 anos
- 5 a 9 anos
- 10 a 14 anos
- ...
- 95 a 99 anos
- 100 anos ou mais

**Vantagens**

- Requisições menores.
- Não excede o limite da API.
- Processo escalável.
- Mantém nível de detalhamento adequado para análises demográficas e de varejo.

**Desvantagens**

- Necessidade de consolidar múltiplas respostas da API.

---

## Decisão

A classificação Sexo será expandida utilizando:

```
c2/all
```

A classificação Grupo de idade (C287) será utilizada como estratégia de particionamento da extração.

Serão realizadas 21 requisições, uma para cada grupo etário.

Após a conclusão das requisições, todos os resultados serão consolidados em um único conjunto de dados antes da persistência na Landing e na Bronze.

---

## Justificativa

O objetivo do projeto é apoiar análises de expansão do varejo.

Para esse cenário, indicadores como:

- distribuição da população por sexo;
- população economicamente ativa;
- envelhecimento populacional;
- concentração de faixas etárias;

são mais relevantes do que a população por idade individual.

A utilização dos grupos etários reduz significativamente o volume de dados sem perda relevante para os casos de uso previstos.

Além disso, essa estratégia respeita as limitações da API SIDRA, simplifica a implementação e poderá ser reutilizada em futuras tabelas multidimensionais.

---

## Arquitetura da solução

A implementação segue o fluxo abaixo:

```
API SIDRA
        │
        ▼
21 requisições (uma por grupo etário)
        │
        ▼
Consolidação em memória
        │
        ▼
Arquivo JSON único na Landing
        │
        ▼
Leitura pelo Spark
        │
        ▼
Persistência RAW na Bronze (Delta)
```

Essa abordagem mantém o padrão arquitetural utilizado pelos demais notebooks de ingestão do projeto, preservando um único arquivo JSON por execução e uma Bronze no formato RAW.

---

## Impacto

A Bronze armazenará os dados preservando exatamente a estrutura retornada pela API do SIDRA.

As transformações semânticas, renomeação de colunas, conversão de tipos e regras de negócio serão realizadas posteriormente na camada Silver.

Essa decisão mantém a Bronze aderente ao padrão RAW adotado no projeto.

---

## Evidências

### Spikes realizados

- 99_spike_sidra_api
- 99_spike_sidra_classificacoes
- 99_spike_sidra_9514

### Validações realizadas

- consumo da API SIDRA;
- identificação das classificações da tabela 9514;
- validação dos parâmetros `c` e `d`;
- expansão da classificação Sexo (`c2/all`);
- validação do limite de aproximadamente 50.000 registros por requisição;
- definição da estratégia de particionamento por grupos etários;
- consolidação das respostas em um único conjunto de dados;
- persistência do JSON na Landing;
- persistência RAW na Bronze.