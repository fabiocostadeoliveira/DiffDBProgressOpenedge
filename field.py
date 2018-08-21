from table import Table

class Field:

    table: Table
    name: str
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
        self.table = Table()
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

    def __str__(self):
        return self.name + " - " + self.label + " - " + self.formatt