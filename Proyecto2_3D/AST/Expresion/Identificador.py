from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO


class Identificador(Expression):

    def __init__(self, identificador):
        self.nombre = identificador

    def obtener3D(self, entorno):
        pass