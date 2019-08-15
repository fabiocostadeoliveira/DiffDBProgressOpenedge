import os
QUEBRA_DE_LINHA = '\n'
ESPACO = "" + chr(32) * 5 + ""
ASPAS_DUPLA = "" + "\""

TEXTO_HELP = '-a, --dump1=<nome_da_df1> - ' \
             + QUEBRA_DE_LINHA + ESPACO + '* Passar o nome da primeira df, geralmente a df mais atual' + QUEBRA_DE_LINHA + \
             '-b, --dump2=<nome_da_df2> ' \
             + QUEBRA_DE_LINHA + ESPACO + '* Passar o nome da segunda df, geralmente df desatualizada' + QUEBRA_DE_LINHA + \
             '-c, --dfsaida=<nome_da_dfsaida>' \
             + QUEBRA_DE_LINHA + ESPACO + '* [opcional] Passar nome da df de saida, caso nao seja passado o resultado sera mostrado na tela.' + QUEBRA_DE_LINHA + \
             '-h   * help' + QUEBRA_DE_LINHA + \
             '-v   * versao'

VERSAO = '1.0.0'