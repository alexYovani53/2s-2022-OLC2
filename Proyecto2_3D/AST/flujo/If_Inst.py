from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO, RetornoType


class IfInst(Instruccion):

    def __init__(self, condicion, listaInstrucionPrincipal, listaelseif, bloqueInstElse):
        self.condicion = condicion
        self.listaInstrucionPrincipal = listaInstrucionPrincipal
        self.listaelseif = listaelseif
        self.bloqueInstElse = bloqueInstElse

    def ejecutar3D(self, entorno):
        pass