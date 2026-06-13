import yabplot as yab
import numpy as np
import matplotlib.pyplot as plt
from extrairDicionarios import extrair_lista_de_dicionarios

atlas = 'aparc'
#ATUALIZE O CAMINHO DE "caminho_valores" COM O SEU ARQUIVO.
#LEMBRE DE DEIXAR "data/" NO INÍCIO DO CAMINHO 
caminho_valores = 'data/20260606_214846_SUVR_min.csv'
caminho_mapeamento = 'dicionario/yabplot_freesurfer_mapping.csv'

array_dados_tvalue, array_titulos, = extrair_lista_de_dicionarios(caminho_valores, caminho_mapeamento)

for data in zip(array_dados_tvalue, array_titulos):

    dict_data = data[0]
    title = data[1]

    ax = yab.plot_cortical(data=dict_data, 
                        atlas=atlas, 
                        vminmax=[min(dict_data.values()), max(dict_data.values())], 
                        views=['left_lateral', 'superior', 'left_medial'],
                        bmesh='midthickness',
                        figsize=(400, 300), cmap='viridis')
    ax.set_title(title, fontsize=7)

plt.show()
