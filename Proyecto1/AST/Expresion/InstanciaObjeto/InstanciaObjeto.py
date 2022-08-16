from AST.Abstract.Expression import Expression
from Entorno.RetornoType import RetornoType


class InstanciaObjeto(Expression):

    def __int__(self, identificador, listaExpresiones):
        self.identificador =identificador
        self.listaExpresiones = listaExpresiones

    def obtenerValor(self, entorno) -> RetornoType:

        # 1. VALIDAR QUE EXISTA LA CLASE EN EL ENTORNO
        # 2. RECUPERAR EL SIMBOLO O CLASE
        # 3. CREAR UN NUEVO ENTORNO, SIN NINGUN PADRE
        # 4. VALIDAR Y EJECUTAR LAS DECLARACIONES
        # 5. RETORNAR UN RETORNO TYPE ( VALOR = INSTANCIA, TIPO = TIPO_DATO.OBJETO)

        pass
