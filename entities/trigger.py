from core.sintaxe import sintaxe


class Trigger:

    def __init__(self):
        self._event = ""
        self.override = ""
        self.procedure = ""
        self.crc = ""
        self.table_name = ""

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, p_event):
        if p_event is not None:
            self._event = p_event

    def del_trigger_sintaxe(self):
        return sintaxe.DELETE_TRIGGER.format(event=self.event)

    def __str__(self):
        return sintaxe.ADD_TRIGGER.format(event=self.event,
                                          override=self.override,
                                          procedure=self.procedure,
                                          crc=self.crc)
