from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO, RetornoType


class Return_Instr(Instruccion):

    def __init__(self, tipo, expresion):
        self.tipo = tipo
        self.expresion = expresion

    def ejecutarInstr(self, entorno):

        if self.tipo == TIPO_DATO.VOID:
            return RetornoType(0, TIPO_DATO.VOID)
        else:
            valorRetorno = self.expresion.obtenerValor(entorno)
            return valorRetorno
