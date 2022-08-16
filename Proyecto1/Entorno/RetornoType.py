from enum import  IntEnum


class TIPO_DATO(IntEnum):
    ENTERO = 0,
    DECIMAL = 1,
    CADENA = 2,
    BOOLEAN = 3,
    VOID = 4,
    NULL = 5,
    OBJETO = 6,
    ARRAY = 7,
    VECTOR = 8


class RetornoType:

    def __init__(self, valor=None, tipo=TIPO_DATO.NULL):
        self.valor = valor
        self.tipo = tipo
