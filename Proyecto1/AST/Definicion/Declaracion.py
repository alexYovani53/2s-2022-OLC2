from AST.Abstract.Instruccion import Instruccion
from AST.Expresion.Identificador import Identificador
from Entorno.RetornoType import RetornoType
from Entorno.Simbolo import Simbolo


class Declaracion(Instruccion):

    def __init__(self, identificador: Identificador, expresion, tipo):
        self.identificador = identificador
        self.valorInicializacion = expresion
        self.tipo = tipo
        self.retornoCompilado = None

    def ejecutarInstr(self, entorno):

        if self.valorInicializacion is not None or self.retornoCompilado is not None:

            retornoExpresion = RetornoType()
            if self.valorInicializacion is not None:
                retornoExpresion = self.valorInicializacion.obtenerValor(entorno)
            else:
                retornoExpresion = self.retornoCompilado

            tipoDeclaracion = self.tipo
            tipoExpresion = retornoExpresion.tipo

            if tipoDeclaracion != tipoExpresion:
                # manejo de errores
                return

            existeSimbolo = entorno.existeSimbolo(self.identificador.nombre)
            if existeSimbolo:
                # manejo de errores
                return

            newSimbolo = Simbolo()
            newSimbolo.iniciarSimboloPrimitivo(self.identificador.nombre, retornoExpresion.valor, tipo=self.tipo)

            entorno.agregarSimobolo(newSimbolo)


        else:
            pass
