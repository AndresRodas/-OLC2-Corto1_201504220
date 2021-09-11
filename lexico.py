import ply.lex as lex

tokens = [
    'PARIZQ',
    'PARDER',
    'POR',
    'MAS',
    'MENOS',
    'DIV',
    'DIF',
    'IG',
    'OR',
    'AND',
    'NOT',
    'DECIMAL',
    'ENTERO'
]

#tokens
t_POR = r'\*'
t_MAS = r'\+'
t_MENOS = r'-'
t_DIV = r'/'
t_DIF = r'!='
t_IG = r'=='
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_ignore = " \t"


#detecta cuando es un decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t


#detecta cuando es un entero 
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('integer value too large %d', t.value)
        t.value = 0
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#funcion de error 
def t_error(t):
    print ("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)
    return t

#se instancia el analiador lexico
analizador = lex.lex()












