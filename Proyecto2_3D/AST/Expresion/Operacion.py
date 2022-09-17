from enum import Enum

from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType, TIPO_DATO


class TIPO_OPERACION(Enum):
    SUMA = 1,
    RESTA = 2,
    MULTIPLICACION = 3,
    DIVISION = 4,
    MENOR = 5,
    MAYOR = 6,
    MENORIGUAL = 7,
    MAYORIGUAL = 8,
    DIFERENTE = 9,
    IGUALIGUAL = 10,
    AND = 11,
    OR = 12,
    NOT = 13,


class Operacion(Expression):
    sumaDominante = [
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.DECIMAL, TIPO_DATO.DECIMAL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.CADENA, TIPO_DATO.CADENA, TIPO_DATO.CADENA, TIPO_DATO.CADENA, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.CADENA, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
    ]

    restaMultiplicacionDivison = [
        [TIPO_DATO.ENTERO, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.DECIMAL, TIPO_DATO.DECIMAL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
        [TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL, TIPO_DATO.NULL],
    ]

    def __init__(self, exprIzq, tipo_operacion, exprDer, unario=False):
        self.exprIzq = exprIzq
        self.tipo_operacion = tipo_operacion
        self.exprDer = exprDer
        self.unario = unario
        self.etiquetaVerdadera = ""
        self.etiquetaFalsa = ""

    def obtener3D(self, entorno) -> RetornoType:

        match (self.tipo_operacion):
            case  TIPO_OPERACION.SUMA:
                return self.operacionSuma(entorno)

            case TIPO_OPERACION.MAYOR:
                return self.operacionRelacional(entorno)
            case TIPO_OPERACION.MENOR:
                return self.operacionRelacional(entorno)
            case TIPO_OPERACION.MAYORIGUAL:
                return self.operacionRelacional(entorno)
            case TIPO_OPERACION.MENORIGUAL:
                return self.operacionRelacional(entorno)
            case TIPO_OPERACION.DIFERENTE:
                return self.operacionRelacional(entorno)
            case TIPO_OPERACION.IGUALIGUAL:
                return self.operacionRelacional(entorno)



    def operacionSuma(self,entorno):

        CODIGO_SALIDA = ""
        RETORNO = RetornoType()

        TEMP1 = entorno.generador.obtenerTemporal()

        izq3D = self.exprIzq.obtener3D(entorno)
        der3D = self.exprDer.obtener3D(entorno)

        tipoDominante = Operacion.sumaDominante[izq3D.tipo][der3D.tipo]

        if tipoDominante == TIPO_DATO.ENTERO:

            CODIGO_SALIDA += izq3D.codigo +"\n"
            CODIGO_SALIDA += der3D.codigo +"\n"
            CODIGO_SALIDA += f'{TEMP1} = {izq3D.temporal} + {der3D.temporal};\n'

            RETORNO.iniciarRetorno(CODIGO_SALIDA,"",TEMP1,tipoDominante)

        elif tipoDominante == TIPO_DATO.DECIMAL:

            CODIGO_SALIDA += izq3D.codigo +"\n"
            CODIGO_SALIDA += der3D.codigo +"\n"
            CODIGO_SALIDA += f'{TEMP1} = {izq3D.temporal} + {der3D.temporal};\n'

            RETORNO.iniciarRetorno(CODIGO_SALIDA,"",TEMP1,tipoDominante)

        elif tipoDominante == TIPO_DATO.CADENA:
            TEMP2 = entorno.generador.obtenerTemporal()

            CODIGO_SALIDA += izq3D.codigo
            CODIGO_SALIDA += der3D.codigo
            CODIGO_SALIDA += f'{TEMP2} = HP;\n'
            CODIGO_SALIDA += self.operacionConcatenar(entorno,izq3D)
            CODIGO_SALIDA += self.operacionConcatenar(entorno,der3D)
            CODIGO_SALIDA += f'Heap[HP] = 0;\n'
            CODIGO_SALIDA += f'HP = HP + 1;\n'

            RETORNO.iniciarRetorno(CODIGO_SALIDA,"",TEMP2,TIPO_DATO.CADENA)

        return  RETORNO

    def operacionRelacional(self,entorno):
        # if a< b goto B.true
        # goto B.false

        CODIGO_SALIDA = ""

        izq3D = self.exprIzq.obtener3D(entorno)
        der3D = self.exprDer.obtener3D(entorno)

        CODIGO_SALIDA += izq3D.codigo
        CODIGO_SALIDA += der3D.codigo

        tipoDominante = Operacion.restaMultiplicacionDivison[izq3D.tipo][der3D.tipo]

        if tipoDominante == TIPO_DATO.ENTERO or tipoDominante == TIPO_DATO.DECIMAL:
            CODIGO_SALIDA += f'if ({izq3D.temporal} {self.obtenerSimbolo()} {der3D.temporal}) goto {self.etiquetaVerdadera};\n'
            CODIGO_SALIDA += f'goto {self.etiquetaFalsa}; \n'

            RETORNO = RetornoType()
            RETORNO.iniciarRetorno(CODIGO_SALIDA,"","", TIPO_DATO.BOOLEAN)
            RETORNO.etiquetaV = self.etiquetaVerdadera
            RETORNO.etiquetaF = self.etiquetaFalsa
            return RETORNO

        else:
            return RetornoType()


    def obtenerSimbolo(self):
        match(self.tipo_operacion):
            case TIPO_OPERACION.MAYOR:
                return '>'
            case TIPO_OPERACION.MENOR:
                return '<'
            case TIPO_OPERACION.MAYORIGUAL:
                return '>='
            case TIPO_OPERACION.MENORIGUAL:
                return '<='

    def operacionConcatenar(self,entorno,expresionRetorno):
        CODIGO_SALIDA = ""

        etiquetaCiclo = entorno.generador.obtenerEtiqueta()
        etiquetaSalida = entorno.generador.obtenerEtiqueta()
        CARACTER = entorno.generador.obtenerTemporal()

        CODIGO_SALIDA += f'{etiquetaCiclo}: \n'
        CODIGO_SALIDA += f'{CARACTER} = Heap[(int){expresionRetorno.temporal}];\n'
        CODIGO_SALIDA += f'if ( {CARACTER} == 0) goto {etiquetaSalida};\n'
        CODIGO_SALIDA += f'     Heap[HP] = {CARACTER};\n'
        CODIGO_SALIDA += f'     HP = HP + 1;\n'
        CODIGO_SALIDA += f'     {expresionRetorno.temporal} = {expresionRetorno.temporal} + 1;\n'
        CODIGO_SALIDA += f'     goto {etiquetaCiclo};\n'
        CODIGO_SALIDA += f'{etiquetaSalida}:\n'
        return CODIGO_SALIDA