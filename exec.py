from core.sintaxe import sintaxe
from util.field_util import rename_field
from core.load_dump_file import ler_df
from core import constants as constant
import sys
import getopt


def compare_triggers(table1, table2) ->str:
    dif = False
    command = ""
    result_trigger_list = list()
    ## retira triggers que nao contem na table1
    for trg2 in table2.triggers:
        trg1 = [tt1 for tt1 in table1.triggers if tt1.event.lower() == trg2.event.lower()]
        if len(trg1) is 0:
            action = {'action': 'del', 'trigger': trg2}
            result_trigger_list.append(action)

    ## add triggers que nao contem na table2
    for idx, trg1 in enumerate(table1.triggers):
        trg2 = [tt2 for tt2 in table2.triggers if tt2.event.lower() == trg1.event.lower()]
        if trg2 is [] or trg2 != trg1:
            action = {'action': 'add', 'trigger': trg1}
            result_trigger_list.append(action)

    ##ordena resultado da lista, isso deve ficar assim por causa dos testes unitarios que
    ##tem ordem de comparacao
    result_trigger_list.sort(key=lambda l: l['trigger'].event)
    for item in result_trigger_list:
        trg = item['trigger']
        action = item['action']
        if action == 'add':
            command += str(trg)
        elif action == 'del':
            command += trg.del_trigger_sintaxe()
        else:
            raise ValueError('Acao nao tratada')

    return command


def compareTable(table1, table2) -> str:
    dif: bool = False
    comando = sintaxe.UPDATE_TABLE + '\n'

    if table2 is None:
        return str(table1)

    #if (table1.area != table2.area):
    #    dif = True
    #    comando += "  AREA \"" + table1.area + "\" \n"
    if table1.label != table2.label:
        dif = True
        comando += "  LABEL \"" + table1.label + "\" \n"
    if table1.description != table2.description:
        dif = True
        comando += "  DESCRIPTION \"" + table1.description + "\" \n"
    # if (table1.dump_name != table2.dump_name):
    #     dif = True
    #     comando += "  DUMP-NAME \"" + table1.dump_name + "\" \n"
    if table1.trigger_to_string() != table2.trigger_to_string():
        dif = True
        comando += compare_triggers(table1, table2)
    if dif:
        return comando.format(tableName=table1.name) + '\n'

    return ''


def compareField(field1, field2)->str:
    dif: bool = False
    comando = sintaxe.UPDATE_FIELD + '\n'

    if field2 is None:
        return str(field1)

    if not(field1.typeField.__eq__(field2.typeField)) or field1.extent != field2.extent:
        return rename_field(field1, field2)

    if field1.description != field2.description:
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="DESCRIPTION", prop_value=field1.description)
    if field1.formatt != field2.formatt:
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="FORMAT", prop_value=field1.formatt)
    if field1.initial != field2.initial:
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="INITIAL", prop_value=field1.initial)
    if field1.label != field2.label:
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="LABEL", prop_value=field1.label)
    if field1.position != field2.position:
        dif = True
        comando += sintaxe.PROP_NOT_QUOTE.format(prop_name="POSITION", prop_value=field1.position)
    if field1.columnLabel != field2.columnLabel:
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="COLUMN-LABEL", prop_value=field1.columnLabel)
    if field1.help != field2.help:
        dif = True
        comando += sintaxe.PROP_QUOTE.format(prop_name="HELP", prop_value=field1.help)
    if field1.decimals != field2.decimals:
        dif = True
        comando += sintaxe.PROP_NOT_QUOTE.format(prop_name="DECIMALS", prop_value=field1.decimals)
    if field1.order != field2.order:
        dif = True
        comando += sintaxe.PROP_NOT_QUOTE.format(prop_name="ORDER", prop_value=field1.order)
    if field1.mandatory != field2.mandatory:
        if field2.mandatory is True:
            comando += sintaxe.PROP_FLAG.format(prop_flag="NULL-ALLOWED")
        else:
            comando += sintaxe.PROP_FLAG.format(prop_flag="MANDATORY")

    if dif:
        return comando.format(fieldName=field1.name, tableName=field1.nameTable) + '\n'

    return ''


def compare_index(index1, index2) -> str:
    dif: bool = False

    comando = ""
    if index2 is None:
        return str(index1)

    dif = index2.unique != index1.unique or index2.primary != index1.primary

    if not dif:
        dif = dif_seq(index1, index2)

    if dif:
        comando = sintaxe.RENAME_INDEX.format(
            indexName=index2.name,
            tableName=index2.nameTable,
            newName=index2.name + "_old"
        ) + "\n"

        comando += index1.__str__()
        comando += sintaxe.DROP_INDEX.format(indexName=index2.name + "_old", tableName=index2.nameTable)

    return comando


def dif_seq(i1, i2) -> bool:
    dif = len(i1.indexField) != len(i2.indexField)
    if not dif:
        for indf in i1.indexField:
            if2 = i2.indexField.get(indf, None)
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


def compara_dump1_x_dump2(dump1, dump2) -> str:
    retorno  = ''
    for table in dump1.tables:

        t1 = dump1.tables.get(table, None)
        t2 = dump2.tables.get(table, None)

        if t1 is not None and t1.name.startswith('agr'):
            continue

        if t2 is not None and t2.name.startswith('agr'):
            continue

        comando = compareTable(t1, t2)

        if comando is not '':
            retorno += comando

        for field in t1.fields:
            f1 = t1.fields.get(field, None)
            if t2 is None:
                f2 = None
            else:
                f2 = t2.fields.get(field, None)
            comando = compareField(f1, f2)
            if comando is not '':
                retorno += comando

        for index in t1.indexes:
            i1 = t1.indexes.get(index, None)
            if t2 is None:
                i2 = None
            else:
                i2 = t2.indexes.get(index, None)
            comando = compare_index(i1, i2)
            if comando is not '':
                retorno += comando
    return retorno


# DROP TABLES, FIELS E INDEX QUE EXISTEM NA DUMP2 E NAO NA DUMP1
def compara_dump2_x_dump1(dump1, dump2):
    retorno = ''
    for table in dump2.tables:
        t1 = dump1.tables.get(table, None)
        t2 = dump2.tables.get(table, None)

        if t1 is None:
            comando = drop_table_comando(t2)
            retorno += comando
            continue

        for field in t2.fields:
            f1 = obj_is_none(t1, t1.fields, field, get_propriedade)
            if f1 is None:
                comando = drop_field_comando(t2.fields[field])
                retorno += comando

        for index in t2.indexes:
            i1 = obj_is_none(t1, t1.indexes, index, get_propriedade)
            if i1 is None:
                comando = drop_index_comando(t2.indexes[index])
                retorno += comando
    return retorno


def executa_diferenca(fileNameDump1,fileNameDump2, **kwargs) -> str:
    dump1 = ler_df(fileNameDump1)
    dump2 = ler_df(fileNameDump2)

    retorno = compara_dump1_x_dump2(dump1, dump2)
    if kwargs.get('drops', None) is None:
        retorno += compara_dump2_x_dump1(dump1, dump2)

    return retorno


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hvda:b:c:", ["dump1=","dump2=","dfsaida=","drops"])
    except getopt.GetoptError:
        print ('exec.py --dump1=nome_dump1 --dump2=nome_dump2 --dfsaida=nome_arquivo_saida')
        sys.exit(2)
    opcoes = dict()
    for opt, arg in opts:
        if opt == '-h':
            print(constant.TEXTO_HELP)
            sys.exit()
        elif opt == '-v':
            print('versao:', constant.VERSAO)
            sys.exit()
        elif opt in ("-a", "--dump1"):
            opcoes['dump1'] = arg
        elif opt in ("-b", "--dump2"):
            opcoes['dump2'] = arg
        elif opt in ("-c", "--dfsaida"):
            opcoes['dfsaida'] = arg
        elif opt in ("-d", "--drops"):
            opcoes['drops'] = False

    if opcoes.get('dump1',None) == None or opcoes.get('dump2',None) == None:
        print (constant.QUEBRA_DE_LINHA + "Parametros Invalidos!!!")
        print ("Devem ser informados pelo menos os parametros --dump1 e --dump2")
        exit(1)
    return opcoes


if __name__ == '__main__':
    opcoes = main(sys.argv[1:])
    retorno = executa_diferenca(opcoes.get('dump1'), opcoes.get('dump2'), **opcoes)
    nomeArquivoSaida = opcoes.get('dfsaida', None)
    if nomeArquivoSaida is None:
        print(retorno)
        exit(0)
    else:
        try:
            arquivoSaida = open(nomeArquivoSaida, 'w')
            arquivoSaida.write(retorno)
            arquivoSaida.close()
        except FileNotFoundError as e:
            print(e)
            print('Erro ao criar arquivo de saida!!!')
            exit(1)

