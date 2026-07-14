# ADR-006 — Utilização de Classificações na API SIDRA

## Status

Aceito

---

## Contexto

Durante a implementação das integrações com a API do SIDRA foi identificado que diversas tabelas possuem dimensões adicionais denominadas **Classificações**.

Essas classificações permitem detalhar os indicadores por diferentes categorias, como:

- sexo;
- faixa etária;
- cor ou raça;
- escolaridade;
- situação do domicílio;
- entre outras.

Foi necessário compreender como consultar essas dimensões de forma padronizada.

---

## Problema

A consulta padrão da API retorna apenas os valores agregados da tabela.

Para obter detalhamentos é necessário informar explicitamente as classificações desejadas.

Sem essa parametrização, parte importante das informações estatísticas permanece agregada e indisponível para análises.

---

## Decisão

Todas as classificações da API SIDRA serão consultadas utilizando os parâmetros oficiais:

```
c{codigo_classificacao}
```

e

```
d{codigo_categoria}
```

Sempre que necessário, será utilizada a expansão completa das categorias por meio do parâmetro:

```
c{codigo}/all
```

---

## Estrutura

O padrão da API é:

```
/c{classificacao}/{categoria}
```

Exemplos:

```
c2/all
```

Retorna todas as categorias da classificação Sexo.

```
c287/all
```

Retorna todas as categorias da classificação Grupo de idade.

```
c286/all
```

Retorna todas as categorias da classificação Forma de declaração da idade.

Também é possível consultar categorias específicas:

```
c2/4
```

Homens.

```
c2/5
```

Mulheres.

Ou múltiplas categorias:

```
c2/4,5
```

Homens e Mulheres.

---

## Descoberta das classificações

Antes da implementação de qualquer notebook, deverão ser consultados os metadados da tabela.

Padrão utilizado:

```
https://apisidra.ibge.gov.br/desctabapi.aspx?c={codigo_tabela}
```

Essa consulta permite identificar:

- variáveis;
- classificações;
- categorias;
- níveis territoriais;
- período disponível;
- unidade de medida.

Essa etapa passou a fazer parte do processo de Spike Técnico para qualquer nova tabela SIDRA.

---

## Estratégia adotada

O fluxo padrão para novas tabelas será:

1. Identificar a tabela de interesse.
2. Consultar os metadados (`desctabapi.aspx`).
3. Identificar classificações disponíveis.
4. Avaliar quais classificações possuem valor analítico para o projeto.
5. Verificar limitações da API.
6. Implementar a estratégia de extração.

---

## Justificativa

A utilização das classificações amplia significativamente o potencial analítico dos dados disponibilizados pelo SIDRA.

Ao mesmo tempo, evita consultas desnecessariamente grandes, permitindo selecionar apenas as dimensões relevantes para cada caso de uso.

Além disso, a documentação dos metadados reduz erros de implementação e facilita futuras integrações.

---

## Impacto

Todos os novos notebooks SIDRA deverão iniciar pela análise dos metadados da tabela antes da implementação da extração.

Essa prática reduz retrabalho, facilita a identificação das dimensões disponíveis e padroniza o desenvolvimento das integrações.

---

## Evidências

Spikes realizados:

- 99_spike_sidra_classificacoes
- 99_spike_sidra_9514
- 99_spike_sidra_9515

Validações realizadas:

- utilização dos parâmetros `c` e `d`;
- expansão de categorias utilizando `all`;
- consulta aos metadados da API (`desctabapi.aspx`);
- identificação das classificações das tabelas SIDRA;
- aplicação das classificações na estratégia de ingestão.