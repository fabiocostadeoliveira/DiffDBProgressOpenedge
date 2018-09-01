from load_dump_file import ler_df
aaa = ler_df("./df.df")
field = aaa.tables['acr001'].fields[0]
print(field.typeField)