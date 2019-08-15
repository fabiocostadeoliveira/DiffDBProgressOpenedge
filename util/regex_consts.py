
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
