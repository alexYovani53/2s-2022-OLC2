from Entorno.RetornoType import TIPO_DATO


class Simbolo:

    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.identificador = ""
        self.valor = None
        self.tipo = TIPO_DATO.NULL
        self.constante = False
        self.direccionRelativa = 0

        self.parametros = []
        self.instrucciones = []


        # simbolo instancia
        self.idClase = ""
        self.entornoInstancia = None

        # simbolo arreglo
        self.valores = []
        self.dimensiones = []


        # referencia
        self.referencia = False
        self.entornoReferencia = "Stack"
        self.puntero = "t1"

    def iniciarSimboloPrimitivo(self, identificador, valor, tipo, direccionRelativa, constante=False):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.constante = constante
        self.direccionRelativa = direccionRelativa

    def iniciarSimboloFuncion(self, identificador,listaParametros,listaInstrucciones, tipo, ):
        self.identificador = identificador
        self.tipo = tipo
        self.parametros = listaParametros
        self.instrucciones = listaInstrucciones

    def iniciarSimboloClase(self, idClase, listaInstrucciones):
        self.identificador = idClase
        self.instrucciones = listaInstrucciones

    def iniciarSimboloInstancia(self, idClase, idInstancia, entornoInstancia, tipo):
        self.idClase = idClase
        self.identificador = idInstancia
        self.entornoInstancia = entornoInstancia
        self.tipo = tipo

    def iniciarSimboloArreglo(self, tipo, dimensiones, valores):
        self.dimensiones =dimensiones
        self.valores = valores
        self.tipo = tipo