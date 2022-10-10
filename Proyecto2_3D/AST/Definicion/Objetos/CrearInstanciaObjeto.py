from AST.Abstract.Instruccion import Instruccion
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolos.Instancia import Instancia


class CrearInstanciaObjeto(Instruccion):

    def __init__(self,idClase, idInstancia, expresion):
        self.idClase = idClase
        self.idInstancia = idInstancia
        self.expresion = expresion
        self.valorCompilador = None

    def ejecutar3D(self, entorno):
        if(entorno.existeClase(self.idClase) == False): return ""
        if(entorno.existeSimbolo(self.idInstancia)): return ""

        resultadoExpresion = self.expresion.obtener3D(entorno)

        if resultadoExpresion.tipo is not TIPO_DATO.OBJETO: return ""

        instancia: Instancia = resultadoExpresion.valor
        if instancia.idClase != self.idClase: return  ""
        instancia.identificador = self.idInstancia

        temp1 = entorno.generador.obtenerTemporal()
        CODIGO_SALIDA = resultadoExpresion.codigo
        CODIGO_SALIDA += f"{temp1} = SP + {entorno.tamanio};\n"
        entorno.tamanio += 1
        CODIGO_SALIDA += f"Stack [ (int) {temp1} ] = {resultadoExpresion.temporal}; \n"
        CODIGO_SALIDA += "/* FINALIZANDO DECLARACIÓN DE OBJETO */\n"

        entorno.agregarSimbolo(instancia)

        return CODIGO_SALIDA