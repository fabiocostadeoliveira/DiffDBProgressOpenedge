class Table:

    name: str
    area: str
    label: str
    description: str
    dumpName: str
    tableTrigger: list
    fields: list
    indexes: list

    def __init__(self):
        self.name          = str()
        self.area          = str()
        self.label         = str()
        self.description   = str()
        self.dump_name     = str()
        self.table_trigger = list()
        self.fields        = list()
        self.indexes       = list()

    def __str__(self):
        return self.name + " - " + self.dump_name + " - " + self.label + " - " + self.area + " - " + self.description




