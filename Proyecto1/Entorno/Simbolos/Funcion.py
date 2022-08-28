from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolo import Simbolo


class Funcion(Simbolo, Instruccion):


    comparacionTipo = [
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.DECIMAL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.BOOLEAN, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.VOID],
    ]

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

            if declaracion.esReferencia is True:
                declaracion.entornoReferencia = entornoQueLlamo
                declaracion.valorReferencia =  expresiones[index]

            declaracion.retornoCompilado = expresiones[index].obtenerValor(entornoQueLlamo)
            declaracion.ejecutarInstr(entornoFuncion)
            index += 1

        return True

    def ejecutarInstr(self, entorno):

        for instruccion in self.instrucciones:

            if instruccion is None: continue
            valorRetorno = instruccion.ejecutarInstr(entorno)

            if valorRetorno is not None:

                if isinstance(valorRetorno, RetornoType):

                    validarTipo = Funcion.comparacionTipo[self.tipo][valorRetorno.tipo]

                    if validarTipo is not TIPO_DATO.NULL:

                        return valorRetorno

                    else:
                        #manejo de errores
                        return RetornoType()


    def __str__(self):
        return f"Funcion {self.identificador}"