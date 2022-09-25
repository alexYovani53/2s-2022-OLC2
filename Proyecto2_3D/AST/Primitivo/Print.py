import tkinter

from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO
from main2 import Generador3DInstancia


class Print(Instruccion):

    def __init__(self, expression):
        self.expression = expression

    def ejecutar3D(self, entorno):

        CODIGO_SALIDA = ""

        valorExpresion = self.expression.obtener3D(entorno)

        if valorExpresion.tipo == TIPO_DATO.ENTERO:
            CODIGO_SALIDA += "/* IMPRIMIENDO UN VALOR ENTERO*/\n"
            CODIGO_SALIDA += valorExpresion.codigo
            CODIGO_SALIDA += f'printf(\"%d\", (int){valorExpresion.temporal}); \n'
            return CODIGO_SALIDA

        elif valorExpresion.tipo == TIPO_DATO.DECIMAL:
            CODIGO_SALIDA += "/* IMPRIMIENDO UN VALOR DECIMAL*/\n"
            CODIGO_SALIDA += valorExpresion.codigo
            CODIGO_SALIDA += f'printf(\"%f\", (float){valorExpresion.temporal}); \n'
            return CODIGO_SALIDA

        elif valorExpresion.tipo == TIPO_DATO.CADENA:

            temp1 = entorno.generador.obtenerTemporal()
            caracter = entorno.generador.obtenerTemporal()
            etqCiclo = entorno.generador.obtenerEtiqueta()
            etqSalida = entorno.generador.obtenerEtiqueta()
            etqAuxiliar = entorno.generador.obtenerEtiqueta()
            etqAuxiliar2 = entorno.generador.obtenerEtiqueta()

            CODIGO_SALIDA += "/* IMPRIMIENDO UN VALOR CADENA*/\n"
            CODIGO_SALIDA += valorExpresion.codigo
            CODIGO_SALIDA += f'{temp1} = {valorExpresion.temporal};\n'
            CODIGO_SALIDA += f'{etqCiclo}: \n'
            CODIGO_SALIDA += f'{caracter} = Heap[(int){temp1}];\n'

            CODIGO_SALIDA += f'if({caracter} != 1 ) goto {etqAuxiliar};\n'
            CODIGO_SALIDA += f'     {temp1} = {temp1} + 1;\n'
            CODIGO_SALIDA += f'{caracter} = Heap[(int){temp1}];\n'
            CODIGO_SALIDA += f'printf(\"%d\", (int){caracter}); \n'
            CODIGO_SALIDA += f'     {temp1} = {temp1} + 1;\n'
            CODIGO_SALIDA += f'got {etqCiclo}; '

            CODIGO_SALIDA += f'{etqAuxiliar}: \n'
            CODIGO_SALIDA += f'if({caracter} == 0) goto {etqSalida};\n' \
                             f'     printf(\"%c\",(char) {caracter});\n' \
                             f'     {temp1} = {temp1} + 1;\n' \
                             f'     goto {etqCiclo};\n'

            CODIGO_SALIDA += f'{etqSalida}:\n'
            return CODIGO_SALIDA
