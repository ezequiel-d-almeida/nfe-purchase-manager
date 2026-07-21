# 🚗 Gerenciador de Compras via NF-e

> Um pipeline ETL desenvolvido em Python para automatizar o processamento de XMLs de Nota Fiscal Eletrônica (NF-e), transformando documentos fiscais em uma base de dados estruturada para análise e tomada de decisão.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-Excel-success?style=for-the-badge)
![ETL](https://img.shields.io/badge/Pipeline-ETL-orange?style=for-the-badge)
![Power BI](https://img.shields.io/badge/Power_BI-Analytics-yellow?style=for-the-badge)

</p>

---

# 📖 Sobre o Projeto

Empresas que trabalham com dezenas ou centenas de Notas Fiscais Eletrônicas precisam lidar diariamente com atividades repetitivas:

- localizar XMLs;
- remover arquivos duplicados;
- organizar documentos;
- extrair informações fiscais;
- consolidar dados para análise.

Todo esse processo normalmente é manual, sujeito a erros e consome horas de trabalho.

Este projeto foi desenvolvido para resolver esse problema.

O sistema automatiza todo o fluxo de processamento das NF-es, convertendo centenas de XMLs em uma base estruturada pronta para geração de relatórios, dashboards e análises gerenciais.

---

# 🎯 Objetivo

Construir um pipeline ETL capaz de:

- organizar automaticamente milhares de XMLs;
- eliminar documentos duplicados;
- extrair informações relevantes das notas fiscais;
- transformar os dados em objetos estruturados;
- gerar uma planilha Excel pronta para análise;
- servir como fonte de dados para dashboards no Power BI.

---

# ⚙️ Arquitetura do Pipeline

```
             XMLs de NF-e
                    │
                    ▼
        XML Cleaner (Extract)
        ─────────────────────
        • Seleção da pasta
        • Remoção de duplicados
        • Organização por Ano/Mês
                    │
                    ▼
        XML Manager (Transform)
        ───────────────────────
        • Leitura dos XMLs
        • Parsing do XML
        • Modelagem dos dados
        • Objetos Purchase
        • Objetos Product
        • Objetos Installment
                    │
                    ▼
        Excel Writer (Load)
        ───────────────────
        • Compras
        • Produtos
        • Parcelas
                    │
                    ▼
           Dashboard Power BI
```

---

# 🧩 Fluxo do Projeto

```
Selecionar pasta
        │
        ▼
Ler XMLs
        │
        ▼
Remover duplicados
        │
        ▼
Organizar arquivos
        │
        ▼
Extrair dados fiscais
        │
        ▼
Modelar objetos Python
        │
        ▼
Gerar Excel
        │
        ▼
Power BI
```

---

# 📊 Informações extraídas

Cada XML fornece automaticamente:

### Compra

- Fornecedor
- CNPJ
- Número da Nota Fiscal
- Data de Emissão
- Valor Total

### Produtos

- Código
- Descrição
- Quantidade
- Unidade
- Valor Unitário
- Valor Total

### Parcelas

- Número da parcela
- Data de vencimento
- Valor

---

# 📁 Estrutura do Projeto

```
Gerenciador-de-Compras-via-NFe/

│

├── xml_cleaner/
│   ├── main.py
│   ├── organize_by_date.py
│   ├── remove_duplicates.py
│   ├── select_folder.py
│   └── xml_utils.py
│
├── xml_manager/
│   ├── extractor/
│   ├── models/
│   ├── output/
│   ├── utils/
│   └── main.py
│
├── docs/
│
├── requirements.txt
│
└── README.md
```

---

# 🏗️ Modelagem

O projeto utiliza uma modelagem orientada a objetos para representar os dados das notas fiscais.

## Purchase

Representa uma Nota Fiscal.

Possui:

- fornecedor
- CNPJ
- número da NF
- data
- valor total
- lista de produtos
- lista de parcelas

---

## Product

Representa um item comprado.

Cada produto contém:

- código
- descrição
- quantidade
- unidade
- valor unitário
- valor total

---

## Installment

Representa uma parcela da nota.

Contém:

- número
- vencimento
- valor

---

# 📈 Resultado

Ao final do processamento o sistema gera automaticamente um arquivo Excel contendo:

- Compras
- Produtos
- Parcelas

Essa estrutura pode ser utilizada diretamente em ferramentas de Business Intelligence como Power BI.

---

# 🛠️ Tecnologias

- Python
- XML
- ElementTree
- Dataclasses
- OpenPyXL
- Tkinter

---

# ▶️ Como executar

Clone o projeto

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Execute

```bash
python xml_cleaner/main.py
```

Selecione a pasta contendo os XMLs.

O sistema executará automaticamente todo o pipeline.

---

# 💡 Aplicações

Este projeto pode ser utilizado para:

- Gestão de compras
- Controle financeiro
- Consolidação de NF-es
- Engenharia de Dados
- ETL de documentos fiscais
- Alimentação de Data Warehouse
- Construção de Dashboards

---

# 🚀 Próximas melhorias

- Banco de dados PostgreSQL
- Exportação para Parquet
- Logs estruturados
- Testes automatizados
- Interface Web
- Docker
- Agendamento automático
- Pipeline em Apache Airflow

---

# 📚 Conceitos aplicados

- ETL
- Data Cleaning
- Data Extraction
- Data Modeling
- Object-Oriented Programming
- XML Parsing
- File Processing
- Data Transformation
- Data Pipeline
- Business Intelligence

---

# 👨‍💻 Autor

**Ezequiel Damasceno de Almeida**

Graduando em Ciência de Dados.

Desenvolvendo projetos focados em Engenharia de Dados, Automação de Processos e Business Intelligence.

LinkedIn:
> https://www.linkedin.com/in/almeida-ezequiel

GitHub:
> https://github.com/ezequiel-d-almeida