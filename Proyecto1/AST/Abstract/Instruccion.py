from abc import ABC, abstractmethod


class Instruccion(ABC):

    @abstractmethod
    def ejecutarInstr(self, entorno):
        pass