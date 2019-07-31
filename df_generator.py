from entities.table import Table
from entities.field import Field
import sys, json, getopt

t: Table


def executar(args):
    d = json.loads(args)
    dict_table = d.get('table', None)
    if dict_table is not None:
        t = criar_table(dict_table)

        ret = t.__str__()
        for f in t.fields:
            ret += t.fields.get(f).__str__()
        print(ret)


def criar_table(table):
    t: Table
    t = Table()
    t.name = table.get('name', '')
    t.description = table.get('description', '')
    t.dump_name = table.get('dump_name', t.name)
    criar_fields(table, t)
    return t


def criar_fields(dict_table, table):
    position = 2
    order = 10
    for field in dict_table['fields']:
        f: Field
        f = Field()
        f.name = field.get('name', '')
        f.typeField = field.get('type', '')
        f.label = field.get('label', f.name)
        f.description = field.get('description', '')
        f.position = str(position)
        f.order = str(order)
        f.nameTable = table.name
        f.columnLabel = field.get('column_label', f.name)
        table.addField(f)

        position += 1
        order += 10

def abrir_arq(nome):
    f = open(nome, 'r', encoding="utf-8", errors='ignore')
    texto = f.read()
    f.close()
    return texto


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvda:b:c:", ["file="])
        arq = ''
        for opt, arg in opts:
            if opt == '--file':
                arq = arg
    except getopt.GetoptError:
        print('exec.py --file=nome_arquivo')
        sys.exit(2)

    dados = abrir_arq(arq)
    executar(dados)
