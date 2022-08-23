from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO


class CrearArreglo(Instruccion):

    def __init__(self,idInstancia, dimensiones, tipo, expresion):
        self.idInstancia = idInstancia
        self.dimensiones = dimensiones
        self.tipo = tipo
        self.expresion = expresion

    def ejecutarInstr(self, entorno):

        expresionArreglo = self.expresion.obtenerValor(entorno)

        if expresionArreglo.tipo != TIPO_DATO.ARRAY:
            return


        objetoArreglo = expresionArreglo.valor

        if objetoArreglo.tipo != self.tipo:
            return

        if entorno.existeSimbolo(self.idInstancia):
            return

        objetoArreglo.identificador = self.idInstancia
        entorno.agregarSimbolo(objetoArreglo)