from table import Table

class Field:

    table: Table
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

    def __init__(self):
        self.table = Table()
        self.formatt = None
        self.initial = None
        self.label = None
        self.position = None
        self.maxWidth = None
        self.column_label = None
        self.valExp = None
        self.valMsg = None
        self.help = None
        self.order = None