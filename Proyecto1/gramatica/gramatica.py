import ply.yacc as yacc

# *************************** SECCION DE ANALIZADOR LEXICO   **************************
from AST.Ast import Ast
from AST.Control.Return_Instr import Return_Instr
from AST.Definicion.Arreglo.CrearArreglo import CrearArreglo
from AST.Definicion.Declaracion import Declaracion
from AST.Definicion.Objetos.CrearInstanciaObjeto import CrearInstanciaObjeto
from AST.Definicion.Objetos.GuardarClase import GuardarClase
from AST.Error.CustomError import CustomError
from AST.Expresion.Acceso.AccesObjeto import AccesoObjeto
from AST.Expresion.Acceso.AccesoArreglo import AccesoArreglo
from AST.Expresion.Arreglo.ArrayData import ArrayData
from AST.Expresion.Arreglo.ArrayInstancia import ArrayInstancia
from AST.Expresion.Identificador import Identificador
from AST.Expresion.InstanciaObjeto.InstanciaObjeto import InstanciaObjeto
from AST.Expresion.Llamada import Llamada
from AST.Expresion.Operacion import Operacion, TIPO_OPERACION
from AST.Expresion.Primitivo import Primitivo
from AST.Primitivo.Print import Print
from AST.flujo.If_Inst import IfInst
from Entorno.RetornoType import TIPO_DATO
from Entorno.Simbolos.Funcion import Funcion


errores = []

reservadas = {
    'int': 'INT',
    'string': 'STRING_TYPE',
    'float': 'FLOAT',
    'boolean': 'BOOLEAN',
    'print': 'PRINT',
    'true': 'TRUE',
    'false': 'FALSE',

    'void': 'VOID',
    'return': 'RETURN_W',
    'if': 'IF_W',
    'else': 'ELSE_W',

    'class': 'CLASS',
    'new': 'NEW'
}

tokens = [
             'DOBLEPT',
             'PUNTO',
             'PTCOMA',
             'COMA',
             'PIZQ',
             'PDER',
             'LLAVEIZQ',
             'LLAVEDER',
             'CORIZQ',
             'CORDER',

             'AND',
             'OR',
             'NOT',

             'MAYORIGUAL',
             'MENOR',
             'MENORIGUAL',
             'MAYOR',
             'IGUALIGUAL',
             'DIFERENTE',
             'IGUAL',

             'MAS',
             'MENOS',
             'DIVISION',
             'MULTIPLICACION',
             'DECIMAL',
             'ENTERO',
             'ID',
             'CADENA'
         ] + list(reservadas.values())

# definir tokens
t_DOBLEPT = r'\:'
t_PUNTO = r'\.'
t_PTCOMA = r';'
t_COMA = r','
t_PIZQ = r'\('
t_PDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_CORIZQ = r'\['
t_CORDER = r'\]'

t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'

t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_IGUALIGUAL = r'\=\='
t_DIFERENTE = r'\!\='
t_IGUAL = r'\='

t_MAS = r'\+'
t_MENOS = r'-'
t_DIVISION = r'/'
t_MULTIPLICACION = r'\*'


def t_DECIMAL(t):
    r"""\d+\.\d+"""
    try:
        t.value = float(t.value)
    except ValueError:
        t.value = 0.0
    return t


def t_ENTERO(t):
    r"""\d+"""
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = 0
    return t


def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z0-9_]*"""
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


def t_CADENA(t):
    """\".*?\""""
    t.value = t.value[1:-1]  # Eliminar las comillas dobles
    return t


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1


t_ignore = " \t\r"


def t_newLine(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    errores.append(CustomError("Lexico", "Error léxico: " + t.value[0], t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)


textoEntrada = ""


def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# creando el lexer
import ply.lex as lex

lexer = lex.lex()

# *************************** SECCION DE ANALIZADOR SINTACTICO  (parser) ************************** 
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'MAYOR', 'MENORIGUAL', 'MENOR', 'MAYORIGUAL', 'IGUALIGUAL', 'DIFERENTE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('right', 'NOT', 'UMENOS')
)


def p_init(t):
    """init : clases_funciones """

    t[0] = Ast(t[1])


def p_clases_funciones(t):
    """ clases_funciones : clases_funciones clase_funcion """
    t[1].append(t[2])
    t[0] = t[1]


def p_clases_funciones_corte(t):
    """ clases_funciones : clase_funcion """
    t[0] = [t[1]]


def p_clase_funcion(t):
    """ clase_funcion : clase
                      | funcion"""
    t[0] = t[1]

def p_clase_funcion_error(t):
    """ clase_funcion : error LLAVEDER """
    errores.append(CustomError("Sintáctico", "Error Sintáctico: " + str(t[1].value), t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""


def p_clase(t):
    """  clase : CLASS ID bloqueClase"""
    t[0] = GuardarClase(idClase=t[2], listaInstrucciones=t[3])


def p_bloque_clase(t):
    """ bloqueClase : LLAVEIZQ instrs_clase LLAVEDER
                    | LLAVEIZQ  LLAVEDER"""
    if len(t) == 4:
        t[0] = t[2]
    else:
        t[0] = []


def p_funcion(t):
    """funcion : tipo_funcion ID PIZQ  PDER bloque
               | tipo_funcion ID PIZQ lista_parametros PDER bloque"""

    if len(t) == 6:
        t[0] = Funcion(t[2], [], t[5], t[1])
    else:
        t[0] = Funcion(t[2], t[4], t[6], t[1])


# ------------------------------------------ PARAMETROS FUCION

def p_lista_parametros(t):
    """ lista_parametros : lista_parametros COMA parametro"""
    t[1].append(t[3])
    t[0] = t[1]


def p_lista_parametros_corte(t):
    """ lista_parametros : parametro"""
    t[0] = [t[1]]


def p_parametro(t):
    """ parametro : tipo_dato ID
                  | MULTIPLICACION tipo_dato ID"""


    if len(t) == 3:
        id = Identificador(t[2])
        t[0] = Declaracion(id, None, t[1])
    else:
        id = Identificador(t[3])
        t[0] = Declaracion(id, None, t[2],True  )

# ------------------------------------------ BLOQUE

def p_bloque(t):
    """bloque  : LLAVEIZQ  LLAVEDER
                | LLAVEIZQ  instrucciones LLAVEDER """

    if len(t) == 3:
        t[0] = []
    else:
        t[0] = t[2]


# ------------------------------------------ INSTRUCCIONES CLASE
def p_instrs_clase(t):
    """ instrs_clase : instrs_clase instr """
    t[1].append(t[2])
    t[0] = t[1]


def p_instrs_clase_corte(t):
    """ instrs_clase :  instr """
    t[0] = [t[1]]


def p_instr(t):
    """ instr : declaracion PTCOMA"""
    t[0] = t[1]


# ------------------------------------------- INSTRUCCIONES

def p_instrucciones(t):
    """instrucciones : instrucciones instruccion"""
    if t[2] != -1:
        t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    """ instrucciones : instruccion """
    t[0] = [t[1]]


def p_instruccion(t):
    """instruccion : print_inst PTCOMA
                   | declaracion PTCOMA
                   | declaracion_objeto PTCOMA
                   | declaracion_arreglo PTCOMA
                   | llamada PTCOMA
                   | return_inst PTCOMA
                   | if_instr"""
    t[0] = t[1]


def p_error_sintaxis(t):
    """ instruccion : error PTCOMA """
    t[0] = -1
    errores.append(CustomError("Sintáctico", "Error Sintáctico: " + str(t[1].value), t.lineno(1), find_column(input, t.slice[1])))



# DECLARACION ------------------------
def p_declaracion(t):
    """ declaracion : tipo_dato ID IGUAL expresion
                    | tipo_dato ID """

    if len(t) == 3:
        t[0] = Declaracion(Identificador(t[2]), None, t[1])
    else:
        t[0] = Declaracion(Identificador(t[2]), t[4], t[1])


# DECLARACION ARREGLO ----------------

def p_declaracion_arreglo(t):
    """ declaracion_arreglo : tipo_dato niveles ID IGUAL expresion """
    t[0] = CrearArreglo(idInstancia=t[3], dimensiones=t[2], tipo=t[1], expresion=t[5])


def p_niveles(t):
    """niveles : niveles nivel """
    t[1] += 1
    t[0] = t[1]

def p_niveles_corte(t):
    """ niveles : nivel """
    t[0] = 1

def p_nivel(t):
    """ nivel : CORIZQ CORDER """


# DECLARACION OBJETO ----------------
def p_declaracion_objeto(t):
    """ declaracion_objeto : ID ID IGUAL expresion """

    t[0] = CrearInstanciaObjeto(idClase=t[1], idInstancia=t[2], expresion=t[4])


# PRINT ------------------------------
def p_print(t):
    """print_inst : PRINT PIZQ expresion PDER"""
    instr = Print(t[3])
    t[0] = instr


# LLAMADA -----------------------------
def p_llamada(t):
    """ llamada : ID PIZQ PDER
                | ID PIZQ lista_expresiones PDER"""

    if len(t) == 4:
        t[0] = Llamada(t[1], [])
    else:
        t[0] = Llamada(t[1], t[3])


# RETURNS -----------------------------
def p_return_instr(t):
    """ return_inst : RETURN_W
                    | RETURN_W expresion"""

    if len(t) == 2:
        t[0] = Return_Instr(TIPO_DATO.VOID, None)
    else:
        t[0] = Return_Instr(TIPO_DATO.NULL, t[2])


# if , if - else , if-elseif-else, if - elseif- elseif
def p_if_instr(t):
    """ if_instr :  IF_W PIZQ expresion PDER bloque
                 |  IF_W PIZQ expresion PDER bloque ELSE_W bloque
                 |  IF_W PIZQ expresion PDER bloque  listaelseif
                 |  IF_W PIZQ expresion PDER bloque  listaelseif ELSE_W bloque"""

    if len(t) == 6:
        t[0] = IfInst(t[3], t[5], [], [])
    elif len(t) == 7:
        t[0] = IfInst(t[3], t[5], t[6], [])
    elif len(t) == 8:
        t[0] = IfInst(t[3], t[5], [], t[7])
    else:
        t[0] = IfInst(t[3], t[5], t[6], t[8])


def p_lista_else_if(t):
    """ listaelseif : listaelseif else_if  """
    t[1].append(t[2])
    t[0] = t[1]


def p_lista_else_if_corte(t):
    """ listaelseif : else_if"""
    t[0] = [t[1]]


def p_else_if(t):
    """ else_if : ELSE_W IF_W PIZQ expresion PDER bloque"""
    t[0] = IfInst(t[4], t[6], [], [])


# ________________________________________ LISTA EXPRESIONES
def p_lista_expresiones(t):
    """ lista_expresiones : lista_expresiones COMA  expresion"""
    t[1].append(t[3])
    t[0] = t[1]


def p_lista_expresiones_corte(t):
    """ lista_expresiones : expresion"""
    t[0] = [t[1]]


# ---------------------------------------- EXPRESIONES

def p_expresion_logica(t):
    """expresion : expresion OR expresion
                 | expresion AND expresion
                 | NOT expresion %prec NOT"""

    if t[2] == '&&':
        t[0] = Operacion(t[1], TIPO_OPERACION.AND, t[3])
    if t[2] == '||':
        t[0] = Operacion(t[1], TIPO_OPERACION.OR, t[3])


def p_expresion_relacional(t):
    """expresion : expresion MENOR expresion
                 | expresion MAYOR expresion
                 | expresion MAYORIGUAL expresion
                 | expresion MENORIGUAL expresion
                 | expresion DIFERENTE expresion
                 | expresion IGUALIGUAL expresion"""

    if t[2] == '<':
        t[0] = Operacion(t[1], TIPO_OPERACION.MENOR, t[3])
    if t[2] == '>':
        t[0] = Operacion(t[1], TIPO_OPERACION.MAYOR, t[3])
    if t[2] == '<=':
        t[0] = Operacion(t[1], TIPO_OPERACION.MENORIGUAL, t[3])
    if t[2] == '>=':
        t[0] = Operacion(t[1], TIPO_OPERACION.MAYORIGUAL, t[3])
    if t[2] == '==':
        t[0] = Operacion(t[1], TIPO_OPERACION.IGUALIGUAL, t[3])
    if t[2] == '!=':
        t[0] = Operacion(t[1], TIPO_OPERACION.DIFERENTE, t[3])


def p_expresion_aritmetica(t):
    """expresion : MENOS expresion %prec UMENOS
                 | expresion MAS expresion
                 | expresion MENOS expresion
                 | expresion MULTIPLICACION expresion
                 | expresion DIVISION expresion
                 | PIZQ expresion PDER"""

    if len(t) == 3:
        t[0] = Operacion(t[2], TIPO_OPERACION.RESTA, None, True)
    elif t[1] == '(':
        t[0] = t[2]
    else:
        if t[2] == '+':
            t[0] = Operacion(t[1], TIPO_OPERACION.SUMA, t[3])
        elif t[2] == '-':
            t[0] = Operacion(t[1], TIPO_OPERACION.RESTA, t[3])


def p_expresion_primitiva(t):
    """expresion : ENTERO
                    | DECIMAL
                    | ID
                    | CADENA
                    | TRUE
                    | FALSE"""

    if t.slice[1].type == 'ENTERO':
        t[0] = Primitivo(t[1], TIPO_DATO.ENTERO)
    elif t.slice[1].type == 'DECIMAL':
        t[0] = Primitivo(t[1], TIPO_DATO.DECIMAL)
    elif t.slice[1].type == 'ID':
        t[0] = Identificador(t[1])
    elif t.slice[1].type == 'CADENA':
        t[0] = Primitivo(t[1], TIPO_DATO.CADENA)
    elif t.slice[1].type == 'TRUE':
        t[0] = Primitivo(True, TIPO_DATO.BOOLEAN)
    elif t.slice[1].type == 'FALSE':
        t[0] = Primitivo(False, TIPO_DATO.BOOLEAN)


def p_otras_expresiones(t):
    """ expresion : llamada
                  | acceso_objeto_expresion
                  | acceso_array_expresion
                  | instancia_objeto
                  | array_data
                  | array_instancia
                  | if_instr"""
    t[0] = t[1]


# ARRAY DATA --------------------------
def p_array_data(t):
    """ array_data : CORIZQ lista_expresiones CORDER"""
    t[0] = ArrayData(listaExpresiones = t[2])

# ARRAY INSTANCIA ---------------------
def p_array_instancia(t):
    """ array_instancia : NEW tipo_dato dimensiones"""
    t[0] = ArrayInstancia(tipo = t[2], dimensiones = t[3])

def p_dimensiones(t):
    """ dimensiones : dimensiones dimension"""
    t[1].append(t[2])
    t[0] = t[1]


def p_dimensiones_corte(t):
    """ dimensiones : dimension"""
    t[0] = [t[1]]

def p_dimension(t):
    """ dimension : CORIZQ expresion CORDER"""
    t[0] = t[2]

# INSTANCIA OBJETO -------------------------
def p_instancia_objeto(t):
    """ instancia_objeto : NEW ID PIZQ PDER
                         | NEW ID PIZQ lista_expresiones PDER"""
    if len(t) == 5:
        t[0] = InstanciaObjeto(idClase=t[2], listaExpresiones=[])
    else:
        t[0] = InstanciaObjeto(idClase=t[2], listaExpresiones=t[4])



# ACCESO A OBJETO  ----------------------
def p_acceso_objeto_expresion(t):
    """ acceso_objeto_expresion : acceso_objeto"""
    t[0] = AccesoObjeto(listaExpresiones=t[1])


def p_acceso_objeto(t):
    """ acceso_objeto : acceso_objeto  PUNTO expresion"""
    t[1].append(t[3])
    t[0] = t[1]


def p_acceso_objeto_cort(t):
    """ acceso_objeto : expresion"""
    t[0] = [t[1]]

# ACCESO ARRAY ----------------------------
def p_acceso_array(t):
    """acceso_array_expresion : ID dimensiones"""
    t[0] = AccesoArreglo( idArreglo = t[1] ,listaExpresiones = t[2])






# ------------------------------------------ TIPOS DE RETORNO

def p_tipo_retorno_funcion(t):
    """ tipo_funcion : INT
                     | STRING_TYPE
                     | BOOLEAN
                     | VOID
                     | FLOAT"""

    if t[1] == 'int':
        t[0] = TIPO_DATO.ENTERO
    if t[1] == 'string':
        t[0] = TIPO_DATO.CADENA
    if t[1] == 'boolean':
        t[0] = TIPO_DATO.BOOLEAN
    if t[1] == 'float':
        t[0] = TIPO_DATO.DECIMAL
    if t[1] == 'void':
        t[0] = TIPO_DATO.VOID


def p_tipo_dato(t):
    """ tipo_dato : INT
                     | STRING_TYPE
                     | BOOLEAN
                     | FLOAT"""

    if t[1] == 'int':
        t[0] = TIPO_DATO.ENTERO
    if t[1] == 'string':
        t[0] = TIPO_DATO.CADENA
    if t[1] == 'boolean':
        t[0] = TIPO_DATO.BOOLEAN
    if t[1] == 'float':
        t[0] = TIPO_DATO.DECIMAL


def p_error(t):
    print(f"SE ENCONTRO UN ERROR {t.value}")



# Definicion del parser

parser = yacc.yacc()




def getErrores():
    return errores

input = ''
def parse(inp):
    global lexer
    global input
    global errores


    errores = []
    input = inp
    lexer = lex.lex()
    return parser.parse(inp)
