from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO, RetornoType


class Return_Instr(Instruccion):

    def __init__(self, tipo, expresion):
        self.tipo = tipo
        self.expresion = expresion

    def ejecutar3D(self, entorno):
        pass

