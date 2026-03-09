# 🌱 FarmTech Solutions - Sistema de Gestão Agrícola Digital

> **Projeto Acadêmico FIAP** - Agricultura Digital e Inovação Tecnológica

Sistema completo para gestão de culturas agrícolas, desenvolvido em Python e R, com funcionalidades de cálculo de área, manejo de insumos e análise estatística de dados.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Instalar e Rodar](#-como-instalar-e-rodar)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação no Windows](#instalação-no-windows)
  - [Instalação no macOS](#instalação-no-macos)
  - [Instalação no Linux](#instalação-no-linux)
- [Como Usar o Sistema](#-como-usar-o-sistema)
- [Requisitos do Projeto](#-requisitos-do-projeto)
- [Equipe](#-equipe)

---

## 🎯 Sobre o Projeto

Este projeto foi desenvolvido para a **FarmTech Solutions**, uma startup fictícia que trabalha com inovação em agricultura digital. O sistema auxilia fazendas a:

- Gerenciar diferentes tipos de culturas (Café e Soja)
- Calcular áreas de plantio usando geometria
- Planejar o uso de insumos agrícolas (fertilizantes, pesticidas)
- Analisar estatísticas de produção
- Consultar dados meteorológicos para tomada de decisão

---

## ⚡ Funcionalidades

### Aplicação Python (`main.py`)

✅ **Gestão de 2 Culturas:**
- ☕ Café (área circular)
- 🌾 Soja (área retangular)

✅ **Funcionalidades do Menu:**
1. **Entrada de Dados** - Adicionar novas culturas
2. **Saída de Dados** - Visualizar todas as culturas cadastradas
3. **Atualização de Dados** - Modificar registros existentes
4. **Deleção de Dados** - Remover registros
5. **Sair** - Exportar dados automaticamente

✅ **Cálculos Automáticos:**
- Área de plantio (circular ou retangular)
- Quantidade de insumos necessários (em litros)
- Estimativas baseadas no número de ruas e comprimento

### Aplicação R (`statistics_analysis.R`)

📊 **Análise Estatística:**
- Média e desvio padrão
- Valores mínimos e máximos
- Mediana e variância
- Análise por tipo de cultura
- Insights sobre área total cultivada

### Script R Bônus (`weather_api.R`)

🌦️ **Dados Meteorológicos:**
- Clima atual (temperatura, umidade, vento)
- Previsão de 7 dias
- Recomendações agrícolas baseadas no clima
- Integração com API Open-Meteo (gratuita)

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão Recomendada | Finalidade |
|------------|-------------------|------------|
| Python | 3.8 ou superior | Aplicação principal |
| R | 4.0 ou superior | Análise estatística |
| Git | Qualquer versão | Versionamento |

**Pacotes R necessários:** `jsonlite`, `httr` (instalados automaticamente)

---

## 📁 Estrutura do Projeto

```
farmtech-solutions/
├── src/
│   ├── python/
│   │   └── main.py              # Aplicação principal em Python
│   └── r/
│       ├── statistics_analysis.R # Análise estatística
│       └── weather_api.R         # API meteorológica (bônus)
├── data/
│   └── crop_data.csv            # Dados exportados (gerado automaticamente)
├── README.md                    # Este arquivo
├── LICENSE                      # Licença do projeto
└── .gitignore                   # Arquivos ignorados pelo Git
```

---

## 🚀 Como Instalar e Rodar

### Pré-requisitos

Antes de começar, você precisa ter instalado na sua máquina:
1. **Python 3** (linguagem de programação)
2. **R** (linguagem para estatística)
3. **Git** (para baixar o projeto)

---

### Instalação no Windows

#### **Passo 1: Instalar Python**

1. Acesse: https://www.python.org/downloads/
2. Clique em **"Download Python"** (versão 3.x)
3. Execute o instalador
4. ⚠️ **IMPORTANTE:** Marque a opção **"Add Python to PATH"** antes de instalar
5. Clique em **"Install Now"**
6. Aguarde a instalação

**Verificar instalação:**
```cmd
python --version
```
Deve aparecer algo como: `Python 3.11.0`

#### **Passo 2: Instalar R**

1. Acesse: https://cran.r-project.org/bin/windows/base/
2. Clique em **"Download R for Windows"**
3. Execute o instalador
4. Aceite todas as opções padrão
5. Clique em **"Avançar"** até finalizar

**Verificar instalação:**
```cmd
Rscript --version
```

#### **Passo 3: Instalar Git**

1. Acesse: https://git-scm.com/download/win
2. Execute o instalador
3. Aceite todas as opções padrão
4. Clique em **"Next"** até finalizar

**Verificar instalação:**
```cmd
git --version
```

#### **Passo 4: Baixar o Projeto**

1. Abra o **Prompt de Comando** (CMD):
   - Pressione `Windows + R`
   - Digite `cmd` e pressione Enter

2. Navegue até a pasta onde quer salvar o projeto:
```cmd
cd C:\Users\SeuNome\Documents
```

3. Clone o projeto:
```cmd
git clone https://github.com/SEU_USUARIO/farmtech-solutions.git
cd farmtech-solutions
```

---

### Instalação no macOS

#### **Passo 1: Instalar Homebrew (gerenciador de pacotes)**

1. Abra o **Terminal** (Cmd + Espaço, digite "Terminal")
2. Cole este comando:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Pressione Enter e aguarde

#### **Passo 2: Instalar Python, R e Git**

```bash
brew install python
brew install r
brew install git
```

**Verificar instalações:**
```bash
python3 --version
Rscript --version
git --version
```

#### **Passo 3: Baixar o Projeto**

```bash
cd ~/Documents
git clone https://github.com/SEU_USUARIO/farmtech-solutions.git
cd farmtech-solutions
```

---

### Instalação no Linux (Ubuntu/Debian)

#### **Passo 1: Atualizar o sistema**

```bash
sudo apt update
sudo apt upgrade
```

#### **Passo 2: Instalar Python, R e Git**

```bash
sudo apt install python3 python3-pip
sudo apt install r-base
sudo apt install git
```

**Verificar instalações:**
```bash
python3 --version
Rscript --version
git --version
```

#### **Passo 3: Baixar o Projeto**

```bash
cd ~/Documents
git clone https://github.com/SEU_USUARIO/farmtech-solutions.git
cd farmtech-solutions
```

---

## 📖 Como Usar o Sistema

### 1️⃣ Executar a Aplicação Python

#### **Windows (CMD):**
```cmd
cd C:\Users\SeuNome\Documents\farmtech-solutions\src\python
python main.py
```

#### **macOS/Linux (Terminal):**
```bash
cd ~/Documents/farmtech-solutions/src/python
python3 main.py
```

**O que fazer:**
1. Aparecerá um menu com 5 opções
2. Digite `1` para adicionar uma cultura
3. Siga as instruções na tela
4. Adicione pelo menos 3-5 registros (para análise estatística)
5. Digite `5` para sair (os dados serão exportados automaticamente)

---

### 2️⃣ Executar a Análise Estatística em R

#### **Windows (CMD):**
```cmd
cd C:\Users\SeuNome\Documents\farmtech-solutions\src\r
Rscript statistics_analysis.R
```

#### **macOS/Linux (Terminal):**
```bash
cd ~/Documents/farmtech-solutions/src/r
Rscript statistics_analysis.R
```

**O que vai acontecer:**
- O script vai ler o arquivo `crop_data.csv` gerado pelo Python
- Vai calcular médias, desvios padrão e outras estatísticas
- Vai mostrar análises por tipo de cultura
- Tudo será exibido no terminal

---

### 3️⃣ Executar API Meteorológica (Bônus)

#### **Windows (CMD):**
```cmd
cd C:\Users\SeuNome\Documents\farmtech-solutions\src\r
Rscript weather_api.R
```

#### **macOS/Linux (Terminal):**
```bash
cd ~/Documents/farmtech-solutions/src/r
Rscript weather_api.R
```

**O que fazer:**
1. O script vai instalar os pacotes necessários automaticamente
2. Escolha uma cidade da lista ou digite coordenadas
3. Aguarde os dados meteorológicos aparecerem
4. Veja recomendações agrícolas baseadas no clima

---

## 📝 Requisitos do Projeto

### ✅ Implementado

- [x] a. Suporte a 2 tipos de culturas (Café e Soja)
- [x] b. Cálculo de área de plantio (circular e retangular)
- [x] c. Cálculo de manejo de insumos (com quantidade por metro)
- [x] d. Dados organizados em vetores (listas Python)
- [x] e. Menu com 5 opções:
  - [x] Entrada de dados
  - [x] Saída de dados
  - [x] Atualização de dados
  - [x] Deleção de dados
  - [x] Sair do programa
- [x] f. Uso de loops e estruturas de decisão
- [x] g. Aplicação R com estatísticas (média, desvio padrão)
- [x] h. Uso do GitHub para versionamento
- [x] **BÔNUS:** API meteorológica em R

--- 

## 🔧 Solução de Problemas

### Problema: "Python não é reconhecido como comando"

**Solução Windows:**
1. Pesquise "Variáveis de Ambiente" no menu Iniciar
2. Clique em "Variáveis de Ambiente"
3. Em "Path", adicione: `C:\Users\SeuNome\AppData\Local\Programs\Python\Python3X`
4. Reinicie o CMD

### Problema: "Arquivo crop_data.csv não encontrado" no R

**Solução:**
- Você precisa executar o Python PRIMEIRO
- Adicionar dados e sair do programa (opção 5)
- Só então executar o script R

### Problema: Erro ao instalar pacotes R

**Solução:**
```r
install.packages("jsonlite", repos = "https://cloud.r-project.org/")
install.packages("httr", repos = "https://cloud.r-project.org/")
```

---

## 👥 Equipe

- **Integrante 1:** Larissa Sthefanny G. Trigueiro - RM[rm570065]
- **Integrante 2:** Georgia - RM[]
- **Integrante 3:** Carlos Amaral - RM[]
- **Integrante 4:** Daniel A. - RM[]

---

## 📚 Referências

- EMBRAPA - Agricultura de Precisão
- Open-Meteo API: https://open-meteo.com
- Python Documentation: https://docs.python.org
- R Documentation: https://www.r-project.org

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
