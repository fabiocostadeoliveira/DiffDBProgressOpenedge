#from builtins import print

from entities.table import Table
from entities.field import Field
from entities.index import Index, IndexField
from entities.sequence import Sequence
from entities.trigger import Trigger
from util.parser_regex_progress import ParserRegexProgress as Prp

import abc
import re


class Dict:
    fields: list
    indexes: list
    sequences: list

    def __init__(self):
        self.tables = {}
        self.fields = []
        self.indexes = []
        self.sequences = []


class RegexUtil:
    REGEX_TABLE = open('./regex/table_regex.txt', encoding='utf-8', mode='r').read()
    REGEX_FIELD = open('./regex/field_regex.txt', encoding='utf-8', mode='r').read()
    REGEX_INDEX = open('./regex/index_regex.txt', encoding='utf-8', mode='r').read()
    REGEX_SEQUE = open('./regex/seque_regex.txt', encoding='utf-8', mode='r').read()
    REGEX_PROP_INT = r".*\s(?P<VALOR>[0-9]*)"
    REGEX_PROP_SEM_ASPAS = r".*\s(?P<CONTEUDO>\w.*)"
    REGEX_PROP_STRING = r"\"(?P<dados>.*)\""
    REGEX_ADD_FIELD = r"(?P<ADDFIELD>add\s*field\s*)(?P<CAMPO>\".*?\")(?P<TABELA>\sOF\s*\".*\")(?P<TIPO>\s*AS\s*.*)"
    REGEX_ADD_INDEX = r"(?P<ADDINDEX>add\s*index\s*)(?P<INDICE>\".*?\")(?P<TABELA>\sON\s*\".*\")"
    REGEX_INDEX_FIELD = r"(?P<INDEXFIELD>index-field\s*\".*\"\s*(?P<ORDENACAO>ASCENDING|DESCENDING)\s*(?P<ABBREVIATED>ABBREVIATED|))"
    REGEX_TRIGGER = r"(?P<EVENT>TABLE-TRIGGER\s*\".*?\")\s*|(?P<OVERRIDE>OVERRIDE|NO-OVERRIDE)|(?P<PROCEDURE>PROCEDURE\s*\".*?\")|(?P<CRC>CRC\s*\".*?\")"


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
            elif match.lastgroup == 'TABLETRIGGER':
                t = match.groupdict()['TABLETRIGGER']
                res_trigger_regex = re.finditer(RegexUtil.REGEX_TRIGGER, t, re.MULTILINE | re.IGNORECASE)
                parse_triggers = Prp(res_trigger_regex)
                trigger = Trigger()
                trigger.table_name = table.dump_name
                trigger.event = parse_triggers.first_value_string('EVENT')
                trigger.override = parse_triggers.group_value('OVERRIDE', default='OVERRIDE')
                trigger.procedure = parse_triggers.first_value_string('PROCEDURE')
                trigger.crc = parse_triggers.first_value_string('CRC')
                table.addTrigger(trigger)
        return table


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
            elif match.lastgroup == 'EXTENT':
                compile = re.compile(RegexUtil.REGEX_PROP_INT)
                field.extent = compile.findall(match.groupdict()['EXTENT'])[0]
            elif match.lastgroup == 'MANDATORY':
                field.mandatory = True

            elif match.lastgroup == 'ADDFIELD':
                matchesField = re.finditer(RegexUtil.REGEX_ADD_FIELD, match.groupdict()['ADDFIELD'], re.MULTILINE | re.IGNORECASE)
                for matchNum1, matchField in enumerate(matchesField):
                    compileString = re.compile(RegexUtil.REGEX_PROP_STRING)
                    compileSemAspas = re.compile(RegexUtil.REGEX_PROP_SEM_ASPAS)
                    field.nameTable = compileString.findall(matchField.group('TABELA'))[0]
                    field.typeField = compileSemAspas.findall(matchField.group('TIPO'))[0]
                    field.name = compileString.findall(matchField.group('CAMPO'))[0].lower()

        return field


class ModeloIndex(ModeloComando):
    def converter(self, comandoStr):
        compileDados = re.compile(RegexUtil.REGEX_PROP_STRING)
        matches = re.finditer(RegexUtil.REGEX_INDEX, comandoStr, re.MULTILINE | re.IGNORECASE)
        index = Index()

        i = 0
        for matchNum, match in enumerate(matches):
            if match.lastgroup == 'ADDINDEX':
               #index.name = compileDados.findall(match.groupdict()['ADDINDEX'])[0]
               matchesIndex = re.finditer(RegexUtil.REGEX_ADD_INDEX, match.groupdict()['ADDINDEX'], re.MULTILINE | re.IGNORECASE)
               for matchNum1, matchIndex in enumerate(matchesIndex):
                   compileString = re.compile(RegexUtil.REGEX_PROP_STRING)
                   index.name = matchIndex.group('INDICE').replace("\"","")
                   index.nameTable = compileString.findall(matchIndex.group('TABELA'))[0]

            elif match.lastgroup == 'AREA':
                index.area = compileDados.findall(match.groupdict()['AREA'])[0]
            elif match.lastgroup == 'UNIQUE':
                index.unique = True
            elif match.lastgroup == 'PRIMARY':
                index.primary = True
            elif match.lastgroup == 'INDEXFIELD':
                matchesIndex = re.finditer(RegexUtil.REGEX_INDEX_FIELD, match.groupdict()['INDEXFIELD'],re.MULTILINE | re.IGNORECASE)
                for matchNum1, matchIndex in enumerate(matchesIndex):
                    indexF = IndexField()
                    indexF.fieldName = compileString.findall(matchIndex.group('INDEXFIELD'))[0].lower()
                    indexF.order = matchIndex.group('ORDENACAO')
                    indexF.abbreviated = matchIndex.group('ABBREVIATED')
                    indexF.nameIndex = index.name
                    indexF.nameTable = index.nameTable
                    i += 1
                    indexF.seq = i
                    index.indexField[indexF.fieldName] = indexF
        return index


class ModeloSequece(ModeloComando):
    def converter(self, comandoStr):
        compileDados = re.compile(RegexUtil.REGEX_PROP_STRING)
        matches = re.finditer(RegexUtil.REGEX_SEQUE, comandoStr, re.MULTILINE | re.IGNORECASE)
        sequence = Sequence()

        for matchNum, match in enumerate(matches):
            if match.lastgroup == 'ADDSEQUENCE':
                sequence.name = compileDados.findall(match.groupdict()['ADDSEQUENCE'])[0]
            elif match.lastgroup == 'INITIAL':
                if len(compileDados.findall(match.groupdict()['INITIAL'])) > 0:
                    sequence.initial = compileDados.findall(match.groupdict()['INITIAL'])[0]
            elif match.lastgroup == 'INCREMENT':
                if len(compileDados.findall(match.groupdict()['INCREMENT'])) > 0:
                    sequence.increment = compileDados.findall(match.groupdict()['INCREMENT'])[0]
            elif match.lastgroup == 'CYCLEONLIMIT':
                if len(compileDados.findall(match.groupdict()['CYCLEONLIMIT'])) > 0:
                    sequence.cycleOnLimit = compileDados.findall(match.groupdict()['CYCLEONLIMIT'])[0]
            elif match.lastgroup == 'MINVAL':
                if len(compileDados.findall(match.groupdict()['MINVAL'])) > 0:
                    sequence.minVal = compileDados.findall(match.groupdict()['MINVAL'])[0]
            elif match.lastgroup == 'MAXVAL':
                if len(compileDados.findall(match.groupdict()['MAXVAL'])) > 0:
                    sequence.maxVal = compileDados.findall(match.groupdict()['MAXVAL'])[0]

        return sequence


def isTable(comando):
    return comando.strip()[:9] == "ADD TABLE"


def isField(comando):
    return comando.strip()[:9] == "ADD FIELD"


def isIndex(comando):
    return comando.strip()[:9] == "ADD INDEX"


def isSequence(comando):
    return comando.strip()[:12] == "ADD SEQUENCE"


def getModeloConversao(comando):
    if isTable(comando):
        return ModeloTable()
    elif isField(comando):
        return ModeloField()
    elif isIndex(comando):
        return ModeloIndex()
    elif isSequence(comando):
        return  ModeloSequece()

'''
Inicio Execução
'''


def ler_df(arquivo):
    f = open(arquivo, 'r', encoding="utf-8", errors='ignore')
    texto = f.read()
    f.close()

    dump = Dict()
    if len(texto.split("ADD")) <= 1:
        return dump

    for cmd in texto.split("ADD"):
        if len(cmd.replace("\n", "").strip()) > 0:
            comando = "ADD" + cmd
            modeloComando = getModeloConversao(comando)
            comando = modeloComando.converter(comando)
            if type(comando) is Table:
                tabela: Table
                tabela = comando
                dump.tables[tabela.name] = tabela
            elif type(comando) is Field:
                field: Field
                field = comando
                dump.tables[field.nameTable].addField(field)
                dump.fields.append(field)
            elif type(comando) is Index:
                index: Index
                index = comando
                dump.tables[index.nameTable].addIndex(index)
                dump.indexes.append(index)
            elif type(comando) is Sequence:
                sequence: Sequence
                sequence = comando
                dump.sequences.append(sequence)
    return dump

