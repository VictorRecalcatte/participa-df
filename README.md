Participa DF - Classificador Híbrido de Dados Pessoais (IA)
Este projeto foi desenvolvido para o Hackathon Participa DF (2026), focado na categoria Acesso à Informação. A solução automatiza a identificação de dados sensíveis em pedidos de informação, garantindo a conformidade com a LGPD e o Edital nº 10/2025.

A Solução: Arquitetura Híbrida de Triagem
O diferencial deste sistema é a sua Eficiência Operacional e de Custos. Em vez de depender exclusivamente de processamento em nuvem, o sistema utiliza uma abordagem em camadas:

Camada Local (Regex): Identifica instantaneamente padrões estruturados como CPF, e-mail e telefone.

Camada Local (Heurísticas/Whitelist): Filtra textos administrativos e institucionais (ex: "Programa de Integridade", "SEI") que, embora contenham termos "suspeitos", são claramente públicos. Isso reduz drasticamente o consumo de tokens de IA.

Camada de IA (Gemini 2.5 Flash Lite): Acionada apenas em casos de dúvida semântica real, garantindo precisão na identificação de relatos pessoais complexos.

Protocolo Fail-Safe: Caso a cota da API seja excedida ou ocorra falha de conexão, o sistema aplica o princípio da Privacidade por Padrão, classificando o item como Não Público para evitar qualquer risco de exposição.

Tecnologias Utilizadas
Python 3.9+
Google Gemini API (gemini-2.5-flash-lite)
Pandas & Openpyxl: Manipulação de planilhas Excel.
Python-Dotenv: Gestão segura de credenciais de API.

Como Instalar e Rodar
Para que o avaliador execute o projeto:

Clonar o repositório: git clone https://github.com/VictorRecalcatte/participa-df

Instalar dependências: pip install -r requirements.txt

Configurar o Ambiente:

Renomeie o arquivo .env.example para .env.

Insira sua chave de API do Google AI Studio na variável GEMINI_API_KEY.

Execução: python main.py

O sistema processará a amostra e gerará o arquivo resultados_desafios_df.xlsx com as classificações e justificativas técnicas.

Conformidade e Documentação
Cada registro classificado acompanha uma Justificativa Detalhada, fundamentando se a decisão foi baseada em padrões sintáticos ou análise semântica contextual, facilitando a auditoria pelos servidores da CGDF.

Desenvolvido por: Victor Augusto Recalcatte Hackathon Participa DF 2026
