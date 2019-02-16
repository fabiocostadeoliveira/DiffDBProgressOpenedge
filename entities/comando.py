import abc

class Comando(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getId(self):
        return