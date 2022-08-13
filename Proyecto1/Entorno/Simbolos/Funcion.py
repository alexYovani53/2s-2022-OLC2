from AST.Abstract.Instruccion import Instruccion
from Entorno.Simbolo import Simbolo


class Funcion(Simbolo, Instruccion):

    def __init__(self, identificador, listaParametros, listaInstrucciones, tipo):
        super().__init__()
        super().iniciarSimboloFuncion(identificador,listaParametros,listaInstrucciones,tipo)

    def ejecutarParametros(self, entornoFuncion, expresiones: [], entornoQueLlamo) -> bool:
        declaraciones  = self.parametros

        if len(declaraciones) != len(expresiones):
            # manejo de error
            return False

        index = 0
        for declaracion in declaraciones:
            declaracion.retornoCompilado = expresiones[index].obtenerValor(entornoQueLlamo)
            declaracion.ejecutarInstr(entornoFuncion)
            index += 1

        return True

    def ejecutarInstr(self, entorno):

        for instruccion in self.instrucciones:
            instruccion.ejecutarInstr(entorno)




####  funcion ( int a, int b, int c)                funcion( expresion1, expresion2, expresion3)