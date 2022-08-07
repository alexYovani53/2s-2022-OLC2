import ply.yacc as yacc

# *************************** SECCION DE ANALIZADOR LEXICO   **************************
from AST.Definicion.Declaracion import Declaracion
from AST.Expresion.Identificador import Identificador
from AST.Expresion.Operacion import Operacion, TIPO_OPERACION
from AST.Expresion.Primitivo import  Primitivo
from AST.Primitivo.Print import Print
from Entorno.RetornoType import TIPO_DATO

reservadas = {
    'int': 'INT',
    'print': 'PRINT',
    'true': 'TRUE',
    'false': 'FALSE',
}

tokens = [
             'DOBLEPT',
             'PTCOMA',
             'PIZQ',
             'PDER',
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
t_PTCOMA = r';'
t_PIZQ = r'\('
t_PDER = r'\)'
t_CORIZQ = r'\{'
t_CORDER = r'\}'

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
    return  t

def t_newLine(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')


t_ignore = " \t\r"


def t_error(t):
    print(f"Se encontro un error lexico {t.value[0]}")
    t.lexer.skip(1)


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
    """init :  instrucciones"""
    t[0] = t[1]


def p_instrucciones(t):
    """instrucciones : instrucciones instruccion"""
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    """ instrucciones : instruccion"""
    t[0] = [t[1]]


def p_instruccion(t):
    """instruccion : print_inst
                   | declaracion """
    t[0] = t[1]

def p_declaracion(t):
    """ declaracion : INT ID  IGUAL expresion  PTCOMA
                    | INT ID PTCOMA """

    t[0] = Declaracion(Identificador(t[2]), t[4] , TIPO_DATO.ENTERO)


def p_print(t):
    """print_inst : PRINT PIZQ expresion PDER PTCOMA"""
    instr = Print(t[3])
    t[0] = instr


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


def p_error(t):
    print("SE ENCONTRO UN ERROR")


# Definicion del parser

parser = yacc.yacc()


def parse(input):
    global lexer
    lexer = lex.lex()
    return parser.parse(input)
