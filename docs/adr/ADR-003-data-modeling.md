# ADR-003 - Padrões de Modelagem de Dados

## Status

Aceito

---

## Data

14/07/2026

---

## Contexto

O projeto Retail Intelligence Brasil será composto por diversas fontes de dados públicas brasileiras, incluindo informações demográficas, econômicas, geográficas, empresariais e de mercado.

Essas fontes possuem diferentes granularidades, formatos e chaves naturais.

Era necessário definir um padrão único de modelagem que garantisse integração entre domínios, facilidade de manutenção e consistência ao longo da evolução da plataforma.

---

# Decisão

A plataforma adotará Modelagem Dimensional como padrão para a camada Silver e Gold.

A modelagem seguirá principalmente os conceitos propostos por Ralph Kimball, utilizando dimensões e fatos para organizar os dados analíticos.

---

# Arquitetura de Modelagem

```
Bronze

↓

Silver

↓

Dimensões
Fatos

↓

Gold

↓

Produtos Analíticos
```

---

# Camada Bronze

A camada Bronze armazenará os dados exatamente como disponibilizados pelas fontes oficiais.

Não existirão regras de negócio nesta camada.

As tabelas Bronze servirão como histórico da origem dos dados.

---

# Camada Silver

A camada Silver será responsável pela criação do modelo dimensional.

Ela conterá principalmente:

- Dimensões
- Fatos
- Tabelas auxiliares

---

# Camada Gold

A camada Gold conterá apenas produtos analíticos.

Exemplos:

- Indicadores
- Data Marts
- Agregações
- Modelos para BI
- Bases para Ciência de Dados

---

# Convenções de Nomenclatura

## Dimensões

Todas as dimensões deverão iniciar com:

```
dim_
```

Exemplos

```
dim_estado

dim_municipio

dim_cnae

dim_empresa
```

---

## Fatos

Todas as tabelas fato deverão iniciar com:

```
fato_
```

Exemplos

```
fato_populacao

fato_emprego

fato_pib
```

---

## Indicadores

Os produtos analíticos deverão iniciar com:

```
indicador_
```

Exemplos

```
indicador_expansao

indicador_potencial_consumo
```

---

# Chaves Naturais

Sempre que existir um identificador oficial da fonte, ele deverá ser preservado.

Exemplos

| Domínio | Chave Natural |
|----------|---------------|
| Município | Código IBGE |
| Estado | Código UF |
| Empresa | CNPJ |
| CNAE | Código CNAE |

As chaves naturais nunca deverão ser descartadas.

---

# Chaves Substitutas

Surrogate Keys poderão ser utilizadas quando necessário para otimizar relacionamentos ou manter histórico.

Mesmo quando existirem, a chave natural continuará disponível na tabela.

---

# Relacionamentos

Sempre que possível os relacionamentos deverão utilizar códigos oficiais.

Exemplo

Correto

```
Municipio_IBGE = 4305108
```

Evitar

```
Nome do Município = Porto Alegre
```

Descrições podem mudar.

Códigos oficiais permanecem estáveis.

---

# Granularidade

Toda tabela deverá possuir uma granularidade claramente definida.

Exemplo

```
dim_estado

1 linha por Estado
```

```
dim_municipio

1 linha por Município
```

```
fato_populacao

1 linha por Município e Ano
```

---

# Integração entre Fontes

O Código IBGE do Município será a principal chave de integração entre diferentes fontes públicas.

Exemplo

```
IBGE
      │
      ▼
dim_municipio
      ▲
      │
Receita Federal

      ▲
      │
CAGED

      ▲
      │
RAIS

      ▲
      │
DATASUS

      ▲
      │
Banco Central
```

---

# Tipos de Dados

Sempre que possível utilizar:

| Tipo | Utilização |
|-------|------------|
| Integer | Identificadores |
| Long | Grandes identificadores |
| Decimal | Valores monetários |
| Date | Datas |
| Timestamp | Auditoria |
| Boolean | Flags |

Evitar armazenar números como String.

---

# Nulls

Valores nulos deverão ser tratados na camada Silver.

A camada Bronze preservará exatamente o dado original.

---

# Histórico

Sempre que necessário preservar histórico, utilizar técnicas apropriadas para Slowly Changing Dimensions (SCD).

A escolha da estratégia será documentada em ADR específica.

---

# Objetivos

A padronização da modelagem busca garantir:

- consistência;
- integração entre fontes;
- facilidade de manutenção;
- governança;
- escalabilidade;
- reutilização.

---

# Consequências

## Positivas

- Modelo consistente.
- Facilidade para integração de novas fontes.
- Menor acoplamento entre pipelines.
- Melhor desempenho analítico.
- Organização padronizada.

## Negativas

- Maior esforço inicial de modelagem.
- Necessidade de documentação contínua.

---

# Referências

- Ralph Kimball – The Data Warehouse Toolkit
- Databricks Lakehouse Architecture
- Delta Lake Documentation
- Microsoft Dimensional Modeling Guidance