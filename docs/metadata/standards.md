# Padrões de Desenvolvimento

Este documento define os padrões adotados para desenvolvimento, organização e manutenção da plataforma Retail Intelligence Brasil.

---

# Arquitetura

A plataforma segue a arquitetura Lakehouse utilizando o padrão Medallion.

```
Landing
    ↓
Bronze
    ↓
Silver
    ↓
Gold
```

Todas as novas integrações devem seguir esse fluxo.

---

# Estrutura dos Pipelines

Cada entidade deverá possuir dois notebooks para ingestão inicial.

```
01_download_<entidade>

02_bronze_<entidade>
```

Quando implementadas as próximas camadas, deverão ser utilizados:

```
03_silver_<entidade>

04_gold_<produto>
```

---

# Estrutura dos Notebooks

Todos os notebooks devem seguir a mesma organização.

```
1. Imports

2. Configuração

3. Extração

4. Validação

5. Persistência

6. Inspeção

7. Encerramento
```

Cada etapa deve possuir comentários padronizados para facilitar manutenção e leitura.

---

# Landing

Os dados extraídos das fontes oficiais devem ser armazenados inicialmente na Landing.

Características:

- Arquivos originais.
- Sem transformações.
- Formato JSON.
- Organização por fonte e entidade.
- Persistência em Volumes do Unity Catalog.

---

# Bronze

A camada Bronze deve:

- Ler exclusivamente os arquivos da Landing.
- Preservar a estrutura original da fonte.
- Não aplicar regras de negócio.
- Persistir os dados em Delta Lake.

---

# Silver

A camada Silver será responsável por:

- Limpeza.
- Padronização.
- Integração.
- Enriquecimento.
- Deduplicação.

---

# Gold

A camada Gold disponibilizará produtos analíticos.

Exemplos:

- Dimensões.
- Fatos.
- Indicadores.
- Data Marts.

---

# Convenções de Código

Todos os notebooks devem:

- Utilizar Python e Apache Spark.
- Possuir cabeçalho padronizado.
- Utilizar comentários por seção.
- Utilizar variáveis com nomes descritivos.
- Utilizar `snake_case`.
- Evitar valores fixos no código.
- Centralizar configurações no início do notebook.

---

# Tratamento de Erros

Sempre que aplicável, os pipelines devem:

- Validar a resposta da fonte.
- Interromper a execução em caso de erro.
- Exibir mensagens claras de execução.
- Evitar persistência de dados inconsistentes.

---

# Logging

Todos os notebooks devem registrar:

- Início da execução.
- Fonte consumida.
- Quantidade de registros.
- Caminho de persistência.
- Finalização da carga.

---

# Governança

Todos os ativos devem:

- Ser versionados no Git.
- Possuir documentação.
- Seguir o padrão de nomenclatura definido pelo projeto.
- Manter rastreabilidade entre origem e destino dos dados.

---

# Tecnologias

A plataforma utiliza:

- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog
- Python
- SQL
- Git
- GitHub