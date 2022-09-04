from abc import ABC, abstractmethod


class Instruccion(ABC):

    @abstractmethod
    def ejecutar3D(self, entorno):
        pass