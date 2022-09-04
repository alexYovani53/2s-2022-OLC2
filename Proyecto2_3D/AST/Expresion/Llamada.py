from AST.Abstract.Expression import Expression
from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import RetornoType


class Llamada(Instruccion, Expression):

    def __init__(self, identificador, listaExpresiones):
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def obtener3D(self, entorno) -> RetornoType:
        pass

    def ejecutar3D(self, entorno):
        pass