from AST.Abstract.Expression import Expression
from AST.Abstract.Instruccion import Instruccion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import RetornoType, TIPO_DATO


class Llamada(Instruccion, Expression):

    def __init__(self, identificador, listaExpresiones):
        self.identificador = identificador
        self.listaExpresiones = listaExpresiones

    def obtener3D(self, entorno) -> RetornoType:

        CODIGO_SALIDA = ""

        if entorno.existeFuncion(self.identificador) is False:
            return RetornoType()

        funcion = entorno.obtenerFuncion(self.identificador)
        CODIGO_SALIDA += f"/* LLAMADA A FUNCION {self.identificador}*/\n"

        ENTORNO_FUNCION = EntornoTabla(entorno.generador, entorno)
        ENTORNO_FUNCION.tamanio = 1

        puntero_entorno_nuevo = entorno.generador.obtenerTemporal()
        CODIGO_SALIDA += f"{puntero_entorno_nuevo} = SP + {entorno.tamanio};\n"

        codigoParametros = funcion.ejecutarParametros(ENTORNO_FUNCION, self.listaExpresiones, entorno,
                                                      puntero_entorno_nuevo)

        self.verificar_funcion_generada(ENTORNO_FUNCION, funcion)

        CODIGO_SALIDA += codigoParametros
        CODIGO_SALIDA += f"SP = SP + {entorno.tamanio};\n"
        CODIGO_SALIDA += f"{self.identificador}();\n"
        CODIGO_SALIDA += f"SP = SP - {entorno.tamanio};\n"




        TEMPORAL = entorno.generador.obtenerTemporal()
        TEMPORAL2 = entorno.generador.obtenerTemporal()

        CODIGO_SALIDA += f"{TEMPORAL} = SP + {entorno.tamanio};"
        CODIGO_SALIDA += f"{TEMPORAL2} = Stack[ (int) {TEMPORAL}];"

        retorno = RetornoType()
        retorno.iniciarRetorno(CODIGO_SALIDA,"",TEMPORAL2,funcion.tipo)
        return retorno

    def ejecutar3D(self, entorno):

        resultado = self.obtener3D(entorno)
        return resultado.codigo

    def verificar_funcion_generada(self,entorno,funcion):
        if funcion.ya_se_gero:
            return


        funcion.ya_se_gero = True
        entorno.sustituirFuncion(funcion)

        resultadoFuncion = funcion.ejecutar3D(entorno)
        entorno.generador.agregarFuncion(resultadoFuncion)
