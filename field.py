

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
        return self.name + " - " + self.label + " - " + self.formatt