from enum import Enum

from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO
from main2 import Generador3DInstancia


class Primitivo(Expression):

    def __init__(self, valor, tipoDato):
        self.valor = valor
        self.tipoDato = tipoDato

        self.etiquetaVerdadera = ""
        self.etiquetaFalsa = ""

    def obtener3D(self, entorno) -> RetornoType:

        CODIGO_SALIDA = ""
        retorno = RetornoType()

        if (self.tipoDato == TIPO_DATO.ENTERO or self.tipoDato == TIPO_DATO.DECIMAL):

            temp1 = entorno.generador.obtenerTemporal()
            CODIGO_SALIDA += f'{temp1} = {self.valor};'
            retorno.iniciarRetorno(CODIGO_SALIDA,"", temp1, self.tipoDato)

        if ( self.tipoDato == TIPO_DATO.CADENA):

            temp2 = entorno.generador.obtenerTemporal()
            CODIGO_SALIDA += f'{temp2} = HP;\n'

            for caracter in self.valor:
                valor = ord(caracter)
                CODIGO_SALIDA += f'Heap[HP] ={valor}; /*{caracter}*/\n'
                CODIGO_SALIDA += f'HP = HP + 1;\n'

            CODIGO_SALIDA += f'Heap[HP] = 0;\n'
            CODIGO_SALIDA += f'HP = HP+1;\n'

            retorno.iniciarRetorno(CODIGO_SALIDA, "", temp2, self.tipoDato)

        if (self.tipoDato == TIPO_DATO.BOOLEAN):

            temp2 = entorno.generador.obtenerTemporal()
            if self.etiquetaVerdadera != "" and self.valor == True:
                CODIGO_SALIDA += f"goto {self.etiquetaVerdadera};\n"
                retorno.etiquetaV = self.etiquetaVerdadera
                retorno.etiquetaF = self.etiquetaFalsa
            elif self.etiquetaFalsa != "" and self.valor == False:
                CODIGO_SALIDA += f"goto {self.etiquetaFalsa};\n"
                retorno.etiquetaV = self.etiquetaVerdadera
                retorno.etiquetaF = self.etiquetaFalsa
            else:
                if self.valor == True:
                    CODIGO_SALIDA += f'{temp2} = 1;'
                else:
                    CODIGO_SALIDA += f'{temp2} = 0;'

            retorno.iniciarRetorno(CODIGO_SALIDA, "", temp2, self.tipoDato)


        return retorno