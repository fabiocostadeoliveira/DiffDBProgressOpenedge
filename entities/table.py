from core.sintaxe import sintaxe
from core import constants as consts

class Table:

    name: str
    area: str
    label: str
    description: str
    dump_name: str
    triggers: list
    fields: dict
    indexes: dict

    def __init__(self):
        self._name = str()
        self.area = str()
        self.label = str()
        self.description = str()
        self.dump_name = str()
        #self.table_trigger = list()
        self._triggers = list()
        self.fields = dict()
        self.indexes = dict()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, pname):
        if pname is not None:
            self._name = pname.lower()

    @property
    def triggers(self):
        return self._triggers

    @triggers.getter
    def triggers(self):
        self._triggers.sort(key=lambda trigger: trigger.event, reverse=False)
        return self._triggers

    @triggers.setter
    def triggers(self, list_triggers):
        self._triggers = list_triggers

    def addField(self, field):
        self.fields.update({field.name: field})

    def addIndex(self, index):
        self.indexes.update({index.name.lower(): index})

    def addTrigger(self, trigger):
        self._triggers.append(trigger)

    def get_sort_triggers_by_event_name(self):
        self._triggers.sort(key=lambda trigger: trigger.event, reverse=False)
        return self._triggers


    def __str__(self):
        properties = ""
        triggers = ""
        dif = False
       # print('area=' + self.area + str(self.area != None) )
       # if (self.area != ""):
       #     dif = True
       #     properties += sintaxe.PROP_QUOTE.format(prop_name="AREA", prop_value=self.area)
        if self.label != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="LABEL", prop_value=self.label)
        if self.description != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="DESCRIPTION", prop_value=self.description)
        if self.dump_name != "":
            dif = True
            properties += sintaxe.PROP_QUOTE.format(prop_name="DUMP-NAME", prop_value=self.dump_name)
        if len(self.triggers) > 0:
            for idx, t in enumerate(self.triggers):
                triggers += str(t)
        if dif:
            return sintaxe.ADD_TABLE_ALL.format(tableName=self.name, properties=properties, triggers=triggers)

    def _eq_(self, other):
        if type(other) is Table:
            return other.name == self.name
        else:
            return False

    def trigger_to_string(self):
        triggers = ""
        for t in self.triggers:
            triggers += str(t)
        return triggers


