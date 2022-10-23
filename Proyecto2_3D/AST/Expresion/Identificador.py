from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO


class Identificador(Expression):

    def __init__(self, identificador):
        self.nombre = identificador

        self.etiquetaVerdadera = ""
        self.etiquetaFalsa = ""

        self.retornarReferencia = False

    def obtener3D(self, entorno):

        retorno = RetornoType()
        CODIGO_SALIDA = ""

        if entorno.existeSimbolo(self.nombre):

            TEMP1 = entorno.generador.obtenerTemporal()
            TEMP2 = entorno.generador.obtenerTemporal()
            TEMP3 = entorno.generador.obtenerTemporal()
            simbolo = entorno.obtenerSimbolo(self.nombre)

            CODIGO_SALIDA += f"/* ACCEDIENDO A VARIABLE  {self.nombre}*/\n"
            CODIGO_SALIDA += f'{TEMP1} = SP + {simbolo.direccionRelativa};\n'

            if (self.retornarReferencia):
                TEMP2 = TEMP1
            else:
                CODIGO_SALIDA += f'{TEMP2} = Stack[(int) {TEMP1}];\n'

            if simbolo.referencia is True:
                CODIGO_SALIDA += f'{TEMP3} = Stack[(int) {TEMP2}];\n'

            if simbolo.tipo is TIPO_DATO.BOOLEAN and self.etiquetaVerdadera != "":
                CODIGO_SALIDA += f"if ( {TEMP2} == 1 ) goto {self.etiquetaVerdadera};\n"
                CODIGO_SALIDA += f"goto {self.etiquetaFalsa}; \n"
                retorno.etiquetaV = self.etiquetaVerdadera
                retorno.etiquetaF = self.etiquetaFalsa

            if simbolo.referencia is True:
                retorno.iniciarRetorno(CODIGO_SALIDA, "", TEMP3, simbolo.tipo)
            else:
                retorno.iniciarRetorno(CODIGO_SALIDA,"",TEMP2,simbolo.tipo)

            return retorno
        else:
            return RetornoType()
