from core.sintaxe import sintaxe


class Table:

    name: str
    area: str
    label: str
    description: str
    dump_name: str
    tableTrigger: list
    fields: dict
    indexes: dict

    def __init__(self):
        self.name = str()
        self.area = str()
        self.label = str()
        self.description = str()
        self.dump_name = str()
        self.table_trigger = list()
        self.fields = dict()
        self.indexes = dict()

    def addField(self, field):
        self.fields.update({field.name: field})

    def addIndex(self, index):
        self.indexes.update({index.name: index})

    def __str__(self):
        properties = ""
#        print('area=' + self.area + str(self.area != None) )
#        if (self.area != ""):
#            dif = True
#            properties += sintaxe.PROP_QUOTE.format(prop_name="AREA", prop_value=self.area)
        if self.label != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="LABEL", prop_value=self.label)
        if self.description != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="DESCRIPTION", prop_value=self.description)
        if self.dump_name != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="DUMP-NAME", prop_value=self.dump_name)
        if dif:
            return sintaxe.ADD_TABLE_ALL.format(tableName=self.name,properties=properties)

    def _eq_(self, other):
        if type(other) is Table:
            return other.name == self.name
        else:
            return False

