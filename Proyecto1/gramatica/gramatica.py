import ply.yacc as yacc

# *************************** SECCION DE ANALIZADOR LEXICO   **************************
from AST.Expresion.Operacion import Operacion, TIPO_OPERACION
from AST.Expresion.Primitivo import TIPO_DATO, Primitivo
from AST.Primitivo.Print import Print

reservadas = {
    'int': 'INT',
    'print': 'PRINT'
}

tokens = [
             'PTCOMA',
             'PIZQ',
             'PDER',
             'CORIZQ',
             'CORDER',
             'MAS',
             'MENOS',
             'DIVISION',
             'MULTIPLICACION',
             'DECIMAL',
             'ENTERO',
             'ID'
         ] + list(reservadas.values())

# definir tokens

t_PTCOMA = r';'
t_PIZQ = r'\('
t_PDER = r'\)'
t_CORIZQ = r'\{'
t_CORDER = r'\}'
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

def t_newLine(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')


t_ignore = " \t\r"


def t_error(t):
    print(f"Se encontro un error lexico {t.value[0]}" )
    t.lexer.skip(1)


# creando el lexer
import ply.lex as lex

lexer = lex.lex()

# *************************** SECCION DE ANALIZADOR SINTACTICO  (parser) **************************
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION')
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
    """instruccion : print_inst"""
    t[0] = t[1]


def p_print(t):
    """print_inst : PRINT PIZQ expression PDER"""
    instr = Print(t[3])
    t[0] = instr


def p_expression_aritmetica(t):
    """expression : expression MAS expression
                 | expression MENOS expression"""

    if t[2] == '+':
        t[0] = Operacion(t[1], TIPO_OPERACION.SUMA, t[3])
    elif t[2] == '-':
        t[0] = Operacion(t[1], TIPO_OPERACION.RESTA, t[3])


def p_expression_primitiva(t):
    """expression : ENTERO
                    | DECIMAL"""

    if t.slice[1].type == 'ENTERO':
        t[0] = Primitivo(t[1], TIPO_DATO.ENTERO)
    elif t.slice[1].type == 'DECIMAL':
        t[0] = Primitivo(t[1], TIPO_DATO.DECIMAL)


def p_error(t):
    print("SE ENCONTRO UN ERROR")


# Definicion del parser

parser = yacc.yacc()


def parse(input):
    global lexer
    lexer = lex.lex()
    return parser.parse(input)
