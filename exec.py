from core.sintaxe import sintaxe
from util.field_util import rename_field
from core.load_dump_file import ler_df


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

    return ''


def compareField(field1, field2)->str:
    dif: bool = False
    comando = sintaxe.UPDATE_FIELD + '\n'

    if field2 is None:
        return str(field1)

    if not(field1.typeField.__eq__(field2.typeField)):
        return rename_field(field1, field2)

    if field1.description != field2.description:
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

    return ''


def compare_index(index1, index2) -> str:
    dif: bool = False

    comando = ""

    if index2 is None:
        return str(index1)

    dif = index1.area != index2.area or index2.unique != index1.unique or index2.primary != index1.primary

    if not dif:
        dif = dif_seq(index1, index2)

    if dif:
        comando = sintaxe.RENAME_INDEX.format(
            indexName=index2.name,
            tableName=index2.nameTable,
            newName=index2.name + "_old"
        ) + "\n"

        comando += index1.__str__() + "\n"

        comando += sintaxe.DROP_INDEX.format(indexName=index2.name + "_old", tableName=index2.nameTable)

    return comando


def dif_seq(i1, i2) -> bool:
    dif = False

    dif = len(i1.indexField) != len(i2.indexField)
    if not dif:
        for indf in i1.indexField:
            if2 = i2.indexField[indf]
            if if2 is None:
                dif = True
                break
            if i1.indexField[indf].seq != i2.indexField[indf].seq:
                dif = True
                break
    return dif


def drop_table_comando(table)->str:
    return sintaxe.DROP_TABLE.format(tableName=table.name)


def drop_field_comando(field)->str:
    return sintaxe.DROP_FIELD.format(fieldName=field.name,tableName=field.nameTable)


def drop_index_comando(index)->str:
    return sintaxe.DROP_INDEX.format(indexName=index.name,tableName=index.nameTable)


def get_propriedade(obj, name):
    return obj.get(name, None)


def obj_is_none(table, prop, obj, funcao):
    if table is None:
        return None
    else:
        return funcao(prop,obj)


def compara_dump1_x_dump2(dump1,dump2) -> str:

    retorno  = ''
    for table in dump1.tables:
        t1 = dump1.tables.get(table, None)
        t2 = dump2.tables.get(table, None)

        comando = compareTable(t1, t2)
        print(comando)
        if comando is not '':
            retorno += comando
            print(retorno)

        for field in t1.fields:
            f1 = t1.fields.get(field, None)
            if t2 is None:
                f2 = None
            else:
                f2 = t2.fields.get(field, None)
            comando = compareField(f1, f2)
            if comando is not '':
                retorno += comando
                print(comando)

        for index in t1.indexes:
            i1 = t1.indexes.get(index, None)
            if t2 is None:
                i2 = None
            else:
                i2 = t2.indexes.get(index, None)
            comando = compare_index(i1, i2)
            if comando is not '':
                retorno += comando
                print(comando)
    return retorno

# DROP TABLES, FIELS E INDEX QUE EXISTEM NA DUMP2 E NAO NA DUMP1
def compara_dump2_x_dump1(dump1,dump2):
    retorno = ''
    for table in dump2.tables:
        t1 = dump1.tables.get(table, None)
        t2 = dump2.tables.get(table, None)

        if t1 is None:
            comando = drop_table_comando(t2)
            retorno += comando
            print(comando)
            continue

        for field in t2.fields:
            f1 = obj_is_none(t1, t1.fields, field, get_propriedade)
            if f1 is None:
                comando = drop_field_comando(t2.fields[field])
                retorno += comando
                print(comando)

        for index in t2.indexes:
            i1 = obj_is_none(t1, t1.indexes, index, get_propriedade)
            if i1 is None:
                comando = drop_index_comando(t2.indexes[index])
                retorno += comando
                print(comando)
    return retorno


def executa_diferenca(fileNameDump1,fileNameDump2, **kwargs) -> str:
    dump1 = ler_df(fileNameDump1)
    dump2 = ler_df(fileNameDump2)

    retorno = compara_dump1_x_dump2(dump1, dump2)
    retorno += compara_dump2_x_dump1(dump1, dump2)
    #print('argumentos',kwargs)
    return retorno


if __name__ == '__main__':
    opcoes = {'fileoutput':'./dump_inc.df','ignoredrops':True}
    executa_diferenca('./dumps/df1.df','./dumps/df2.df',**opcoes)



