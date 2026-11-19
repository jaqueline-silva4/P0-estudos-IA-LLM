import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY não encontrada.")

client = genai.Client()

solicitacao = input("Digite sua solicitação: ")

prompt = f"""
Você é um classficador de solicitações de suporte de atendimento.

Analise a mensagem do usuário e classifique em uma categoria.

1.Uma categoria:
- Cobrança
- Acesso
- Dúvida
- Bug 
- Solicitação
- Suporte Técnico
- Cancelamento
- Outros

2. Uma prioridade:
-Baixa
-Média
-Alta

Critérios da classificação:

- Cobrança: pagamentos, faturas, valores, boletos, cobranças.
- Acesso: login, senha, permissão, autenticação.
- Dúvida: perguntas, esclarencimentos.
- Bug: erros, comportamentos inesperados.
- Solicitação: pedidos de serviços, alterações.
- Suporte técnico: problemas com dispositivos, configurações, instalações.
- Cancelamento: encerramento de pedidos ou serviços.
- Outros: mensagens que não se encaixam nas categorias acima.

Prioridade:

-Baixa: situação sem urgência ou de impacto signicativo.
-Média: situação que exige atenção, mas que pode continuar utilizando o serviço.
-Alta: situação que impede uma atividade importante ou causa grande impacto significativo.

Observação: 
Não considere automaticamente toda reclamação como prioridade alta.
Não invente outras categorias que não estejam na mensagem.

Retorne neste formato:

Categoria: [categoria]
Prioridade: [prioridade]

Mensagem do Usuário: {solicitacao}
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite", contents = prompt
)

print("\nResultado da categoria:")
print(response.text.strip())



