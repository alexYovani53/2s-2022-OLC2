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

    def __init__(self, tipo=TIPO_DATO.NULL):
        self.codigo = ""
        self.etiqueta = ""
        self.temporal = ""
        self.tipo = tipo
        self.etiquetaV = ""
        self.etiquetaF = ""
        self.valor = None

    def iniciarRetorno(self, codigo, etiqueta, temporal, tipo):
        self.codigo = codigo
        self.temporal = temporal
        self.etiqueta = etiqueta
        self.tipo = tipo

    def iniciarRetornoInstancia(self, codigo, temporal, tipo, OBJETO):
        self.codigo = codigo
        self.temporal = temporal
        self.tipo = tipo
        self.valor = OBJETO


    def iniciarRetornoArreglo(self, codigo, temporal, tipo, ARREGLO):
        self.codigo = codigo
        self.temporal = temporal
        self.tipo = tipo
        self.valor = ARREGLO