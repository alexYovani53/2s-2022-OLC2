from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO


class Identificador(Expression):

    def __init__(self, identificador):
        self.nombre = identificador

    def obtenerValor(self, entorno) -> RetornoType:
        existeSimbolo = entorno.existeSimbolo(self.nombre)
        simbolo = entorno.obtenerSimbolo(self.nombre)

        if existeSimbolo:

            if simbolo.tipo == TIPO_DATO.OBJETO:
                return RetornoType(valor=simbolo, tipo=TIPO_DATO.OBJETO)
            else:
                return RetornoType(valor=simbolo.valor, tipo=simbolo.tipo)
