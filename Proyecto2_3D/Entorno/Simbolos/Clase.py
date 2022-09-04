from Entorno.Simbolo import Simbolo


class Clase(Simbolo):

    def __init__(self, idClase, listaInstrucciones):
        super().__init__()
        super().iniciarSimboloClase(idClase, listaInstrucciones)