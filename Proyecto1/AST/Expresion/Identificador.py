from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType


class Identificador(Expression):

    def __init__(self, identificador):
        self.nombre = identificador

    def obtenerValor(self, entorno) -> RetornoType:
        existeSimbolo = entorno.existeSimbolo(self.nombre)
        simbolo = entorno.obtenerSimbolo(self.nombre)

        if existeSimbolo:
            return RetornoType(valor=simbolo.valor, tipo=simbolo.tipo)
