from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import RetornoType, TIPO_DATO


class CrearInstanciaObjeto(Instruccion):

    def __init__(self,idClase, idInstancia, expresion):
        self.idClase = idClase
        self.idInstancia = idInstancia
        self.expresion = expresion
        self.valorCompilador = None

    def ejecutarInstr(self, entorno):

        existeClase = entorno.existeClase(self.idClase)

        if existeClase is not True:
            print(f"la clase {self.idClase} no existe")
            return

        existeInstancia = entorno.existeSimbolo(self.idInstancia)
        if existeInstancia:
            print(f"La instancia ya esta creada {self.idInstancia}")
            return

        expresionInstancia: RetornoType = self.expresion.obtenerValor(entorno)

        if expresionInstancia.tipo != TIPO_DATO.OBJETO:
            print(f"la expresion no es una instancia")
            return

        if expresionInstancia.valor.idClase != self.idClase:
            print(f"las clases no coiciden")
            return

        instanciaSimbolo = expresionInstancia.valor
        instanciaSimbolo.identificador = self.idInstancia

        entorno.agregarSimbolo(instanciaSimbolo)
