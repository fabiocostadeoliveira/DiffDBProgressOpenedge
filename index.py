from sintaxe import sintaxe

class Index:
    nameTable: str
    name: str
    area: str
    unique: bool
    primary: bool
    indexField: dict

    def __init__(self):
        self.nameTable = ""
        self.name = ""
        self.area = ""
        self.unique = False
        self.primary = False
        self.indexField = dict()

    def __str__(self):
        properties = ""
        if self.area != "":
            properties += sintaxe.PROP_QUOTE.format(prop_name="AREA", prop_value=self.area)
        if self.unique:
            properties += sintaxe.PROP_NONE.format(prop_name="UNIQUE")
        if self.primary:
            properties += sintaxe.PROP_NONE.format(prop_name="PRIMARY")

        fields = ""
        for field in self.indexField:
            fields += self.indexField[field].__str__()
        return sintaxe.ADD_INDEX_ALL.format(indexName=self.name, tableName=self.nameTable, properties=properties, fields=fields)


class IndexField:
    nameTable: str
    nameIndex: str
    fieldName: str
    order: str
    abbreviated: bool
    seq: int

    def __init__(self):
        self.nameTable = ""
        self.nameIndex = ""
        self.fieldName = ""
        self.order = ""
        self.abbreviated = False
        self.seq = 0

    def __eq__(self, other):
        if type(other) is IndexField:
            return other.nameTable == self.nameTable and other.nameIndex == self.nameIndex and other.fieldName == self.fieldName
        else:
            return False

    def __str__(self):
        cmdstr = "  INDEX-FIELD \"" + self.fieldName + "\""
        if self.order != '':
            cmdstr += " " + self.order
        if self.abbreviated:
            cmdstr += " ABBREVIATED"
        cmdstr += "\n"
        return cmdstr
