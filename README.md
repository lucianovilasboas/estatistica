# 📊 Estatistica - Aplicativos Interativos de Estatística e Probabilidade

Bem-vindo ao repositório de aplicativos interativos para apoio à disciplina de **Estatística e Probabilidade** do curso de Tecnologia em Processos Gerenciais do IFMG - Campus Ponte Nova.

## 📖 Descrição do Projeto

Este projeto foi desenvolvido para facilitar o ensino e a aprendizagem dos conceitos fundamentais de estatística através de aplicativos interativos construídos com **Streamlit**. Os aplicativos permitem que os alunos manipulem dados, visualizem distribuições e entendam na prática conceitos abstratos da estatística.

## 🎯 Objetivo

Proporcionar uma forma prática e interativa de explorar os seguintes tópicos:
- Cálculos estatísticos básicos (média, mediana, moda, desvio padrão)
- Distribuições de probabilidade
- Intervalos de confiança
- Testes de hipóteses
- Correlação e regressão linear
- Simulações de eventos probabilísticos

---

## 🚀 Como Iniciar

### Pré-requisitos

- Python 3.9 ou superior
- Docker (opcional, para execução containerizada)

### Instalação Local

1. **Clone o repositório:**
   ```bash
   git clone <repository-url>
   cd estatistica
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   ```bash
   streamlit run Home.py
   ```

4. **Acesse a aplicação:**
   - A aplicação estará disponível em `http://localhost:8501`

### Instalação com Docker

1. **Construa a imagem Docker:**
   ```bash
   docker build -t estatistica .
   ```

2. **Execute o contêiner:**
   ```bash
   docker-compose up
   ```

3. **Acesse a aplicação:**
   - A aplicação estará disponível em `http://localhost:8503`

---

## 📦 Dependências

O projeto utiliza as seguintes bibliotecas Python:

| Biblioteca | Descrição |
|---|---|
| `streamlit` | Framework para criar aplicações web interativas |
| `numpy` | Computação numérica e arrays multidimensionais |
| `pandas` | Manipulação e análise de dados |
| `matplotlib` | Visualização de dados |
| `seaborn` | Visualização estatística de dados |
| `scipy` | Computação científica e estatística |
| `scikit-learn` | Machine learning e análise de dados |
| `plotly` | Gráficos interativos |
| `openpyxl` | Leitura/escrita de arquivos Excel |

---

## 📂 Estrutura do Projeto

```
estatistica/
├── Home.py                           # Página inicial da aplicação
├── estatistica.py                    # Script de exemplo com dados de alturas
├── dados_exmplos.py                  # Base de dados de exemplo (alturas masculinas e femininas)
├── distribuicao.py                   # Geração e visualização de distribuições
├── rtttl.py                          # Conversor de notações musicais (RTTTL)
├── requirements.txt                  # Dependências do projeto
├── Dockerfile                        # Configuração do Docker
├── docker-compose.yml                # Configuração do Docker Compose
├── README.md                         # Este arquivo
└── pages/                            # Páginas da aplicação Streamlit
    ├── 1_∑_Somatorium.py             # Cálculo de somatórios
    ├── 2_∑_Somatorium_xy.py          # Cálculo de somatório duplo (x*y)
    ├── 3_📑_Sumarização.py           # Sumarização de dados estatísticos
    ├── 4_📉_Histograma.py            # Geração de histogramas
    ├── 5_📐_Desvio Padrao.py         # Cálculo de desvio padrão e variância
    ├── 6_📐_Desvio Padrao 2.py       # Cálculo avançado de desvio padrão
    ├── 7_📐_Desvio Padrao 3.py       # Cálculo de desvio padrão (método 3)
    ├── 7_📐_Desvio Padrao 4.py       # Cálculo de desvio padrão (método 4)
    ├── 8_🎲_Lançamento.py            # Simulação de lançamento de dados e moedas
    ├── 9_🔢_Gerador.py               # Gerador de dados sintéticos
    ├── 10_🔍_Intervalo de Confiança.py      # Cálculo de intervalo de confiança
    ├── 11_🔍_Intervalo de Confiança 2.py    # Intervalo de confiança (método 2)
    ├── 12_🔍_Intervalo de Confiança 3.py    # Intervalo de confiança (método 3)
    ├── 13_🚪_Monty Hall.py           # Simulação do Problema de Monty Hall
    ├── 14_📊_Hypothesis.py           # Teste de hipóteses entre amostras
    ├── 15_⚙️_Run.py                  # Ferramenta de execução/configuração
    ├── 16_🔗_Correlação.py           # Cálculo e visualização de correlação
    ├── 17_🎲_Sorteador.py            # Sorteador/simulador de eventos
    └── 18_🔢_Regressão.py            # Análise de regressão linear
```

---

## 🎓 Funcionalidades dos Aplicativos

### 1. **Somatório** (`1_∑_Somatorium.py`)
- Cálculo de somatórios simples, da soma dos quadrados e do quadrado da soma
- Entrada interativa de dados
- Visualização passo-a-passo do cálculo

### 2. **Somatório Duplo** (`2_∑_Somatorium_xy.py`)
- Cálculo de somatórios envolvendo duas variáveis (X e Y)
- Útil para cálculos de covariância e correlação

### 3. **Sumarização de Dados** (`3_📑_Sumarização.py`)
- Calcula: média, mediana, moda, quartis, mínimo, máximo, desvio padrão e variância
- Visualização de todas as medidas estatísticas
- Exportação dos resultados

### 4. **Histograma** (`4_📉_Histograma.py`)
- Criação de histogramas interativos
- Análise de distribuição de dados
- Customização de bins e intervalos

### 5. **Desvio Padrão** (`5-8_📐_Desvio Padrao.py`)
- Múltiplas abordagens para cálculo de desvio padrão
- Visualização passo-a-passo do processo
- Cálculo de variância associada

### 6. **Simulação de Lançamento** (`8_🎲_Lançamento.py`)
- Simula lançamentos de dados (1-6) ou moedas (Cara/Coroa)
- Exibe frequências absolutas e relativas
- Gráficos de distribuição

### 7. **Gerador de Dados Sintéticos** (`9_🔢_Gerador.py`)
- Gera dados seguindo distribuição normal
- Parâmetros personalizáveis (média, desvio padrão, tamanho)
- Exportação de dados gerados

### 8. **Intervalos de Confiança** (`10-12_🔍_Intervalo de Confiança.py`)
- Cálculo de intervalos de confiança
- Múltiplas metodologias e níveis de confiança
- Visualização gráfica dos intervalos

### 9. **Problema de Monty Hall** (`13_🚪_Monty Hall.py`)
- Simulação interativa do famoso problema probabilístico
- Comparação entre estratégias de trocar ou manter a escolha
- Análise estatística dos resultados

### 10. **Teste de Hipóteses** (`14_📊_Hypothesis.py`)
- Teste t de Student
- Teste de Mann-Whitney U
- Visualização de distribuições e p-valores
- Interpretação automática dos resultados

### 11. **Análise de Correlação** (`16_🔗_Correlação.py`)
- Importação de dados (CSV ou XLSX)
- Cálculo de matriz de correlação
- Heatmap de correlações
- Análise de relação entre variáveis

### 12. **Regressão Linear** (`18_🔢_Regressão.py`)
- Entrada manual de dados ou importação
- Cálculo da equação da reta
- $R^2$ (coeficiente de determinação)
- Visualização da linha de regressão
- Exportação de resultados

### 13. **Sorteador** (`17_🎲_Sorteador.py`)
- Sorteador de eventos aleatórios
- Simulações de cenários diversos

### 14. **Ferramenta Run** (`15_⚙️_Run.py`)
- Ferramenta auxiliar para execução e configuração

---

## 📚 Arquivos de Dados

### `dados_exmplos.py`
Contém dados de exemplo para testes:
- **100 valores de altura masculina** (média: 1.75m, desvio padrão: 0.07m)
- **100 valores de altura feminina** (média: 1.62m, desvio padrão: 0.06m)

Estes dados podem ser usados em vários aplicativos para exemplificar cálculos estatísticos.

---

## 📝 Arquivos de Suporte

### `distribuicao.py`
Aplicativo para gerar e visualizar distribuições de probabilidade:
- Gera distribuições normais com parâmetros personalizáveis
- Exibe histogramas e estatísticas dos dados gerados

### `rtttl.py`
Conversor de formato RTTTL (Ring Tone Text Transfer Language):
- Converte notações de músicas para áudio
- Utilitário para uso em simulações ou exemplos

---

## 🌐 Página Inicial (`Home.py`)

A página inicial inclui:
- Bem-vindo e informações sobre o projeto
- Informações sobre o Professor Luciano (criador dos aplicativos)
- Contato e links úteis
- Navegação para todos os aplicativos disponíveis

---

## 🐳 Configuração Docker

### Dockerfile
- Imagem base: `python:3.9-slim`
- Instala dependências do `requirements.txt`
- Expõe porta 8501
- Comando padrão: `streamlit run Home.py`

### docker-compose.yml
- Mapeia porta local 8503 para porta 8501 do contêiner
- Monta volume local para desenvolvimento em tempo real
- Container nomeado como `estatistica`

---

## 👨‍🏫 Sobre o Professor Luciano

Professor responsável pelo desenvolvimento desta plataforma educativa:
- **Formação**: Graduação e Mestrado em Ciência da Computação pela UFOP
- **Experiência**: Programação, Desenvolvimento Web, Recuperação da Informação, Aprendizado de Máquina e Ciência de Dados
- **Posição**: Docente e Diretor Geral no IFMG Campus Ponte Nova
- **Email**: luciano.espiridiao@ifmg.edu.br
- **Perfil Streamlit**: [Acesse aqui](https://share.streamlit.io/user/lucianovilasboas)

---

## 📧 Contato

Para dúvidas, sugestões ou mais informações sobre os aplicativos:

**Email**: luciano.espiridiao@ifmg.edu.br

---

## 📄 Licença

Este projeto é fornecido como material educativo para o curso de Tecnologia em Processos Gerenciais do IFMG - Campus Ponte Nova.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Caso tenha sugestões de melhorias, correções de bugs ou novos aplicativos, entre em contato com o Professor Luciano.

---

## 📖 Referências

O projeto aborda os seguintes tópicos de estatística:
- Estatística Descritiva (média, mediana, moda, desvio padrão, variância)
- Distribuições de Probabilidade (normal, uniforme, etc.)
- Intervalos de Confiança
- Testes de Hipóteses
- Correlação e Regressão Linear
- Simulação de Eventos Probabilísticos

---

## 🎯 Objetivos Pedagógicos

✅ Facilitar a compreensão de conceitos estatísticos através da interatividade  
✅ Permitir experimentação prática com dados  
✅ Visualizar graficamente comportamentos estatísticos  
✅ Aplicar conhecimentos em problemas reais  
✅ Desenvolver pensamento crítico analítico  

---

**Última atualização**: 16 de janeiro de 2026  
**Versão**: 1.0
