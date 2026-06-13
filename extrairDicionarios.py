import pandas as pd

def extrair_lista_de_dicionarios(arquivo_valores, arquivo_mapeamento):
    """
    Lê o arquivo contendo os valores e o arquivo de mapeamento.
    
    Retorna uma lista de dicionários, onde cada dicionário 
    corresponde a uma linha do arquivo de valores.
    """
    df_valores = pd.read_csv(arquivo_valores)
    df_mapeamento = pd.read_csv(arquivo_mapeamento)
    
    fs_para_regiao = dict(zip(
        df_mapeamento['freesurfer_number'].astype(str), 
        df_mapeamento['yabplot_region']
    ))
    
    lista_de_dicionarios = []
    lista_de_titulos = []
    
    for indice, linha in df_valores.iterrows():
        dicionario_da_linha = {}
        
        # Armazena o título na lista separada
        titulo = linha['file_path'] if 'file_path' in linha else f"Linha_{indice}"
        lista_de_titulos.append(titulo)
        
        # O dicionário AGORA só conterá as regiões, pois removemos a adição do 'file_path'
        for fs_num, nome_regiao in fs_para_regiao.items():
            if fs_num in df_valores.columns:
                dicionario_da_linha[nome_regiao] = linha[fs_num]
                
        lista_de_dicionarios.append(dicionario_da_linha)
                
    return lista_de_dicionarios, lista_de_titulos
