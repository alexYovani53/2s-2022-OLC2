from AST.Abstract.Instruccion import Instruccion
from Entorno.Simbolos.Clase import Clase


class GuardarClase(Instruccion):

    def __init__(self, idClase, listaInstrucciones):
        self.idClase = idClase
        self.listaInstrucciones = listaInstrucciones

    def ejecutar3D(self, entorno):
        if entorno.existeClase(self.idClase): return ""
        entorno.agregarClase(Clase(idClase=self.idClase,listaInstrucciones= self.listaInstrucciones))
        pass


    def __str__(self):
        return f"GuardarClase ({self.idClase})"