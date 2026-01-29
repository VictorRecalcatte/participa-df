import re

def realizar_triagem(texto):
    """
    Realiza uma análise prévia via Regex e palavras-chave.
    Retorna: (Classificação, Motivo, Requer_IA)
    """
    texto_limpo = str(texto).lower()
    
    # 1. Dados Encontrados

    padrao_cpf = r'\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11}'
    padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    padrao_tel = r'(\(?\d{2}\)?\s?\d{4,5}-?\d{4})'
    
    if re.search(padrao_cpf, texto_limpo) or re.search(padrao_email, texto_limpo) or re.search(padrao_tel, texto_limpo):
        return "não público", "Identificação de dado pessoal estruturado (CPF, e-mail ou telefone) detectada via padrão numérico/sintático.", False
    
    indicadores_pessoais = [
        "meu nome", "meu cpf", "minha casa", "meu endereço", 
        "meu telefone", "meu rg", "meu email", "meu e-mail",
        "minha consulta", "meu prontuário", "minha solicitação pessoal", "rg", 'cpf'
    ]

    # Verifica se alguma dessas combinações aparece no texto
    if any(frase in texto_limpo for frase in indicadores_pessoais):
        return "não público", "Presença de expressões de autoidentificação e posse em primeira pessoa, indicando relato de natureza privada e exposição de identidade do cidadão.", False

   # 2. Nomes e endereços por extenso - Necessita IA
    palavras_suspeitas = ['nome', 'rua', 'endereço', 'casa', 'apartamento', 'moro', 'nascimento']
    if any(palavra in texto_limpo for palavra in palavras_suspeitas):
        return "dúvida", "Análise semântica necessária", True
    
    # 3. Nenhum dado sensível detectado
    return "público", "Nenhum dado sensível detectado", False