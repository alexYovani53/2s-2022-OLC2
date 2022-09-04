from AST.Abstract.Instruccion import Instruccion
from Entorno.Simbolos.Clase import Clase


class GuardarClase(Instruccion):

    def __init__(self, idClase, listaInstrucciones):
        self.idClase = idClase
        self.listaInstrucciones = listaInstrucciones

    def ejecutar3D(self, entorno):
        pass


    def __str__(self):
        return f"GuardarClase ({self.idClase})"