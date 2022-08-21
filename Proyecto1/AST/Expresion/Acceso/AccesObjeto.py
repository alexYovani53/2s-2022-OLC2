from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolos.Instancia import Instancia


class AccesoObjeto(Expression):


    def __init__(self,listaExpresiones):
        self.listaExpresiones = listaExpresiones

    def obtenerValor(self, entorno) -> RetornoType:


        # expresion1.expresion2....

        expresionInicial = self.listaExpresiones.pop(0)

        resultadoExpresion:RetornoType = expresionInicial.obtenerValor(entorno)

        if resultadoExpresion.tipo != TIPO_DATO.OBJETO:
            return  RetornoType()


        OBJETO: Instancia = resultadoExpresion.valor

        return self.acceso_recursivo(self.listaExpresiones,OBJETO)



    def acceso_recursivo(self, listaExpresion, Objeto:Instancia) ->RetornoType:

        expresionInicial = listaExpresion.pop(0)

        resultadoExpresion: RetornoType = expresionInicial.obtenerValor(Objeto.entornoInstancia)

        if len(listaExpresion) == 0:
            return resultadoExpresion

        else:
            if resultadoExpresion.tipo != TIPO_DATO.OBJETO:
                return RetornoType()

            OBJETO: Instancia = resultadoExpresion.valor

            return self.acceso_recursivo(listaExpresion,OBJETO)
