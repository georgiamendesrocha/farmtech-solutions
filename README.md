# FarmTech Solutions - Agricultura Digital

Projeto acadêmico desenvolvido para a FIAP com foco em agricultura digital, usando Python e R.

## Objetivo do projeto

A aplicação permite:
- cadastrar duas culturas agrícolas: **Café** e **Soja**;
- calcular a área de plantio conforme a figura geométrica escolhida para cada cultura;
- calcular o manejo de insumos com base em número de ruas, comprimento das ruas e quantidade aplicada por metro;
- armazenar os dados em vetores/listas;
- atualizar, visualizar e deletar registros;
- exportar os dados para CSV;
- analisar estatísticas básicas em R;
- consultar dados meteorológicos via API pública usando R.

## Tecnologias utilizadas

- Python 3
- R
- Open-Meteo API
- Git/GitHub

## Estrutura do projeto

```text
farmtech-solutions/
├── src/
│   ├── python/
│   │   ├── main.py
│   │   └── test_functions.py
│   └── r/
│       ├── statistics_analysis.R
│       └── weather_api.R
├── data/
│   ├── crop_data.csv
│   └── crop_data_example.csv
├── docs/
│   ├── article_summary.md
│   └── video_link.txt
├── README.md
├── QUICK_START.md
├── GIT_GUIDE.md
├── CHECKLIST.md
├── LICENSE
└── test_setup.sh
```

## Requisitos do enunciado atendidos

### Python
- 2 culturas: Café e Soja
- cálculo de área circular e retangular
- cálculo de manejo de insumos
- uso de vetores/listas
- menu com entrada, saída, atualização, deleção e saída do programa
- uso de estruturas de decisão e repetição

### R
- cálculo de média e desvio padrão
- estatísticas adicionais: mediana, mínimo, máximo e variância
- leitura do CSV exportado pela aplicação Python
- uso de API meteorológica pública

## Como executar

### 1. Aplicação Python

No terminal:

```bash
cd src/python
python main.py
```

### 2. Testes da aplicação Python

```bash
cd src/python
python test_functions.py
```

### 3. Análise estatística em R

Depois de cadastrar dados no Python e sair do programa:

```bash
cd src/r
Rscript statistics_analysis.R
```

### 4. Consulta meteorológica em R

```bash
cd src/r
Rscript weather_api.R
```

## Formato do CSV exportado

```csv
crop_type,area_shape,area_m2,rows,row_length_m,input_product,input_amount_ml_per_m,total_input_liters
Coffee,Circular,7853.98,50,100.00,Phosphate,500.00,2500.00
Soybean,Rectangular,10000.00,80,120.00,Herbicide,300.00,2880.00
```

## Integrantes

- Daniel Abreu dos Santos
- Carlos Magnus Costa Amaral
- Georgia Mendes Rocha
- Larissa Sthefanny Guedes Trigueiro

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE`.
