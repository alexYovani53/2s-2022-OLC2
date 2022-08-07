from Entorno.RetornoType import TIPO_DATO


class Simbolo:

    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.identificador = ""
        self.valor = None
        self.tipo = TIPO_DATO.NULL
        self.constante = False

    def iniciarSimboloPrimitivo(self, identificador, valor, tipo, constante=False):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.constante = constante
