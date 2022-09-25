from AST.Abstract.Instruccion import Instruccion


class For(Instruccion):

    def __init__(self):
        pass

    def ejecutar3D(self, entorno):

        ETIQUETA_SALIDA = entorno.generador.obtenerEtiqueta()
        ETIQUETA_INICO = entorno.generador.obtenerEtiqueta()


        #  ETIQUETA INICIO

        CODIGO_SALIDA = ""

        # GENERAR CODIGO DE INSTRUCCIONES

        CODIGO_SALIDA.replace("ETIQUETA_BREAK", ETIQUETA_SALIDA)
        CODIGO_SALIDA = f"{ ETIQUETA_SALIDA}: \n"

        pass
