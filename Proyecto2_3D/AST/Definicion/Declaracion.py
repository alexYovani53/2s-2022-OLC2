from AST.Abstract.Instruccion import Instruccion
from AST.Expresion.Identificador import Identificador
from Entorno.RetornoType import RetornoType
from Entorno.Simbolo import Simbolo


class Declaracion(Instruccion):

    def __init__(self, identificador: Identificador, expresion, tipo, esReferencia = False):
        self.identificador = identificador
        self.valorInicializacion = expresion
        self.tipo = tipo
        self.retornoCompilado = None

        self.esReferencia = esReferencia
        self.entornoReferencia = None
        self.valorReferencia = None

    def ejecutar3D(self, entorno):
        pass