# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(?P<ADDTABLE>add\s*table\s*\"*.+\")|(?P<AREA>area\s*\"*.+\")|(?P<LABEL>label\s*\"*.+\")|(?P<DESCRIPTION>description\s*\"*.+\")|(?P<DUMPNAME>dump-name\s*\"*.+\")|(?P<TABLETRIGGER>TABLE-TRIGGER\s*\"*.+\"\sOVERRIDE\sPROCEDURE\s*\".*\"\scrc\s\".*\")"

test_str = ("ADD TABLE \"acr001\"\n"
            "  AREA \"Schema Area\"\n"
            "  LABEL \"Cadastro de Distribuicoes\"\n"
            "  DESCRIPTION \"Cadastro de Distribuicoes\"\n"
            "  DUMP-NAME \"acr001\"\n"
            "  TABLE-TRIGGER \"Delete\" OVERRIDE PROCEDURE \"acr001de.trg\" CRC \"?as.\"\n"
            "  TABLE-TRIGGER \"create\" OVERRIDE PROCEDURE \"acr001cr.trg\" CRC \"as.\"\n"
            "  TABLE-TRIGGER \"create\" OVERRIDE PROCEDURE \"acr001cr.trg\" CRC \",.;:?/°/][´`Oó!@#$%¨&*()-+\"\n"
            " ")

matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)

for count, valor in enumerate(matches):
    count = count + 1
    print(str(valor.lastgroup))
'''
for b in matches:
    print('aaa' + str(b))
'''

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))
    '''
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))
    '''

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
