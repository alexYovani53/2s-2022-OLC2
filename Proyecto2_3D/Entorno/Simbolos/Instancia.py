from Entorno.RetornoType import TIPO_DATO
from Entorno.Simbolo import Simbolo


class Instancia(Simbolo):

    def __init__(self,idClase, idInstancia, entornoInstancia):
        super().__init__()
        super().iniciarSimboloInstancia(idClase, idInstancia, entornoInstancia, TIPO_DATO.OBJETO)