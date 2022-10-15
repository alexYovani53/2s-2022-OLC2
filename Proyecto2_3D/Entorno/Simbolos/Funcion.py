from AST.Abstract.Instruccion import Instruccion
from AST.Definicion.Declaracion import Declaracion
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolo import Simbolo


class Funcion(Simbolo, Instruccion):


    comparacionTipo = [
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.DECIMAL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL,TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL,TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.BOOLEAN, TIPO_DATO.NULL,TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.VOID,TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.VOID,TIPO_DATO.NULL],
    ]

    def __init__(self, identificador, listaParametros, listaInstrucciones, tipo):
        super().__init__()
        super().iniciarSimboloFuncion(identificador,listaParametros,listaInstrucciones,tipo)
        self.ya_se_gero = False
        self.entornoFuncion = None

    def ejecutarParametros(self, entornoFuncion, expresiones: [], entornoQueLlamo, puntero_entorno_nuevo) -> str:

        if len(self.parametros) != len(expresiones):
            return ""

        CODIGO_SALIDA = ""
        for i in range(len(expresiones)):
            declaracion_tomada = self.parametros[i]
            expresion_tomada = expresiones[i]

            if isinstance(declaracion_tomada, Declaracion):
                declaracion_tomada.expresionCompilada = expresion_tomada.obtener3D(entornoQueLlamo)
                declaracion_tomada.puntero_entorno_nuevo = puntero_entorno_nuevo
                declaracion_tomada.ejecuta_en_funcion = True

                CODIGO_SALIDA += declaracion_tomada.ejecutar3D(entornoFuncion)

        return CODIGO_SALIDA


    # PARA MANEJAR LOS RETORNO ---------------------
    # DEVEMOS SUSTITUIR UNA PALABRA CLAVE QUE SE GENERA DENTRO DE LA INSTRUCCIÓN --->> RETURN <<---
    # ESTA PALABRA CLAVE SE CAMBIARÁ POR EL NOMBRE DE UNA ETIQUETA
    def ejecutar3D(self, entorno):

        CODIGO_SALIDA = ""
        ETIQUETA_RETURN = entorno.generador.obtenerEtiqueta()

        CODIGO_SALIDA += f"void {self.identificador}() {{ \n"

        for instruccion in self.instrucciones:
            CODIGO_SALIDA += instruccion.ejecutar3D(entorno)

        CODIGO_SALIDA = CODIGO_SALIDA.replace("SECCION_N_RETORNO", ETIQUETA_RETURN)

        CODIGO_SALIDA += f"{ETIQUETA_RETURN}: \n"
        CODIGO_SALIDA += f"return; \n"
        CODIGO_SALIDA += f"}}\n"
        return CODIGO_SALIDA

    def __str__(self):
        return f"Funcion {self.identificador}"