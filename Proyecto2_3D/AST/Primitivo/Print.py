import tkinter

from AST.Abstract.Instruccion import Instruccion


class Print(Instruccion):

    def __init__(self, expression):
        self.expression = expression

    def ejecutar3D(self, entorno):
        pass