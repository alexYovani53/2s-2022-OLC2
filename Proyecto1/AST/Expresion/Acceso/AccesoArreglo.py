from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo


class AccesoArreglo(Expression):

    def __init__(self, idArreglo, listaExpresiones):
        self.idArreglo = idArreglo
        self.listaExpresiones = listaExpresiones

    def obtenerValor(self, entorno) -> RetornoType:

        if entorno.existeSimbolo(self.idArreglo) is not True:
            return RetornoType()

        arreglo = entorno.obtenerSimbolo(self.idArreglo)
        if isinstance(arreglo, InstanciaArreglo) is not True:
            return RetornoType()

        if len(self.listaExpresiones) != len(arreglo.dimensiones):
            return RetornoType()

        dimensiones = self.compilarDimensiones(entorno)

        valor = arreglo.ObtenerValor(dimensiones,0,arreglo.valores)
        return RetornoType(valor = valor, tipo=arreglo.tipo)


    def compilarDimensiones(self, entorno ):
        listaDimensiones = []

        for dim in self.listaExpresiones:
            dimVal = dim.obtenerValor(entorno)
            # operador ternario      hacer_si_true if condicion else hacer_si_false
            if dimVal.tipo != TIPO_DATO.ENTERO:
                return
            else:
                listaDimensiones.append(dimVal.valor)

        return listaDimensiones
