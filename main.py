import pandas as pd
import time
from ia_service import analisar_texto_sensivel
from triagem import realizar_triagem

def processar_desafio_df():
    #Caminho do Arquivo Excel, Modifique conforme necessário
    caminho_arquivo = 'amostra.xlsx'

    ##Carrega os dados do arquivo xls
    try:
        df = pd.read_excel(caminho_arquivo)
        print("Arquivo Excel carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo Excel: {e}")
        return
    
    resultados = []


    for index, linha in df.iterrows():
        ## Ajuste conforme os nomes das colunas do seu arquivo
        id_pedido = linha.get('ID')
        descricao = linha.get('Texto Mascarado')

        print(f"Processando pedido ID: {id_pedido}")


        classificacao, motivo, requer_ia = realizar_triagem(descricao)
        #Chama Análise via IA se necessário
        if requer_ia == True:
            analise_ia = analisar_texto_sensivel(id_pedido, descricao)
            
            resultados.append({
                "ID": id_pedido,
                "TEXTO ORIGINAL": descricao,
                "CLASSIFICACAO": analise_ia.get("classificacao"), # 'público' ou 'não público' 
                "JUSTIFICATIVA": analise_ia.get("justificativa")
            })

            time.sleep(3)  # Pequena pausa para evitar rate limiting
        else:
            resultados.append({
                "ID": id_pedido,
                "TEXTO ORIGINAL": descricao,
                "CLASSIFICACAO": classificacao,
                "JUSTIFICATIVA": motivo
            })

    # Cria um DataFrame com os resultados
    df_final = pd.DataFrame(resultados)

    print(df_final)
    df_final.to_excel('resultados_desafios_df.xlsx', index=False)
    print("Processamento concluído. Resultados salvos em resultados_desafios_df.xlsx")

if __name__ == "__main__":
    processar_desafio_df()

