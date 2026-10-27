# SalesInsight PY — Análise de Vendas com Python

## 1. Sobre o projeto

O SalesInsight PY é um mini-projeto de análise de dados de vendas desenvolvido em Python. Seu objetivo é organizar, limpar e analisar dados comerciais, gerando indicadores de receita por categoria, região e cliente.

O projeto utiliza bibliotecas da biblioteca padrão do Python, como `csv`, `json` e `random`, sem depender do Pandas.

## 2. Objetivos

- Gerar um conjunto de dados fictícios de vendas.
- Inspecionar os registros e identificar campos vazios.
- Limpar os dados e converter os tipos necessários.
- Calcular a receita total de cada venda.
- Classificar as vendas por faixa de receita.
- Calcular receitas por categoria, região e no total geral.
- Segmentar clientes de acordo com o gasto acumulado.
- Exportar os resultados para arquivos CSV e JSON.

## 3. Tecnologias utilizadas

- Python 3
- Módulo `csv`
- Módulo `json`
- Módulo `random`
- Módulo `pathlib`
- Git e GitHub
- Visual Studio Code

## 4. Estrutura do projeto

```text
Mini_Projeto_Modulo_01/
├── main.py
├── modulo_vendas.py
├── vendas.csv
├── README.md
└── outputs/
    ├── metricas_resumo.csv
    └── estatisticas.json
```

## 5. Como executar

### Pré-requisitos

- Python 3 instalado.
- Projeto aberto no Visual Studio Code.

### Execução

No terminal, dentro da pasta do projeto, execute:

```powershell
py main.py
```
Durante a execução, o programa realiza as seguintes etapas:

1. Gera um conjunto de dados fictícios de vendas com 120 registros.
2. Inspeciona os dados e identifica campos vazios.
3. Remove registros com campos vazios ou valores inválidos e converte os tipos necessários.
4. Calcula a receita total e classifica as vendas por faixa de receita.
5. Consolida as receitas por categoria, região e no total geral.
6. Segmenta os clientes de acordo com o gasto acumulado.
7. Exporta os resultados para os arquivos CSV e JSON na pasta `outputs/`.

## 6. Regras de análise

### Faixas de preço

A classificação das vendas utiliza a receita total, calculada pela multiplicação da quantidade pelo preço unitário:

- **Baixo:** receita inferior a R$ 500.
- **Médio:** receita de R$ 500 até R$ 2.000, inclusive.
- **Alto:** receita superior a R$ 2.000.

### Segmentação de clientes

Os clientes são classificados de acordo com o gasto acumulado:

- **Bronze:** gasto inferior a R$ 3.000.
- **Prata:** gasto de R$ 3.000 até R$ 8.000, inclusive.
- **Ouro:** gasto superior a R$ 8.000.

## 7. Arquivos de saída

### `outputs/metricas_resumo.csv`

Armazena as receitas agrupadas por categoria e região, além da receita geral.

### `outputs/estatisticas.json`

Armazena as receitas por categoria e região, a receita geral, a quantidade de clientes e os dados da segmentação de clientes.

## 8. Observações

Os dados de vendas são fictícios e gerados aleatoriamente para fins educacionais. Por isso, os valores das receitas e os resultados das análises podem variar a cada execução.

## 9. Controle de versão

O projeto utiliza Git para registrar a evolução do desenvolvimento e GitHub para armazenar o repositório remoto.

## 10. Autor

Projeto desenvolvido como atividade prática da Trilha de Inteligência Artificial, no módulo de Fundamentos de Dados, Programação e Análise Preditiva com Python.
