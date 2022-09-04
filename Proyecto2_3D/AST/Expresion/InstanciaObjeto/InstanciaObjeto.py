from AST.Abstract.Expression import Expression
from AST.Definicion.Declaracion import Declaracion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolos.Clase import Clase
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Simbolos.Instancia import Instancia


class InstanciaObjeto(Expression):

    def __init__(self, idClase, listaExpresiones):
        self.idClase =idClase
        self.listaExpresiones = listaExpresiones


    def obtener3D(self, entorno):
        pass