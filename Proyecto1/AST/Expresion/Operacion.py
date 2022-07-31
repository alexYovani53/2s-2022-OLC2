from enum import Enum

from AST.Abstract.Expression import Expression

class TIPO_OPERACION(Enum):
    SUMA = 1,
    RESTA = 2

class Operacion(Expression):

    def __init__(self, exprIzq, tipo_operacion, exprDer):
        self.exprIzq = exprIzq
        self.tipo_operacion = tipo_operacion
        self.exprDer = exprDer

    def obtenerValor(self, entorno):

        if self.tipo_operacion == TIPO_OPERACION.SUMA:

            valorIzq = self.exprIzq.obtenerValor(None)
            valorDer = self.exprDer.obtenerValor(None)

            resultado = valorIzq + valorDer

            return f"el valor es  {resultado}"