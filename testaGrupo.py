from table import Table
from field import Field
from index import Index
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(?P<ADDTABLE>add\s*table\s*\".*\")|(?P<AREA>area\s*\".*\")|(?P<LABEL>label\s*\".*\")|(?P<DESCRIPTION>description\s*\".*\")|(?P<DUMPNAME>dump-name\s*\".*\")|(?P<TABLETRIGGER>TABLE-TRIGGER\s*\".*\"\sOVERRIDE\sPROCEDURE\s*\".*\"\scrc\s\".*\")"

test_str = open('C:\\Users\\deivian.souza\\Desktop\\Diferenca\\dffinal.df')
test_str = test_str.read()

matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print(match.group())


    '''
        if (match.lastindex == 6):
    '''
    '''
    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))
    '''

