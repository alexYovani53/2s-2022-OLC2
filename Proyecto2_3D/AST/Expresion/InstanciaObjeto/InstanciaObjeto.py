from AST.Abstract.Expression import Expression
from AST.Definicion.Arreglo.CrearArreglo import CrearArreglo
from AST.Definicion.Declaracion import Declaracion
from Entorno.EntornoTabla import EntornoTabla
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolos.Clase import Clase
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Simbolos.Instancia import Instancia


class InstanciaObjeto(Expression):

    def __init__(self, idClase, listaExpresiones):
        self.idClase =idClase
        self.listaExpresiones = listaExpresiones


    def obtener3D(self, entorno):

        if entorno.existeClase(self.idClase) is False: return RetornoType()

        CODIGO_SALIDA = ""
        clasePlantilla : Clase  = entorno.obtenerClase(self.idClase)

        temp1 = entorno.generador.obtenerTemporal()

        CODIGO_SALIDA += f"/*Declaración de instancia de objeto*/\n"
        CODIGO_SALIDA += f"{temp1} = HP; \n"
        CODIGO_SALIDA += f" HP = HP + {self.tamanioDeClase(clasePlantilla)}; \n"


        ENTORNO_INSTANCIA = EntornoTabla(entorno.generador, None)

        index = 0
        for declaracion in clasePlantilla.instrucciones:

            if isinstance(declaracion, Declaracion):

                resultadoExpr = self.listaExpresiones[index].obtener3D(entorno)
                declaracion.declarar_en_instancia = "true"
                declaracion.puntero_entorno_nuevo = temp1
                declaracion.expresionCompilada = resultadoExpr
                CODIGO_SALIDA += declaracion.ejecutar3D(ENTORNO_INSTANCIA)
            elif isinstance(declaracion, CrearArreglo):
                declaracion.declarar_en_instancia = "true"
                pass

            index += 1

        instanciaNueva = Instancia(self.idClase,"",ENTORNO_INSTANCIA)

        retorno = RetornoType()
        retorno.iniciarRetornoInstancia(CODIGO_SALIDA, temp1, TIPO_DATO.OBJETO, instanciaNueva)
        return retorno

    def tamanioDeClase(self, clasePlantilla: Clase):

        contador = 0
        for instruccion in clasePlantilla.instrucciones:
            if isinstance(instruccion, Declaracion):
                contador += 1
        return contador