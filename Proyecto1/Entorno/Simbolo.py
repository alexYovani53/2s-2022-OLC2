from Entorno.RetornoType import TIPO_DATO


class Simbolo:

    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.identificador = ""
        self.valor = None
        self.tipo = TIPO_DATO.NULL
        self.constante = False

        self.parametros = []
        self.instrucciones = []

    def iniciarSimboloPrimitivo(self, identificador, valor, tipo, constante=False):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.constante = constante

    def iniciarSimboloFuncion(self, identificador,listaParametros,listaInstrucciones, tipo, ):
        self.identificador = identificador
        self.tipo = tipo
        self.parametros = listaParametros
        self.instrucciones = listaInstrucciones
