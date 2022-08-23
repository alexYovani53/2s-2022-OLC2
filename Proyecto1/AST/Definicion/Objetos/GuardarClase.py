from AST.Abstract.Instruccion import Instruccion
from Entorno.Simbolos.Clase import Clase


class GuardarClase(Instruccion):

    def __init__(self, idClase, listaInstrucciones):
        self.idClase = idClase
        self.listaInstrucciones = listaInstrucciones

    def ejecutarInstr(self, entorno):

        existeClase = entorno.existeClase(self.idClase)

        if existeClase:
            #manejo de error
            print("La clase ya existe")
            return

        claseNueva = Clase(self.idClase,self.listaInstrucciones)
        entorno.agregarClase(claseNueva)

    def __str__(self):
        return f"GuardarClase ({self.idClase})"