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

        arreglo = InstanciaArreglo(tipo=self.tipo, valores=valores, dimensiones=dimensionesInt)
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
            valorDefecto = self.valor_defecto()
            for i in range(0, anchoNuevoInt):
                valores.insert(i, valorDefecto.valor)

        return valores


    def valor_defecto(self)-> RetornoType:

        match self.tipo:
            case TIPO_DATO.ENTERO :
                return RetornoType(valor=-1,tipo=TIPO_DATO.ENTERO)
            case TIPO_DATO.DECIMAL :
                return RetornoType(valor=0.0,tipo=TIPO_DATO.DECIMAL)
            case TIPO_DATO.CADENA :
                return RetornoType(valor="",tipo=TIPO_DATO.CADENA)
            case TIPO_DATO.BOOLEAN :
                return RetornoType(valor=False,tipo=TIPO_DATO.BOOLEAN)
