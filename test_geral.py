import unittest

from ../exec import  

class TesteGeral(unittest.TestCase):
    def test_tabela_existe_apenas_dump1(self):
        strCompara = open("arq/dfTeste1_d1.df", 'r', encoding="utf-8", errors='ignore').read()
