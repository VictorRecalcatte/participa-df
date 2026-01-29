import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Carrega a chave da API do arquivo .env para segurança
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analisar_texto_sensivel(id_pedido, descricao):
    """
    Interface com o Gemini para identificar dados pessoais conforme o Edital nº 10/2025.
    Identifica: nome, CPF, RG, telefone e endereço de e-mail.
    """
    # Usar o nome do modelo sem o v1beta se possível
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    
    # Prompt otimizado para as métricas do Edital (Precisão e Sensibilidade)
    prompt = f"""
    Você é um auditor de privacidade.
    Sua tarefa é identificar se o pedido de acesso à informação abaixo contém dados pessoais.
    
    Dados a procurar: nome completo, CPF, RG, telefone e e-mail.
    
    Texto do Pedido (ID {id_pedido}):
    "{descricao}"
    
    Responda estritamente em formato JSON:
    {{
        "classificacao": "não público" ou "público",
        "dados_expostos": ["lista de itens encontrados"],
        "justificativa": "breve explicação técnica"
    }}
    """
    
    try:
        response = model.generate_content(prompt)

        # Limpeza para garantir que o retorno seja apenas o JSON

        resposta_bruta = response.text

        #Limpa Markdown
        texto_limpo = resposta_bruta.replace('```json', '').replace('```', '').strip()

        # Converte para JSON 
        json_res = json.loads(texto_limpo)

        return json_res
    except Exception as e:
        # Captura a mensagem de erro real (ex: Quota Exceeded, API Key Expired, etc)
        mensagem_erro_real = str(e)
        
        return {
            "classificacao": "não público", 
            "dados_expostos": ["ERRO TÉCNICO / API"],
            "justificativa": f"Falha na análise semântica. Classificado preventivamente como NÃO PÚBLICO para proteção de dados."
        }