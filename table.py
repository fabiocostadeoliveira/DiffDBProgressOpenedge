class Table:

    area: str
    label: str
    description: str
    dumpName: str
    tableTrigger: list
    fields: list
    indexes: list

    def __init__(self):
        self.area          = None
        self.label         = None
        self.description   = None
        self.dump_name     = None
        self.table_trigger = list()
        self.fields        = list()
        self.indexes       = list()




