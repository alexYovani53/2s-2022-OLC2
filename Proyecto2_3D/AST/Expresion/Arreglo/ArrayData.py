from AST.Abstract.Expression import Expression
from Entorno.RetornoType import TIPO_DATO, RetornoType
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo


class ArrayData(Expression):

    def __init__(self, listaExpresiones):
        self.expresiones = listaExpresiones


    def obtener3D(self, entorno):
        pass