from abc import ABC, abstractmethod

from Entorno.RetornoType import RetornoType


class Expression(ABC):

    @abstractmethod
    def obtener3D(self, entorno) -> RetornoType:
        pass

