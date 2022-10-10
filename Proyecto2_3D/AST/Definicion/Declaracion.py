from AST.Abstract.Instruccion import Instruccion
from AST.Expresion.Identificador import Identificador
from Entorno.RetornoType import RetornoType
from Entorno.Simbolo import Simbolo


class Declaracion(Instruccion):

    def __init__(self, identificador: Identificador, expresion, tipo, esReferencia=False):
        self.identificador = identificador
        self.valorInicializacion = expresion
        self.tipo = tipo
        self.expresionCompilada = None

        self.esReferencia = esReferencia
        self.entornoReferencia = None
        self.valorReferencia = None

        # cambio de entorno
        self.puntero_entorno_nuevo = ""
        self.ejecuta_en_funcion = False

        # declaración en HEAP
        self.declarar_en_instancia = False

    def ejecutar3D(self, entorno):

        CODIGO_SALIDA = ""

        valorExpresion = None
        if self.valorInicializacion is not None:
            valorExpresion = self.valorInicializacion.obtener3D(entorno=entorno)
        elif self.expresionCompilada is not None:
            valorExpresion = self.expresionCompilada

        PUNTERO_ENTORNO = "SP"
        SEGMENTO_MEMORIA = "Stack"

        if self.ejecuta_en_funcion:
            PUNTERO_ENTORNO = self.puntero_entorno_nuevo

        if self.declarar_en_instancia:
            PUNTERO_ENTORNO = self.puntero_entorno_nuevo
            SEGMENTO_MEMORIA = "Heap"

        tamanioEntorno = entorno.tamanio
        temp1 = entorno.generador.obtenerTemporal()

        CODIGO_SALIDA += "/* DECLARACIÓN DE UNA VARIABLE */\n"
        CODIGO_SALIDA += valorExpresion.codigo + '\n'
        CODIGO_SALIDA += f'{temp1} = {PUNTERO_ENTORNO} + {tamanioEntorno}; \n'
        CODIGO_SALIDA += f'{SEGMENTO_MEMORIA}[(int) {temp1}] = {valorExpresion.temporal};\n'

        simbolo = Simbolo()
        simbolo.iniciarSimboloPrimitivo(self.identificador.nombre, None, self.tipo, tamanioEntorno)

        entorno.agregarSimbolo(simbolo)
        entorno.tamanio += 1

        return CODIGO_SALIDA
