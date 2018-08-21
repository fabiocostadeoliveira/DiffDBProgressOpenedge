#from builtins import print

from table import Table
from field import Field
import abc
import re

class RegexUtil:
    REGEX_TABLE = open('./table_regex.txt', encoding='utf-8', mode='r').read()
    REGEX_FIELD = open('./field_regex.txt', encoding='utf-8', mode='r').read()
    REGEX_PROP_STRING = r"\"(?P<dados>.*)\""
    REGEX_PROP_INT = r".*\s(?P<VALOR>[0-9])"

class ModeloComando(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def converter(self, comandoStr):
        return

class ModeloTable(ModeloComando):
    def converter(self, comandoStr):
        compileDados = re.compile(RegexUtil.REGEX_PROP_STRING)
        matches = re.finditer(RegexUtil.REGEX_TABLE, comandoStr, re.MULTILINE | re.IGNORECASE)

        table = Table()

        for matchNum, match in enumerate(matches):
            if match.lastgroup == 'DUMPNAME':
                table.dump_name = compileDados.findall(match.groupdict()['DUMPNAME'])[0]
            elif match.lastgroup == 'AREA':
                table.area = compileDados.findall(match.groupdict()['AREA'])[0]
            elif match.lastgroup == 'DESCRIPTION':
                table.description = compileDados.findall(match.groupdict()['DESCRIPTION'])[0]
            elif match.lastgroup == 'LABEL':
                table.label = compileDados.findall(match.groupdict()['LABEL'])[0]
            elif match.lastgroup == 'ADDTABLE':
                table.name = compileDados.findall(match.groupdict()['ADDTABLE'])[0]
        print(table)

class ModeloField(ModeloComando):
    def converter(self, comandoStr):
        compileDados = re.compile(RegexUtil.REGEX_PROP_STRING)
        matches = re.finditer(RegexUtil.REGEX_FIELD, comandoStr, re.MULTILINE | re.IGNORECASE)

        field = Field()

        for matchNum, match in enumerate(matches):
            if match.lastgroup == 'DESCRIPTION':
                field.description = compileDados.findall(match.groupdict()['DESCRIPTION'])[0]
            elif match.lastgroup == 'FORMAT':
                field.formatt = compileDados.findall(match.groupdict()['FORMAT'])[0]
            elif match.lastgroup == 'INITIAL':
                field.initial = compileDados.findall(match.groupdict()['INITIAL'])[0]
            elif match.lastgroup == 'LABEL':
                field.label = compileDados.findall(match.groupdict()['LABEL'])[0]
            elif match.lastgroup == 'POSITION':
                compile = re.compile(RegexUtil.REGEX_PROP_INT)
                field.position = compile.findall(match.groupdict()['POSITION'])[0]
            elif match.lastgroup == 'COLUMNLABEL':
                field.columnLabel = compileDados.findall(match.groupdict()['COLUMNLABEL'])[0]
            elif match.lastgroup == 'HELP':
                field.help = compileDados.findall(match.groupdict()['HELP'])[0]
            elif match.lastgroup == 'DECIMALS':
                compile = re.compile(RegexUtil.REGEX_PROP_INT)
                field.decimals = compile.findall(match.groupdict()['DECIMALS'])[0]
            elif match.lastgroup == 'ORDER':
                compile = re.compile(RegexUtil.REGEX_PROP_INT)
                field.order = compile.findall(match.groupdict()['ORDER'])[0]
            elif match.lastgroup == 'ADDFIELD':
                field.name = compileDados.findall(match.groupdict()['ADDFIELD'])[0]
        print(field)

class ModeloIndex(ModeloComando):
    def converter(self, comandoStr):
        print("Parece que é um index")

class ModeloSequece(ModeloComando):
    def converter(self, comandoStr):
        print("Parece que é um sequence")

def isTable(comando):
    return (comando.strip()[:9] == "ADD TABLE")
def isField(comando):
    return (comando.strip()[:9] == "ADD FIELD")
def isIndex(comando):
    return (comando.strip()[:9] == "ADD INDEX")
def isSequence(comando):
    return (comando.strip()[:12] == "ADD SEQUENCE")

def getModeloConversao(comando):
    if (isTable(comando)):
        return ModeloTable()
    elif (isField(comando)):
        return ModeloField()
    elif (isIndex(comando)):
        return ModeloIndex()
    elif (isSequence(comando)):
        return  ModeloSequece()

f = open('./dfteste.df', 'r')

texto = f.read()

comando = None

for cmd in texto.split("ADD"):
    if(len(cmd.replace("\n", "").strip()) > 0):
        comando = "ADD" + cmd
        modeloComando = getModeloConversao(comando)
        modeloComando.converter(comando)
