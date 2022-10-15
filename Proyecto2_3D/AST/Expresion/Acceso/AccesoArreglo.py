from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo


class AccesoArreglo(Expression):

    def __init__(self, idArreglo, listaExpresiones):
        self.idArreglo = idArreglo
        self.listaExpresiones = listaExpresiones


    def obtener3D(self, entorno):

        if(entorno.existeSimbolo(self.idArreglo) is False):
            return RetornoType()

        instanciaArreglo = entorno.obtenerSimbolo(self.idArreglo)
        if isinstance(instanciaArreglo, InstanciaArreglo) is False:
            return RetornoType()

        temp1 = entorno.generador.obtenerTemporal()
        temp2 = entorno.generador.obtenerTemporal()
        etiqueta = entorno.generador.obtenerEtiqueta()

        CODIGO_SALIDA = "/* ACCESO A UN ARREGLO*/\n"
        CODIGO_SALIDA += f"{temp1} = SP + {instanciaArreglo.direccionRelativa};\n"
        CODIGO_SALIDA += f"{temp2} = Stack[(int) {temp1}]; \n"

        if len(self.listaExpresiones) != len(instanciaArreglo.dimensiones):
            return  RetornoType()

        listaExpresionesCompiladas = self.compilarDimensiones(entorno)
        for expr in listaExpresionesCompiladas:
            CODIGO_SALIDA += expr.codigo

        resultado = self.accederAPosicion(listaExpresionesCompiladas, temp2,entorno)

        CODIGO_SALIDA += resultado.codigo
        CODIGO_SALIDA = CODIGO_SALIDA.replace("salida_arreglo_x",etiqueta)
        CODIGO_SALIDA += f"{etiqueta}:\n"

        retorno = RetornoType()
        retorno.iniciarRetorno(CODIGO_SALIDA,None,resultado.temporal,instanciaArreglo.tipo)
        return retorno

    def compilarDimensiones(self, entorno ):
        dimensiones = []
        for expresion in self.listaExpresiones:
            retornoExpr = expresion.obtener3D(entorno)
            dimensiones.append(retornoExpr)
            if retornoExpr.tipo != TIPO_DATO.ENTERO:
                return []

        return  dimensiones

    def accederAPosicion(self,listaExpresiones, temporal, entorno):
        CODIGO_SALIDA = "/*ACCEDIENDO A X POSICION*/\n"

        expresionX: RetornoType = listaExpresiones.pop(0)

        temp1 = entorno.generador.obtenerTemporal()
        temp2 = entorno.generador.obtenerTemporal()
        temp3 = entorno.generador.obtenerTemporal()
        temp4 = entorno.generador.obtenerTemporal()


        CODIGO_SALIDA += f"{temp1} = Heap[(int) {temporal}]; /*OBTENIENDO TAMAÑO DE ARREGLO*/\n "
        CODIGO_SALIDA += f" if ({expresionX.temporal} > {temp1}) goto salida_arreglo_x;\n"
        CODIGO_SALIDA += f"{temp2} = {temporal} + 1;\n"
        CODIGO_SALIDA += f"{temp3} = {temp2} + {expresionX.temporal};\n"
        CODIGO_SALIDA += f"{temp4} = Heap[(int) {temp3}];\n"

        retorno = RetornoType()
        if(len(listaExpresiones)> 0):
            resultado =  self.accederAPosicion(listaExpresiones,temp4,entorno)
            CODIGO_SALIDA += resultado.codigo
            retorno.iniciarRetorno(CODIGO_SALIDA,None,resultado.temporal,None)
        else:
            retorno.iniciarRetorno(CODIGO_SALIDA,None,temp4,None)

        return retorno