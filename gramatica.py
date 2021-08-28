from lexico import tokens, analizador
from sys import stdin

from intermediate_code import IntermediateCode


###############SINTACTICO###############
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIV')
)

#metodos
temp = 0
def new_temp():
    globals()["temp"] += 1
    return 't'+str(temp)

# Definición de la gramática
def p_start(t):
    '''start : INPUT expresion'''
    print('Output:\n'+t[2].c3d)

def p_expresion_mas(t):
    '''expresion : expresion MAS t_expresion'''
    t[0] = IntermediateCode('','')
    t[0].tmp = new_temp()
    t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp + '=' + t[1].tmp + '+' + t[3].tmp+'\n'

def p_expresion_menos(t):
    '''expresion : expresion MENOS t_expresion'''
    t[0] = IntermediateCode('','')
    t[0].tmp = new_temp()
    t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp+'=' + t[1].tmp + '-' + t[3].tmp+'\n'

def p_expresion_t(t):
    '''expresion : t_expresion'''
    t[0] = IntermediateCode(t[1].tmp, t[1].c3d)

def p_t_expresion_por(t):
    '''t_expresion : t_expresion POR f_expresion'''
    t[0] = IntermediateCode('','')
    t[0].tmp = new_temp()
    t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp + '=' + t[1].tmp + '*' + t[3].tmp+'\n'

def p_t_expresion_div(t):
    '''t_expresion : t_expresion DIV f_expresion'''
    t[0] = IntermediateCode('','')
    t[0].tmp = new_temp()
    t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp + '=' + t[1].tmp + '/' + t[3].tmp+'\n'

def p_t_expresion_f(t):
    '''t_expresion : f_expresion'''
    t[0] = IntermediateCode(t[1].tmp, t[1].c3d)

def p_f_expresion_par(t):    
    '''f_expresion : PARIZQ expresion PARDER'''
    t[0] = IntermediateCode(t[2].tmp, t[2].c3d)

def p_f_expresion_val(t):    
    '''f_expresion : DECIMAL
                    | ENTERO'''
    t[0] = IntermediateCode(str(t[1]), '')

def p_error(t):
    print("Error sintáctico '%s'" % t.value, ' en la linea ',t.lexer.lineno)

import ply.yacc as yacc
parser = yacc.yacc()


f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)
