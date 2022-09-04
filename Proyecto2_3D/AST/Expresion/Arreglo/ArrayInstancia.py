from AST.Abstract.Expression import Expression
from Entorno.RetornoType import TIPO_DATO, RetornoType
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo


class ArrayInstancia(Expression):

    def __init__(self, tipo, dimensiones ):
        self.tipo = tipo
        self.dimensiones = dimensiones


    def obtener3D(self, entorno):
        pass

    def obtenerDimensiones(self, entorno)->[]:
        pass

    def agregarValor(self, dimensionesCompiladas) ->[]:
        pass


    def valor_defecto(self)-> RetornoType:
        pass