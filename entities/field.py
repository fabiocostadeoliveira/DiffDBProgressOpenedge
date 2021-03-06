from core.sintaxe import sintaxe


class Field:
    name: str
    nameTable: str
    typeField: str
    formatt: str
    initial:str
    label: str
    position: str
    maxWidth: str
    columnLabel: str
    valExp: str
    valMsg: str
    help: str
    order: str
    decimals: str
    description: str
    extent: str
    mandatory: bool


    def __init__(self):
        self.name = ""
        self.formatt = ""
        self.initial = ""
        self.label = ""
        self.position = ""
        self.maxWidth = ""
        self.columnLabel = ""
        self.valExp = ""
        self.valMsg = ""
        self.help = ""
        self.order = ""
        self.decimals = ""
        self._nameTable = ""
        self.description = ""
        self.extent = ""
        self.mandatory = False


    @property
    def nameTable(self):
        return self._nameTable

    @nameTable.setter
    def nameTable(self, pnameTable):
        self._nameTable = pnameTable.lower()

    def __str__(self):
        properties = ""
        dif = False
        if self.description != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="DESCRIPTION", prop_value=self.description)
        if self.formatt != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="FORMAT", prop_value=self.formatt)
        if self.initial != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="INITIAL", prop_value=self.initial)
        if self.label != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="LABEL", prop_value=self.label)
        if self.position != "":
            dif = True
            properties += sintaxe.PROP_NOT_QUOTE.format(prop_name="POSITION", prop_value=self.position)
        if self.columnLabel != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="COLUMN-LABEL", prop_value=self.columnLabel)
        if self.help != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="HELP", prop_value=self.help)
        if self.decimals != "":
            dif = True
            properties += sintaxe.PROP_NOT_QUOTE.format(prop_name="DECIMALS", prop_value=self.decimals)
        if self.extent != "":
            dif = True
            properties += sintaxe.PROP_NOT_QUOTE.format(prop_name="EXTENT", prop_value=self.extent)
        if self.order != "":
            dif = True
            properties += sintaxe.PROP_NOT_QUOTE.format(prop_name="ORDER", prop_value=self.order)

        if dif:
            return sintaxe.ADD_FIELD_ALL.format(
                fieldName=self.name,
                tableName=self.nameTable,
                type=self.typeField,
                properties=properties)

    def _eq_(self, other):
        if type(other) is Field:
            return other.nameTable == self.nameTable and other.name == self.name
        else:
            return False
