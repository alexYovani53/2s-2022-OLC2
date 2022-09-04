from enum import Enum

from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType


class Primitivo(Expression):

    def __init__(self, valor, tipoDato):
        self.valor = valor
        self.tipoDato = tipoDato

    def obtener3D(self, entorno) -> RetornoType:
        pass