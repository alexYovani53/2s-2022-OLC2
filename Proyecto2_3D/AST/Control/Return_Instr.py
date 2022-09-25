from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO, RetornoType


class Return_Instr(Instruccion):

    def __init__(self, tipo, expresion):
        self.tipo = tipo
        self.expresion = expresion

    def ejecutar3D(self, entorno):

        CODIGO_SALIDA = ""

        if self.expresion is None:
            return "goto SECCION_N_RETORNO; \n"
        else:
            resultadoExpresion = self.expresion.obtener3D(entorno)
            CODIGO_SALIDA += resultadoExpresion.codigo

            temporal = entorno.generador.obtenerTemporal()
            CODIGO_SALIDA += f"{temporal} = SP + 0; \n"
            CODIGO_SALIDA += f"Stack[ (int) {temporal}] = {resultadoExpresion.temporal}; \n"
            return CODIGO_SALIDA

