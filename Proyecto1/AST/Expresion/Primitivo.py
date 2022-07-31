from enum import Enum

from AST.Abstract.Expression import Expression

class TIPO_DATO(Enum):
    ENTERO = 0,
    DECIMAL = 1


class Primitivo(Expression):

    def __init__(self, valor, tipoDato):
        self.valor = valor
        self.tipoDato = tipoDato

    def obtenerValor(self, entorno):
        return self.valor