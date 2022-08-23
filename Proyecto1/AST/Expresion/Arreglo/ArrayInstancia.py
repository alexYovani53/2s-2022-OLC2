from AST.Abstract.Expression import Expression
from Entorno.RetornoType import TIPO_DATO, RetornoType
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo


class ArrayInstancia(Expression):

    def __init__(self, tipo, dimensiones ):
        self.tipo = tipo
        self.dimensiones = dimensiones

    def obtenerValor(self, entorno) -> RetornoType:

        dimensionesCompiladas:[] = self.obtenerDimensiones(entorno)
        dimensionesInt = []
        for retornoType in dimensionesCompiladas:
            dimensionesInt.append(retornoType.valor)
        valores = self.agregarValor(dimensionesCompiladas)

        arreglo = InstanciaArreglo(tipo=TIPO_DATO.ENTERO, valores=valores, dimensiones=dimensionesInt)
        return RetornoType(valor=arreglo, tipo=TIPO_DATO.ARRAY )

    def obtenerDimensiones(self, entorno)->[]:

        listaDimensiones = []

        for dim in self.dimensiones:
            valor = dim.obtenerValor(entorno)
            if valor.tipo != TIPO_DATO.ENTERO:
                return []

            listaDimensiones.append(valor)

        return listaDimensiones

    def agregarValor(self, dimensionesCompiladas) ->[]:

        anchoNuevo = dimensionesCompiladas.pop(0)
        anchoNuevoInt = anchoNuevo.valor

        valores = []
        if len(dimensionesCompiladas) > 0:

            subArreglo = self.agregarValor(dimensionesCompiladas)
            for i in range(0, anchoNuevoInt):
                valores.insert(i, subArreglo)
        else:
            for i in range(0, anchoNuevoInt):
                valores.insert(i, 50)

        return valores