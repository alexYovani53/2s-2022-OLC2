from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo


class AccesoArreglo(Expression):

    def __init__(self, idArreglo, listaExpresiones):
        self.idArreglo = idArreglo
        self.listaExpresiones = listaExpresiones


    def obtener3D(self, entorno):
        pass


    def compilarDimensiones(self, entorno ):
        pass