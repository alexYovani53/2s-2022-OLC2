from Entorno.Simbolo import Simbolo
from Entorno.Simbolos.Funcion import Funcion


class EntornoTabla:

    def __init__(self, consola, padre = None):
        self.padre = padre
        self.tabla = {}
        self.tablaFunciones = {}
        self.consola = consola

    def existeSimbolo(self,identificador):
        entorno = self

        while entorno is not None:
            existe = entorno.tabla.get(identificador)
            if existe is not None:
                return True
            else:
                entorno = entorno.padre

        return False

    def existeSimboloEnEntornoActual(self,identificador):
        existe = self.tabla.get(identificador)
        if existe is not None:
            return True
        else:
            return False

    def obtenerSimbolo(self,identificador) -> Simbolo:
        entorno = self
        while entorno is not None:
            simbolo = entorno.tabla.get(identificador)
            if simbolo is not None:
                return simbolo
            else:
                entorno = entorno.padre

        return Simbolo()

    def agregarSimobolo(self,simboloAdd:Simbolo):
        self.tabla[simboloAdd.identificador] = simboloAdd



#  --- MANEJO DE FUNCIONES

    def existeFuncion (self,identificador):
        entorno = self

        while entorno is not None:
            existe = entorno.tablaFunciones.get(identificador)
            if existe is not None:
                return True
            else:
                entorno = entorno.padre

        return False

    def obtenerFuncion(self,identificador) -> Funcion:
        entorno = self
        while entorno is not None:
            simbolo = entorno.tablaFunciones.get(identificador)
            if simbolo is not None:
                return simbolo
            else:
                entorno = entorno.padre

        return None

    def agregarFuncion(self,funcionAdd:Funcion):
        self.tablaFunciones[funcionAdd.identificador] = funcionAdd
