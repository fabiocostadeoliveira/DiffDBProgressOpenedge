import re

regex = r"(add\sfield.*)|(add\sindex.*)|(add\stable.*)|(add\ssequence.*)"

test_str = (
"ADD FIELD \"cgc-cpf-emitente\" OF \"agr018\" AS character   FORMAT \"x(14)\"  INITIAL \"\"  LABEL \"CGC/CPF emitente\"  POSITION 8  MAX-WIDTH 28  COLUMN-LABEL \"CGC/CPF emitente\"  HELP \"CGC ou CPF do emitente do documento\"  ORDER 50\n"
"ADD FIELD \"serie\" OF \"agr018\" AS character   FORMAT \"xx\"  INITIAL \"\"  LABEL \"Serie do dcto...\"  POSITION 9  MAX-WIDTH 4  COLUMN-LABEL \"Serie!do dcto\"  HELP \"Serie do documento\"  ORDER 60\n"
"ADD FIELD \"idc_id_agr018\" OF \"agr018\" AS decimal   DESCRIPTION \"Identificador IDC\"  FORMAT \">>>>>>>>>>>>>>>>>9.99-\"  INITIAL \"?\"  LABEL \"Id IDC...\"  POSITION 10  MAX-WIDTH 15  COLUMN-LABEL \"ID\"  ORDER 90\n"
"ADD FIELD \"idc_time_agr018\" OF \"agr018\" AS decimal   DESCRIPTION \"Time identificador IDC\"  FORMAT \">>>>>>>>>>>>>>>>>9.99-\"  INITIAL \"?\"  LABEL \"Time IDC.\"  POSITION 11  MAX-WIDTH 15  COLUMN-LABEL \"TIME\"  ORDER 100\n"
"ADD FIELD \"mes\" OF \"agr018\" AS integer   DESCRIPTION \"Mes Emissao NFP\"  FORMAT \"99\"  INITIAL \"?\"  LABEL \"Mes.............\"  POSITION 12  MAX-WIDTH 4  COLUMN-LABEL \"Mes\"  HELP \"Mes Emissao NFP\"  ORDER 110\n"
"ADD FIELD \"ano\" OF \"agr018\" AS integer   DESCRIPTION \"Ano Emissao NFp\"  FORMAT \"9999\"  INITIAL \"?\"  LABEL \"Ano.............\"  POSITION 13  MAX-WIDTH 4  COLUMN-LABEL \"Ano\"  HELP \"Ano Emissao NFp\"  ORDER 120\n"
"ADD FIELD \"esp-dcto-nfp\" OF \"agr018\" AS character   FORMAT \"x(5)\"  INITIAL \"\"  LABEL \"Especie dcto NFP\"  POSITION 14  MAX-WIDTH 10  COLUMN-LABEL \"Esp Dcto!NFP\"  HELP \"Especie do documento NFP\"  ORDER 130\n"
"ADD FIELD \"serie-nfp\" OF \"agr018\" AS character   FORMAT \"x(3)\"  INITIAL \"\"  LABEL \"Serie NFP.......\"  POSITION 15  MAX-WIDTH 6  COLUMN-LABEL \"Serie NFP\"  HELP \"Serie da NFP\"  ORDER 140\n"
"ADD FIELD \"chave-nfp\" OF \"agr018\" AS character   FORMAT \"x(60)\"  INITIAL \"\"  LABEL \"Chave da NFP-e...\"  POSITION 16  MAX-WIDTH 120  COLUMN-LABEL \"Chave de acesso da NFP-e\"  HELP \"Chave de acesso da NFP-e\"  ORDER 150\n"
"ADD INDEX \"agr018-1\" ON \"agr018\"   AREA \"Schema Area\"  UNIQUE  PRIMARY  INDEX-FIELD \"empresa\" ASCENDING   INDEX-FIELD \"unidade\" ASCENDING   INDEX-FIELD \"tipo-operacao\" ASCENDING   INDEX-FIELD \"esp-dcto\" ASCENDING   INDEX-FIELD \"cgc-cpf-emitente\" ASCENDING   INDEX-FIELD \"serie\" ASCENDING   INDEX-FIELD \"numero-dcto\" ASCENDING \n"
"ADD TABLE \"agr019\"  AREA \"Schema Area\"  LABEL \"agrp19\"  DESCRIPTION \"Relacionamento de romaneio de pesagem x romaneio baixados\"  DUMP-NAME \"agr019\"\n"
"ADD FIELD \"reg-romaneio\" OF \"agr019\" AS decimal   DESCRIPTION \"Numero sequencial do registro\"  FORMAT \"999999999999\"  INITIAL ?  LABEL \"Numero Registro.\"  POSITION 2  MAX-WIDTH 18  COLUMN-LABEL \"Numero Registro\"  HELP \"Numero sequencial do registro\"  DECIMALS 3  ORDER 10  MANDATORY\n"
"ADD FIELD \"reg-agr003\" OF \"agr019\" AS decimal   FORMAT \"999999999999.999\"  INITIAL \"0\"  LABEL \"Reg agr003......\"  POSITION 3  MAX-WIDTH 18  COLUMN-LABEL \"Reg agr003\"  HELP \"reg do romaneio de atualizacao\"  DECIMALS 3  ORDER 20\n"
"ADD FIELD \"idc_id_agr019\" OF \"agr019\" AS decimal   DESCRIPTION \"Identificador IDC\"  FORMAT \">>>>>>>>>>>>>>>>>9.99-\"  INITIAL \"?\"  LABEL \"Id IDC...\"  POSITION 4  MAX-WIDTH 15  COLUMN-LABEL \"ID\"  ORDER 30\n"
"ADD FIELD \"idc_time_agr019\" OF \"agr019\" AS decimal   DESCRIPTION \"Time identificador IDC\"  FORMAT \">>>>>>>>>>>>>>>>>9.99-\"  INITIAL \"?\"  LABEL \"Time IDC.\"  POSITION 5  MAX-WIDTH 15  COLUMN-LABEL \"TIME\"  ORDER 40\n"
"ADD INDEX \"agr019-1\" ON \"agr019\"   AREA \"Schema Area\"  UNIQUE  PRIMARY  INDEX-FIELD \"reg-romaneio\" ASCENDING   INDEX-FIELD \"reg-agr003\" ASCENDING \n"
"ADD INDEX \"agr019-2\" ON \"agr019\"   AREA \"Schema Area\"  INDEX-FIELD \"reg-agr003\" ASCENDING \n"
"ADD TABLE \"agr020\"  AREA \"Schema Area\"  LABEL \"agr020\"  DESCRIPTION \"Tabelas de acompanhamento de producao.\"  DUMP-NAME \"agr020\"\n"
"ADD FIELD \"empresa\" OF \"agr020\" AS integer   DESCRIPTION \"Codigo de identicacao da empresa\"  FORMAT \"99\"  INITIAL \"0\"  LABEL \"Empresa.........\"  POSITION 2  MAX-WIDTH 4  COLUMN-LABEL \"Empresa\"  VALEXP \"can-find(first cadempwhere cademp.empresa = input agr020.empresa)\"  VALMSG \"Empresa nao cadastrada!\"  HELP \"Codigo da empresa.\"  ORDER 10  MANDATORY\n"
"ADD FIELD \"unidade\" OF \"agr020\" AS integer   DESCRIPTION \"Codigo da unidade\"  FORMAT \"99\"  INITIAL \"0\"  LABEL \"Unidade.........\"  POSITION 3  MAX-WIDTH 4  COLUMN-LABEL \"Unidade\"  VALEXP \"can-find(first cadempwhere cademp.unidade = input agr020.unidade)\"  VALMSG \"Unidade nao cadastrada!\"  HELP \"Codigo da unidade\"  ORDER 20  MANDATORY\n"
"ADD FIELD \"parceir")

matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))