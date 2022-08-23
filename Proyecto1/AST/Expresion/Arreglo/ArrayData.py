from AST.Abstract.Expression import Expression
from Entorno.RetornoType import TIPO_DATO, RetornoType
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo


class ArrayData(Expression):

    def __init__(self, listaExpresiones):
        self.expresiones = listaExpresiones

    def obtenerValor(self, entorno) -> RetornoType:

        tipo = TIPO_DATO.NULL
        expresionesCompiladas = []

        # COMPILAR EXPRESIONES, OBTENER TAMAÑO DE CADA DIMENSION Y VALIDAR CONGRUENCIA DE TIPOS
        for i in range(0, len(self.expresiones)):
            expresion = self.expresiones[i]
            valorExpresion = expresion.obtenerValor(entorno)

            if i == 0:
                tipo = valorExpresion.tipo
                expresionesCompiladas.append(valorExpresion)
            else:
                if tipo != valorExpresion.tipo:
                    print(f"Los tipos dejaron de coinciddir")
                    return RetornoType()
                else:
                    expresionesCompiladas.append(valorExpresion)

        
        # ahora creamos la data
        
        listaDimensiones  = []
        valores = []
        listaDimensiones.append(len(expresionesCompiladas)) # TAMAÑO DE LA DIMENSION 1
        tipoFinal = TIPO_DATO.NULL

        for i in range(0, len(expresionesCompiladas)):
            expresionCompilada = expresionesCompiladas[i]

            if expresionCompilada.tipo != TIPO_DATO.ARRAY:
                tipoFinal = expresionCompilada.tipo
                valores.append(expresionCompilada.valor)
                continue

            else:
                instanciaArray = expresionCompilada.valor
                if i == 0:
                    tipoFinal = instanciaArray.tipo
                    listaDimensiones.extend(instanciaArray.dimensiones)
                else:
                    if instanciaArray.tipo != tipoFinal: return RetornoType()

                valores.insert(i, instanciaArray.valores)


        instanciaArrayRetorno = InstanciaArreglo(tipoFinal, listaDimensiones, valores)
        return RetornoType(valor=instanciaArrayRetorno,tipo=TIPO_DATO.ARRAY)


        
        
