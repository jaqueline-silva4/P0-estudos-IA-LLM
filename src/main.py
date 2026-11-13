import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client()

solicitacao = input("Digite sua solicitação: ")

prompt = f"""
Você é um classficador de solicitações de suporte de atendimento.

Analise a mensagem do usuário e classifique em uma categoria.

- Cobrança
- Acesso
- Dúvida
- Bug 
- Solicitação
- Suporte Técnico
- Cancelamento
- Outros

Critérios da classificação:

- Cobrança: pagamentos, faturas, valores, boletos, cobranças.
- Acesso: login, senha, permissão, autenticação.
- Dúvida: perguntas, esclarencimentos.
- Bug: erros, comportamentos inesperados.
- Solicitação: pedidos de serviços, alterações.
- Suporte técnico: problemas com dispositivos, configurações, instalações.
- Cancelamento: encerramento de pedidos ou serviços.
- Outros: mensagens que não se encaixam nas categorias acima.

Retorne neste formato:

Categoria: [categoria]

Mensagem do Usuário: {solicitacao}
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite", contents = prompt
)

print("\nResultado da categoria:")
print(response.text.strip())



