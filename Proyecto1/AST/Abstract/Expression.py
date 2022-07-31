from abc import ABC, abstractmethod


class Expression(ABC):

    @abstractmethod
    def obtenerValor(self, entorno):
        pass

