from table import Table
from field import Field
from index import Index

import re

#regex = r"(add\sfield.*)|(add\sindex.*)|(add\stable.*)|(add\ssequence.*)"
re_field = r"(add\sfield.*)"
f = open("C:\\Users\\Fábio\\Desktop\\ent_client.df", 'r')
texto = f.read()
'''
texto = f.read()
add_field = re.findall(regex,texto,re.IGNORECASE)
print(add_field)
add_table = re.findall(regex,texto,re.IGNORECASE)
print(add_field)
'''

saida = open("C:\\Users\\Fábio\\Desktop\\client2.df", 'w')
comando = None
for cmd in texto.split("ADD"):
    comando = "ADD " + cmd.replace("\n", "")
    print(comando + "\n")
    #print(comando)
    #saida.write(comando + "\n")
#saida.close()
