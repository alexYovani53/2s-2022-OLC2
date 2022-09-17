from AST.Abstract.Expression import Expression
from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import RetornoType


class Llamada(Instruccion, Expression):

    def __init__(self, identificador, listaExpresiones):
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def obtener3D(self, entorno) -> RetornoType:
        pass

    def ejecutar3D(self, entorno):

        CODIGO_SALIDA = ""

        if entorno.existeFuncion(self.identificador):

            funcion = entorno.obtenerFuncion(self.identificador)

            CODIGO_SALIDA += f"/* LLAMADA A FUNCION {self.identificador}*/\n"

            ENTORNO_FUNCION = EntornoTabla(entorno.generador, entorno)
            ENTORNO_FUNCION.tamanio = 1

            CODIGO_SALIDA += f"SP = SP + {entorno.tamanio};\n"
            CODIGO_SALIDA += f"{self.identificador}();\n"
            CODIGO_SALIDA += f"SP = SP - {entorno.tamanio};\n"

            return CODIGO_SALIDA