from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import TIPO_DATO, RetornoType


class IfInst(Instruccion):

    def __init__(self, condicion, listaInstrucionPrincipal, listaelseif, bloqueInstElse):
        self.condicion = condicion
        self.listaInstrucionPrincipal = listaInstrucionPrincipal
        self.listaelseif = listaelseif
        self.bloqueInstElse = bloqueInstElse

    def ejecutar3D(self, entorno):

        CODIGO_SALIDA = ""

        # if ( a  > a && b = 0 || x == 10)

        ETIQUETA_SALIDA = entorno.generador.obtenerEtiqueta()

        self.condicion.etiquetaVerdadera = entorno.generador.obtenerEtiqueta()
        self.condicion.etiquetaFalsa  = entorno.generador.obtenerEtiqueta()

        expresionCondicion = self.condicion.obtener3D(entorno)
        

        CODIGO_SALIDA += "/* INSTRUCCION IF*/\n"
        CODIGO_SALIDA += expresionCondicion.codigo
        CODIGO_SALIDA += f'{expresionCondicion.etiquetaV}: \n'
        CODIGO_SALIDA += self.generarC3DInstrucciones(entorno,self.listaInstrucionPrincipal)
        CODIGO_SALIDA += f' goto {ETIQUETA_SALIDA};\n'
        CODIGO_SALIDA += f'{expresionCondicion.etiquetaF}:\n'

        if len(self.listaelseif) > 0:

            for intrsElseIf in self.listaelseif:
                intrsElseIf.etiquetaVerdadera = entorno.generador.obtenerEtiqueta()
                intrsElseIf.etiquetaFalsa = entorno.generador.obtenerEtiqueta()

                expresionSubCondion = intrsElseIf.obtener3D(entorno)


        # bool a =    10 > 20;


                CODIGO_SALIDA += "\n\n"
                CODIGO_SALIDA += expresionSubCondion.codigo
                CODIGO_SALIDA += f'{expresionSubCondion.etiquetaV}: \n'
                CODIGO_SALIDA += self.generarC3DInstrucciones(entorno, intrsElseIf.listaInstrucionPrincipal)
                CODIGO_SALIDA += f'goto {ETIQUETA_SALIDA};\n'
                CODIGO_SALIDA += f'{expresionCondicion.etiquetaF}:\n'

        if len(self.bloqueInstElse) > 0:
            CODIGO_SALIDA += self.generarC3DInstrucciones(entorno, self.bloqueInstElse)

        CODIGO_SALIDA+= f'{ETIQUETA_SALIDA}: \n'
        return CODIGO_SALIDA



    def generarC3DInstrucciones(self,entorno,lista):

        CODIGO_SALIDA = ""
        for intrs in lista :
            CODIGO_SALIDA += intrs.ejecutar3D(entorno)

        return CODIGO_SALIDA