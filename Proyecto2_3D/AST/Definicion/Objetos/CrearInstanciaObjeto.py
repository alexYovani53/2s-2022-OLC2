from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import RetornoType, TIPO_DATO


class CrearInstanciaObjeto(Instruccion):

    def __init__(self,idClase, idInstancia, expresion):
        self.idClase = idClase
        self.idInstancia = idInstancia
        self.expresion = expresion
        self.valorCompilador = None

    def ejecutar3D(self, entorno):
        pass