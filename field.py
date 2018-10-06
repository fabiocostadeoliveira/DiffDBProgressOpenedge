from sintaxe import sintaxe

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

    def __init__(self):
#        self.table = tb()
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
        self.nameTable = ""



    def __str__(self):
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
        self.nameTable = ""
        properties = ""
        if (self.formatt != ""):
            properties += sintaxe.PROP_QUOTE.format(prop_name="FORMAT", prop_value=self.formatt)
        if (self.initial != ""):
            properties += sintaxe.PROP_QUOTE.format(prop_name="FORMAT", prop_value=self.formatt)

        return self.name + " - " + self.label + " - " + self.formatt

    def _eq_(self, other):
        if (type(other) is Field):
            return other.nameTable == self.nameTable and other.name == self.name
        else:
            return False