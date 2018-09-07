from table import Table

class Index:
    table: Table
    name: str
    area: str
    unique: bool
    primary: bool
    indexField: list()

    def __init__(self):
        self.table = Table()
        self.name = ""
        self.area = ""
        self.unique = False
        self.primary = False
        self.indexField = list()

    def __str__(self):
        return self.name + " - " + self.area + " - " + self.indexField + " - " +  str(self.unique) + " - " + str(self.primary)



'''
ADD INDEX "acr003-4" ON "acr003" 
  UNIQUE
  PRIMARY
  AREA "Schema Area"
  INDEX-FIELD "codigoDistribuicao" ASCENDING 
  INDEX-FIELD "codigoGrupo" ASCENDING 
  INDEX-FIELD "Descricao" ASCENDING ABBREVIATED 
  INDEX-FIELD "Descricao2" DESCENDING
'''