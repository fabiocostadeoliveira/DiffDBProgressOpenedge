import re

regex = r"(?P<ADDFIELD>add\s*field\s*)(?P<CAMPO>\".*?\")(?P<TABELA>\sOF\s*\".*\")(?P<TIPO>\s*AS\s*.*)"

test_str = ("ADD FIELD \"codigoDistribuicao\" OF \"acr001\" AS decimal")
compile = re.compile(regex)
result = compile.findall(test_str)
print(len(result))

matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)
for matchNum, match in enumerate(matches):
    print(match.groupdict())
'''
for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))
'''