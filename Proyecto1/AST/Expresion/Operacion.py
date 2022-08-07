from enum import Enum

from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO


class TIPO_OPERACION(Enum):
    SUMA = 1,
    RESTA = 2,
    MULTIPLICACION = 3,
    DIVISION = 4,
    MENOR = 5,
    MAYOR = 6,
    MENORIGUAL = 7,
    MAYORIGUAL = 8,
    DIFERENTE = 9,
    IGUALIGUAL = 10,
    AND = 11,
    OR = 12,
    NOT = 13,


class Operacion(Expression):
    sumaDominante = [
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.DECIMAL, TIPO_DATO.DECIMAL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.CADENA, TIPO_DATO.CADENA, TIPO_DATO.CADENA, TIPO_DATO.CADENA, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
    ]

    restaMultiplicacionDivison = [
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.DECIMAL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
    ]

    def __init__(self, exprIzq, tipo_operacion, exprDer, unario=False):
        self.exprIzq = exprIzq
        self.tipo_operacion = tipo_operacion
        self.exprDer = exprDer
        self.unario = unario

    def obtenerValor(self, entorno):

        retornoIzq = RetornoType()
        retornoDer = RetornoType()
        retornoUnario = RetornoType()

        if self.unario:
            retornoUnario = self.exprIzq.obtenerValor(entorno)
        else:
            retornoIzq = self.exprIzq.obtenerValor(entorno)
            retornoDer = self.exprDer.obtenerValor(entorno)

        match self.tipo_operacion:
            case TIPO_OPERACION.SUMA:
                tipoResultante = Operacion.sumaDominante[retornoIzq.tipo][retornoDer.tipo]

                if tipoResultante == TIPO_DATO.ENTERO:
                    return RetornoType(valor=(retornoIzq.valor + retornoDer.valor), tipo=tipoResultante)
                elif tipoResultante == TIPO_DATO.DECIMAL:
                    return RetornoType(valor=(retornoIzq.valor + retornoDer.valor), tipo=tipoResultante)
                elif tipoResultante == TIPO_DATO.CADENA:
                    return RetornoType(valor=(str(retornoIzq.valor) + str(retornoDer.valor)), tipo=tipoResultante)
                elif tipoResultante == TIPO_DATO.NULL:
                    print(f"ERROOOOOOOOOOOR, NO SE PUEDE OPERAR {retornoIzq.tipo} con {retornoDer.tipo}")
                    return RetornoType()

            case TIPO_OPERACION.RESTA:
                if self.unario:
                    return RetornoType(valor=(retornoUnario.valor * -1), tipo=retornoUnario.tipo)
                else:
                    tipoResultante = Operacion.restaMultiplicacionDivison[retornoIzq.tipo][retornoDer.tipo]

                    if tipoResultante == TIPO_DATO.ENTERO:
                        return RetornoType(valor=(retornoIzq.valor - retornoDer.valor), tipo=tipoResultante)
                    elif tipoResultante == TIPO_DATO.DECIMAL:
                        return RetornoType(valor=(retornoIzq.valor - retornoDer.valor), tipo=tipoResultante)
                    elif tipoResultante == TIPO_DATO.NULL:
                        print(f"ERROOOOOOOOOOOR, NO SE PUEDE OPERAR {retornoIzq.tipo} con {retornoDer.tipo}")
                        return RetornoType()
