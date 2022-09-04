from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolos.Instancia import Instancia


class AccesoObjeto(Expression):


    def __init__(self,listaExpresiones):
        self.listaExpresiones = listaExpresiones

    def obtener3D(self, entorno) -> RetornoType:
        pass


    def acceso_recursivo(self, listaExpresion, Objeto:Instancia) ->RetornoType:
        pass