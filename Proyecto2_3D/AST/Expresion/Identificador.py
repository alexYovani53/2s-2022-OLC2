from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO


class Identificador(Expression):

    def __init__(self, identificador):
        self.nombre = identificador

    def obtener3D(self, entorno):


        CODIGO_SALIDA = ""

        if entorno.existeSimbolo(self.nombre):

            TEMP1 = entorno.generador.obtenerTemporal()
            TEMP2 = entorno.generador.obtenerTemporal()
            simbolo = entorno.obtenerSimbolo(self.nombre)

            CODIGO_SALIDA += f"/* ACCEDIENDO A VARIABLE  {self.nombre}*/\n"
            CODIGO_SALIDA += f'{TEMP1} = SP + {simbolo.direccionRelativa};\n'
            CODIGO_SALIDA += f'{TEMP2} = Stack[(int) {TEMP1}];\n'

            retorno =  RetornoType()
            retorno.iniciarRetorno(CODIGO_SALIDA,"",TEMP2,simbolo.tipo)
            return retorno
        else:
            return RetornoType()
