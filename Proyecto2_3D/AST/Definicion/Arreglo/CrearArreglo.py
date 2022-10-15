from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo


class CrearArreglo(Instruccion):

    def __init__(self, idInstancia, dimensiones, tipo, expresion):
        self.idInstancia = idInstancia
        self.dimensiones = dimensiones
        self.tipo = tipo
        self.expresion = expresion

        self.declarar_en_instancia = False

    def ejecutar3D(self, entorno):
        valorArreglo = self.expresion.obtener3D(entorno)
        #  REtornoType(
        #   tipo, codigo, temporal
        #   valor = objeto a guardar en tabla de simbolos
        #)
        if (valorArreglo.tipo != TIPO_DATO.ARRAY): return ""

        temp1 = entorno.generador.obtenerTemporal()

        CODIGO_FINAL = ""
        CODIGO_FINAL += "/*Declaración de un Arreglo*/\n"

        CODIGO_FINAL += valorArreglo.codigo
        CODIGO_FINAL += f"{temp1} = SP + {entorno.tamanio};\n"
        CODIGO_FINAL += f"Stack[(int){temp1}] = {valorArreglo.temporal};\n"


        arreglo: InstanciaArreglo = valorArreglo.valor
        arreglo.identificador = self.idInstancia
        arreglo.direccionRelativa= entorno.tamanio

        entorno.tamanio += 1

        entorno.agregarSimbolo(arreglo)

        return CODIGO_FINAL


