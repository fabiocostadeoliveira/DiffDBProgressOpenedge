import unittest

from exec import executa_diferenca


class TesteGeral(unittest.TestCase):
    def test_tabela_add(self):
        df1 = "testes/arq/dfTable1_d1.df"
        df2 = "testes/arq/dfTable1_d2.df"
        f = open(df1, 'r', encoding="utf-8", errors='ignore')
        strcompara = f.read()
        self.assertEqual(strcompara, executa_diferenca(df1, df2))
        f.close()

    def test_tabela_update(self):
        df1 = "testes/arq/dfTable1_d3.df"
        df2 = "testes/arq/dfTable1_d1.df"
        strcompara = "UPDATE TABLE \"aac014\" \n  DESCRIPTION \"Historico das alteracoes\" \n\n"
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_tabela_drop(self):
        df1 = "testes/arq/dfTable1_d2.df"
        df2 = "testes/arq/dfTable1_d1.df"
        strcompara = "DROP TABLE \"aac014\"\n\n"
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_field_add(self):
        df1 = "testes/arq/dfField1_d1.df"
        df2 = "testes/arq/dfField1_d2.df"
        strcompara = ('ADD FIELD "empresa" OF "aac014" AS integer\n' +
                      '  FORMAT "99"\n' +
                      '  INITIAL "0"\n' +
                      '  LABEL "Empresa........."\n' +
                      '  POSITION 2\n' +
                      '  COLUMN-LABEL "Empresa"\n' +
                      '  HELP "Codigo da empresa"\n'
                      '  ORDER 10\n\n'
        )
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_field_update(self):
        df1 = "testes/arq/dfField1_d1.df"
        df2 = "testes/arq/dfField1_d3.df"
        strcompara = ('UPDATE FIELD "empresa" of "aac014" \n' +
                      '  INITIAL "0"\n' +
                      '  POSITION 2\n' +
                      '  HELP "Codigo da empresa"\n\n'
        )
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_field_drop(self):
        df1 = "testes/arq/dfField1_d2.df"
        df2 = "testes/arq/dfField1_d1.df"
        strcompara = 'DROP FIELD "empresa" ON "aac014"\n\n'
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_field_rename(self):
        df1 = "testes/arq/dfField1_d1.df"
        df2 = "testes/arq/dfField1_d4.df"
        strcompara = ('RENAME FIELD "empresa" OF "aac014" TO "empresa_old"\n' +
                      '\n' +
                      'ADD FIELD "empresa" OF "aac014" AS integer\n' +
                      '  FORMAT "99"\n' +
                      '  INITIAL "0"\n' +
                      '  LABEL "Empresa........."\n' +
                      '  POSITION 2\n' +
                      '  COLUMN-LABEL "Empresa"\n' +
                      '  HELP "Codigo da empresa"\n' +
                      '  ORDER 10\n\n'
        )
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_index_add(self):
        df1 = "testes/arq/dfIndex1_d1.df"
        df2 = "testes/arq/dfField1_d2.df"
        strcompara = ('ADD INDEX "aac014-1" ON "aac014"\n' +
                      '  UNIQUE\n' +
                      '  PRIMARY\n' +
                      '  INDEX-FIELD "empresa" ASCENDING\n' +
                      '  INDEX-FIELD "cgc-cpf-parceiro" ASCENDING\n' +
                      '  INDEX-FIELD "sequencia" ASCENDING\n\n'
        )
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_index_drop(self):
        df1 = "testes/arq/dfField1_d2.df"
        df2 = "testes/arq/dfIndex1_d1.df"
        strcompara = 'DROP INDEX "aac014-1" ON "aac014"\n\n'
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_index_faltandoUmCampo(self):
        df1 = "testes/arq/dfIndex1_d1.df"
        df2 = "testes/arq/dfIndex1_d2.df"
        strcompara = ('RENAME INDEX "aac014-1" ON "aac014" TO "aac014-1_old"\n' +
                      '\n' +
                      'ADD INDEX "aac014-1" ON "aac014"\n' +
                      '  UNIQUE\n' +
                      '  PRIMARY\n' +
                      '  INDEX-FIELD "empresa" ASCENDING\n' +
                      '  INDEX-FIELD "cgc-cpf-parceiro" ASCENDING\n' +
                      '  INDEX-FIELD "sequencia" ASCENDING\n' +
                      '\n' +
                      'DROP INDEX "aac014-1_old" ON "aac014"\n\n'
        )
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_index_umCampoAMais(self):
        df1 = "testes/arq/dfIndex1_d2.df"
        df2 = "testes/arq/dfIndex1_d1.df"
        strcompara = ('RENAME INDEX "aac014-1" ON "aac014" TO "aac014-1_old"\n' +
                      '\n' +
                      'ADD INDEX "aac014-1" ON "aac014"\n' +
                      '  UNIQUE\n' +
                      '  PRIMARY\n' +
                      '  INDEX-FIELD "empresa" ASCENDING\n' +
                      '  INDEX-FIELD "sequencia" ASCENDING\n' +
                      '\n' +
                      'DROP INDEX "aac014-1_old" ON "aac014"\n\n'
                      )
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_index_seqTrocada(self):
        df1 = "testes/arq/dfIndex1_d1.df"
        df2 = "testes/arq/dfIndex1_d3.df"
        strcompara = ('RENAME INDEX "aac014-1" ON "aac014" TO "aac014-1_old"\n' +
                      '\n' +
                      'ADD INDEX "aac014-1" ON "aac014"\n' +
                      '  UNIQUE\n' +
                      '  PRIMARY\n' +
                      '  INDEX-FIELD "empresa" ASCENDING\n' +
                      '  INDEX-FIELD "cgc-cpf-parceiro" ASCENDING\n' +
                      '  INDEX-FIELD "sequencia" ASCENDING\n' +
                      '\n' +
                      'DROP INDEX "aac014-1_old" ON "aac014"\n\n'
                      )
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_index_caseSensitive(self):
        df1 = "testes/arq/dfIndex1_d4.df"
        df2 = "testes/arq/dfIndex1_d1.df"
        self.assertEqual('', executa_diferenca(df1, df2))

    def test_index_sem_schema_area(self):
        df1 = "testes/arq/dfIndex1_d3.df"
        df2 = "testes/arq/dfIndex1_d4.df"
        strcompara = ('RENAME INDEX "aac014-1" ON "aac014" TO "aac014-1_old"\n' +
                      '\n' +
                      'ADD INDEX "aac014-1" ON "aac014"\n' +
                      '  UNIQUE\n' +
                      '  PRIMARY\n' +
                      '  INDEX-FIELD "empresa" ASCENDING\n' +
                      '  INDEX-FIELD "sequencia" ASCENDING\n' +
                      '  INDEX-FIELD "cgc-cpf-parceiro" ASCENDING\n' +
                      '\n' +
                      'DROP INDEX "aac014-1_old" ON "aac014"\n\n'
        )
        self.assertEqual(strcompara, executa_diferenca(df1, df2))

    def test_field_case_insensitive(self):
        df1 = "testes/arq/dfField1_d5.df"
        df2 = "testes/arq/dfField1_d6.df"
        strcompara = ''
        self.assertEqual(strcompara, executa_diferenca(df1, df2))


    def test_alterarExtent(self):
        df1 = "testes/arq/dfField1_d5.df"
        df2 = "testes/arq/dfField1_d1.df"
        f = open(df1, 'r', encoding="utf-8", errors='ignore')
        strcompara = 'RENAME FIELD "empresa" OF "aac014" TO "empresa_old"\n\n'\
            + '''ADD FIELD "empresa" OF "aac014" AS integer
  FORMAT "99"
  INITIAL "0"
  LABEL "Empresa........."
  POSITION 2
  COLUMN-LABEL "Empresa"
  HELP "Codigo da empresa"
  EXTENT 10
  ORDER 10\n\n'''
        f.close()
        self.assertEqual(strcompara, executa_diferenca(df1, df2))
