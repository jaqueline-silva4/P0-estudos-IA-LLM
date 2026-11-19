# P0 - Primeiro Fluxo com LLM

Repositório destinado ao desenvolvimento de uma aplicação em Python que utiliza um Modelo de Linguagem (LLM) para resolver um problema textual real, com foco em integração com APIs, organização do código e execução reproduzível.

## Sobre o projeto

O projeto consiste em um classificador de solicitações de suporte de atendimento. A aplicação recebe uma mensagem textual do usuário e utiliza o modelo **Google Gemini** para identificar sua categoria e prioridade.

O objetivo é facilitar a organização e a identificação das solicitações, auxiliando na triagem dos atendimentos.

## Funcionalidades

- Receber solicitações de suporte pelo terminal.
- Classificar as mensagens em categorias predefinidas.
- Identificar o nível de prioridade de cada solicitação.
- Apresentar o resultado da classificação ao usuário.

### Categorias disponíveis

- Cobrança
- Acesso
- Dúvida
- Bug
- Solicitação
- Suporte Técnico
- Cancelamento
- Outros

### Níveis de prioridade

- Baixa
- Média
- Alta

## Tecnologias utilizadas

- Python
- Google Gemini (LLM)
- Google Gen AI SDK
- python-dotenv

## Estrutura do projeto

```text
P0-estudos-IA-LLM/
│
├── src/
│   └── main.py
│
├── .env
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Como executar o projeto

### 1. Pré-requisitos

- Python instalado.
- Uma chave de API do Google Gemini.

### 2. Clonar o repositório

```bash
git clone https://github.com/jaqueline-silva4/P0-estudos-IA-LLM.git
```

Entre na pasta do projeto:

```bash
cd P0-estudos-IA-LLM
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual:

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API:

```env
GEMINI_API_KEY=sua_chave_aqui
```

A chave de API pode ser obtida no [Google AI Studio](https://aistudio.google.com/apikey).

**Importante:** Não compartilhe sua chave de API nem publique o arquivo `.env` no GitHub.

### 6. Executar a aplicação

```bash
python src/main.py
```

Digite uma solicitação de suporte quando solicitado e aguarde o resultado da classificação.

## Autor

Jaqueline da Silva Miranda

Projeto desenvolvido como parte do percurso de estudos em Inteligência Artificial, no projeto P0 - Primeiro Fluxo com LLM.