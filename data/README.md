# Data Directory

Esta pasta contém os dados do projeto FarmTech Solutions.

## Estrutura:

- **crop_data.csv** - Dados gerados pela aplicação Python (criado automaticamente ao sair do programa)
- **examples/** - Arquivos de exemplo para teste

## Como funciona:

1. Execute `src/python/main.py`
2. Adicione culturas pelo menu
3. Saia do programa (opção 5)
4. O arquivo `crop_data.csv` será gerado aqui automaticamente

## Formato do CSV:

```csv
crop_type,area_m2,rows,input_product,input_amount_ml_per_m
Coffee,7853.98,50,Phosphate,500.00
Soybean,10000.00,80,Herbicide,300.00
```

Este arquivo é lido pelos scripts R para análise estatística.
