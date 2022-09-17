from AST.Abstract.Instruccion import Instruccion
from AST.Expresion.Identificador import Identificador
from Entorno.RetornoType import RetornoType
from Entorno.Simbolo import Simbolo


class Declaracion(Instruccion):

    def __init__(self, identificador: Identificador, expresion, tipo, esReferencia = False):
        self.identificador = identificador
        self.valorInicializacion = expresion
        self.tipo = tipo
        self.retornoCompilado = None

        self.esReferencia = esReferencia
        self.entornoReferencia = None
        self.valorReferencia = None

    def ejecutar3D(self, entorno):

        CODIGO_SALIDA  = ""

        if self.valorInicializacion is not None:
            valorExpresion = self.valorInicializacion.obtener3D(entorno=entorno)

            tamanioEntorno = entorno.tamanio
            temp1 = entorno.generador.obtenerTemporal()

            CODIGO_SALIDA += "/* DECLARACIÓN DE UNA VARIABLE */\n"
            CODIGO_SALIDA += valorExpresion.codigo + '\n'
            CODIGO_SALIDA += f'{temp1} = SP + {tamanioEntorno}; \n'
            CODIGO_SALIDA += f'Stack[(int) {temp1}] = {valorExpresion.temporal};\n'




            simbolo = Simbolo()
            simbolo.iniciarSimboloPrimitivo(self.identificador.nombre,None,self.tipo,tamanioEntorno)

            entorno.agregarSimbolo(simbolo)

            entorno.tamanio += 1

            return CODIGO_SALIDA