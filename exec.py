from load_dump_file import ler_df
from sintaxe import sintaxe

'''
aaa = ler_df("./df.df")
field = aaa.tables['acr001'].fields[0]
print(field.typeField)

'''

def compareTable(table1, table2)->str:
    dif: bool = False
    comando = sintaxe.UPDATE_TABLE + '\n'

    if(table2 == None):
        return str(table1)
    if (table1.area != table2.area):
        dif = True
        comando += "  AREA \"" + table1.area + "\" \n"
    if (table1.label != table2.label):
        dif = True
        comando += "  LABEL \"" + table1.label + "\" \n"
    if(table1.description != table2.description):
        dif = True
        comando += "  DESCRIPTION \"" + table1.description + "\" \n"
    if (table1.dump_name != table2.dump_name):
        dif = True
        comando += "  DUMP-NAME \"" + table1.dump_name + "\" \n"
    if dif:
        return comando.format(tableName=table1.name)

def compareField(field1, field2)->str:
    dif: bool = False
    comando = sintaxe.UPDATE_FIELD + '\n'

    if (field2 == None):
        return str(field1)

    if (field1.description != field2.description):
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="DESCRIPTION", prop_value=field1.description)
    if (field1.formatt != field2.formatt):
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="FORMAT", prop_value=field1.formatt)
    if (field1.initial != field2.initial):
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="INITIAL", prop_value=field1.initial)
    if (field1.label != field2.label):
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="LABEL", prop_value=field1.label)
    if (field1.position != field2.position):
        dif = True
        comando += sintaxe.PROP_NOT_QUOTE.format(prop_name="POSITION", prop_value=field1.position)
    if (field1.columnLabel != field2.columnLabel):
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="COLUMN-LABEL", prop_value=field1.columnLabel)
    if (field1.help != field2.help):
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="HELP", prop_value=field1.help)
    if (field1.decimals != field2.decimals):
        dif = True
        comando += sintaxe.PROP_NOT_QUOTE.format(prop_name="DECIMALS", prop_value=field1.decimals)
    if (field1.order != field2.order):
        dif = True
        comando += sintaxe.PROP_NOT_QUOTE.format(prop_name="ORDER",prop_value=field1.order)
    if dif:
        return comando.format(fieldName=field1.name,tableName=field1.nameTable)

from load_dump_file import ler_df

dump1 = ler_df("./df1.df")
dump2 = ler_df("./df2.df")

for table in dump1.tables:
    t = dump1.tables.get(table,None)
    t2 = dump2.tables.get(table,None)

    print(compareTable(t, t2))


    for field in t.fields:
        f1 = t.fields.get(field, None)
        if(t2 == None):
            f2 = None
        else:
            f2 =  t2.fields.get(field,None)

        print(compareField(f1,f2))

    for index in t.indexes:
        print("Tabela: ", t.name)
        print("Indice: ", t.name, t.indexes.get(index,None))
