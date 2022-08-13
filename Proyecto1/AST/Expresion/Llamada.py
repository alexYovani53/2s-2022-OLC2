from AST.Abstract.Expression import Expression
from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import RetornoType


class Llamada(Instruccion, Expression):

    def __init__(self, identificador, listaExpresiones):
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def obtenerValor(self, entorno) -> RetornoType:

        existeFuncion = entorno.existeFuncion(self.identificador)

        if not existeFuncion:
            # manejo de error
            return RetornoType()

        ENTORNO_FUNCION = EntornoTabla(entorno.consola,entorno.padre)
        funcion = entorno.obtenerFuncion(self.identificador)

        ejecutoParametros = funcion.ejecutarParametros(ENTORNO_FUNCION, self.listaExpresiones, entorno)

        if not ejecutoParametros:
            # manejo de errores
            return RetornoType()

        funcion.ejecutarInstr(entorno)

    def ejecutarInstr(self, entorno):
        self.obtenerValor(entorno)