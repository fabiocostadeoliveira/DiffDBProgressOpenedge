class Sequence:
    name: str
    initial: str
    increment: str
    cycleOnLimit: str
    minVal: str
    maxVal: str

    def __init__(self):
        self.name = ""
        self.initial = ""
        self.increment = ""
        self.cycleOnLimit = ""
        self.minVal = ""
        self.maxVal = ""

    def __str__(self):
        return self.name + " - " + self.initial + " - " + self.increment + " - " + self.cycleOnLimit + " - " \
               + self.minVal + " - " + self.maxVal
