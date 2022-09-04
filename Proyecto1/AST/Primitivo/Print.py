import tkinter

from AST.Abstract.Instruccion import Instruccion


class Print(Instruccion):

    def __init__(self, expression):
        self.expression = expression

    def ejecutarInstr(self, entorno):

        retorno = self.expression.obtenerValor(entorno)

        entorno.consola.consola +=  f"{retorno.valor} \n"