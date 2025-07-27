# Pipeline de ETL para Análise de Criminalidade Urbana

## Objetivo do Projeto

O principal objetivo deste projeto é ranquear e compreender o desenvolvimento da segurança pública nas cidades de **Santana de Parnaíba**, **Barueri** e **Cajamar**, com base em dados oficiais da SSP-SP. Essas três cidades possuem uma origem histórica comum — todas já fizeram parte de um único município: **Santana de Parnaíba**. Ao analisar sua evolução individual após a emancipação administrativa, o projeto busca responder:

- Como cada cidade tem se desenvolvido em termos de segurança?
- Qual delas apresenta melhor desempenho ao longo dos anos?
- Existem padrões sazonais ou estruturais que influenciam os indicadores de criminalidade?

## Sumário Executivo

- Santana de Parnaíba se destaca como a cidade mais segura entre as três analisadas
- Taxa de crimes por 100 mil habitantes: 50% menor que Cajamar e Barueri
- Santana e Cajamar apresentam sazonalidade
- Metodologia replicável para outros municípios
- Dados históricos desde 2022

## Metodologia

### 1. Extração de Dados (E - Extract)
- **Fonte**: Portal da SSP-SP (Secretaria de Segurança Pública de São Paulo)
- **Tecnologias**:
  - Python (VSCode)
  - Selenium para automação no Google Chrome
- **Processo**:
  - Download automático de relatórios mensais
  - Armazenamento temporário em pasta `temp/Documentos`

### 2. Transformação de Dados (T - Transform)
- **Bibliotecas**: pandas
- **Etapas**:
  - Consolidação de arquivos CSV em único DataFrame
  - Padronização de formatos (tabelas, datas)
  - Enriquecimento com metadados (nome do município, totais)
  - Limpeza de dados faltantes (missing values)

### 3. Carga de Dados (L - Load)
- **Destino**: Google Sheets
- **Integração**: API do Google Cloud Platform (GCP)
- **Vantagens**: Acesso remoto e atualização em tempo real

### 4. Análise Exploratória de Dados (EDA)
- **Ambiente**: Jupyter Notebook (Google Colab)
- **Principais análises**:
  - Comparação intermunicipal (volumes históricos)
  - Normalização por população (IBGE Censo 2022)
  - Identificação de sazonalidade

### 5. Visualização e Dashboard
- **Ferramenta**: Power BI
- **Componentes**:
  - Série temporal (evolução mensal)
  - Mapa geográfico
  - Hierarquia de crimes (gráfico de funil)
  - Comparação direta entre cidades

#### Dashboard Interativo
![Dashboard de Criminalidade](https://github.com/user-attachments/assets/b6c29bf3-3a15-4029-abf1-fcf9f7c40d96)

*Visualização completa dos dados de criminalidade - atualizado Julho/2025*

## Principais Resultados
- Barueri apresenta o dobro de ocorrências comparado às outras cidades
- Santana de Parnaíba: 50% mais segura que as demais (taxa por 100k hab.)
- Padrões de sazonalidade identificados (especialmente em Cajamar, a qual apresenta picos no mês de maio, e Santana de Parnaíba)

## Próximos Passos
- Implementação de modelo ARIMA para análise preditiva
- Expansão para outras cidades da região

## Fontes de Dados
- **Primária**: SSP-SP (2021-2024)
- **Secundária**: IBGE (Censo 2022)

## Conclusão
O projeto demonstra a eficácia de pipelines de ETL para:
- Fornecer insights sobre segurança pública
- Identificar padrões e tendências
- Suportar políticas públicas baseadas em dados
- Democratizar o acesso à informação

**Destaque**: Metodologia replicável para outras regiões do Brasil.
