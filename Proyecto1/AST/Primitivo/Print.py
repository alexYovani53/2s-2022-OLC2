from AST.Abstract.Instruccion import Instruccion


class Print(Instruccion):

    def __init__(self, expression):
        self.expression = expression

    def ejecutarInstr(self, entorno):

        valor = self.expression.obtenerValor(None)
        print(f"{valor}")