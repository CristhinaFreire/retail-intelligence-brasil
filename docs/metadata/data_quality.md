# Qualidade dos Dados

Este documento descreve as validações de qualidade aplicadas durante a ingestão de dados na plataforma Retail Intelligence Brasil.

O objetivo é garantir que apenas dados íntegros e rastreáveis sejam persistidos na camada Bronze.

---

# Objetivos

As validações de qualidade buscam assegurar:

- Disponibilidade da fonte de dados.
- Integridade dos arquivos recebidos.
- Consistência da estrutura dos dados.
- Rastreabilidade das cargas.
- Possibilidade de reprocessamento.

---

# Validações da Landing

Durante a etapa de download dos dados são executadas as seguintes validações.

| Validação | Descrição |
|-----------|-----------|
| Disponibilidade da API | Verifica se a fonte oficial está acessível. |
| Status HTTP | Confirma retorno HTTP 200. |
| Resposta JSON | Verifica se a resposta está em formato JSON válido. |
| Quantidade de registros | Registra a quantidade de registros retornados pela API. |
| Persistência | Confirma o armazenamento do arquivo JSON na Landing. |

---

# Validações da Bronze

Na carga para a Bronze são executadas validações antes da persistência das tabelas Delta.

| Validação | Descrição |
|-----------|-----------|
| Leitura do JSON | Confirma a leitura dos arquivos da Landing. |
| Criação do DataFrame | Valida a conversão para Spark DataFrame. |
| Schema | Inspeciona a estrutura dos dados antes da gravação. |
| Escrita Delta | Confirma a criação ou atualização da tabela Delta. |
| Consulta da tabela | Permite validar o conteúdo carregado após a persistência. |

---

# Fontes Implementadas

Atualmente as validações são aplicadas às seguintes entidades da API de Localidades do IBGE:

- Estados
- Municípios
- Regiões
- Regiões Intermediárias
- Regiões Imediatas

---

# Tratamento de Erros

Quando ocorre uma falha durante a ingestão, o pipeline é interrompido e uma exceção é lançada.

As principais situações tratadas são:

- Erro de conexão com a API.
- Status HTTP diferente de 200.
- Falha na leitura do JSON.
- Erro na criação do DataFrame Spark.
- Erro na gravação da tabela Delta.

Esse comportamento evita a persistência de dados incompletos ou inconsistentes.

---

# Evolução Planejada

As próximas versões da plataforma poderão incorporar validações adicionais, como:

- Verificação de registros duplicados.
- Validação de chaves primárias.
- Comparação de schemas entre cargas.
- Monitoramento automático da qualidade.
- Regras de completude dos dados.
- Métricas de qualidade por pipeline.