from AST.Abstract.Expression import Expression
from Entorno.RetornoType import TIPO_DATO, RetornoType
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo


class ArrayData(Expression):

    def __init__(self, listaExpresiones):
        self.expresiones = listaExpresiones
        self.tipo = TIPO_DATO.NULL

    def obtener3D(self, entorno):

        CODIGO_FINAL = ""
        listaDimensiones = []
        temp1 = entorno.generador.obtenerTemporal()
        temp2 = entorno.generador.obtenerTemporal()

        CODIGO_FINAL += f"{temp1} = HP;/*Posicion de referencia en HEAP*/\n"
        expresionesCompiladas = self.expresionesCompiladas(entorno)

        listaDimensiones.append(len(expresionesCompiladas)) # ALMACENAR EL TAMAÑO DE UNA DIMENSION
        CODIGO_FINAL += f"HP = HP + {len(expresionesCompiladas) + 1};  \n"
        CODIGO_FINAL += f"Heap[(int) {temp1} ] = {len(expresionesCompiladas)}; /*Valor que almacena el tamaño*/\n"
        index = 1

        for expr in expresionesCompiladas:
            if (expr.tipo == TIPO_DATO.ARRAY):
                CODIGO_FINAL += "/* referenciando a un sub-arreglo*/\n"
                CODIGO_FINAL += expr.codigo +"\n"
                CODIGO_FINAL += f"{temp2} = {temp1} + {index};\n"
                CODIGO_FINAL += f"Heap[(int) {temp2}] = {expr.temporal};\n"
                if(index == 1 ):
                    listaDimensiones.extend(expr.valor.dimensiones)  # ALMACENAR EL TAMAÑO DE UNA DIMENSION
            else:
                CODIGO_FINAL += "/* almacenando un valor String, bool, int o float */\n"
                CODIGO_FINAL += expr.codigo + "\n"
                CODIGO_FINAL += f"{temp2} = {temp1} + {index};\n"
                CODIGO_FINAL += f"Heap[(int) {temp2}] = {expr.temporal};\n"
            index += 1

        instanciaArreglo = InstanciaArreglo(TIPO_DATO.CADENA, listaDimensiones, None)
        retorno = RetornoType()
        retorno.iniciarRetornoArreglo(CODIGO_FINAL, temp1, TIPO_DATO.ARRAY, instanciaArreglo)
        return retorno

    def expresionesCompiladas(self, entorno):
        expresiones = []

        contador = 0
        for expr in self.expresiones:
            resultadoExpr = expr.obtener3D(entorno)
            if contador == 0:
                self.tipo = resultadoExpr.tipo
            else:
                if (self.tipo != resultadoExpr.tip):
                    return []
            expresiones.append(resultadoExpr)

        return expresiones

    def asignarValores(self, listaExpresionesCompiladas):
        for expr in listaExpresionesCompiladas:
            if (expr.tipo == TIPO_DATO.ARRAY):
                pass
            else:
                pass
