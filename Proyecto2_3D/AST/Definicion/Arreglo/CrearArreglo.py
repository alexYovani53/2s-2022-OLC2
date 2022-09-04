from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO


class CrearArreglo(Instruccion):

    def __init__(self,idInstancia, dimensiones, tipo, expresion):
        self.idInstancia = idInstancia
        self.dimensiones = dimensiones
        self.tipo = tipo
        self.expresion = expresion

    def ejecutar3D(self, entorno):
        pass