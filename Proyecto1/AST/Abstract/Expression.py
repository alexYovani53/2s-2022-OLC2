from abc import ABC, abstractmethod

from Entorno.RetornoType import RetornoType


class Expression(ABC):

    @abstractmethod
    def obtenerValor(self, entorno) -> RetornoType:
        pass

