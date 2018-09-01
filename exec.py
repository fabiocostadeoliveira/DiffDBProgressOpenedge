from load_dump_file import ler_df
aaa = ler_df("./df1.df")
field = aaa.tables['acr001'].fields[0]
print(field.name + " - " + field.typeField + " - " + field.nameTable)