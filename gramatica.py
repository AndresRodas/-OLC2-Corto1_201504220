from lexico import tokens, analizador
from sys import stdin

from intermediate_code import IntermediateCode


###############SINTACTICO###############
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UMENOS','NOT'),
    ('nonassoc','IG','DIF'),
    ('left','MAS','MENOS'),
    ('left','POR','DIV')
)

#metodos
cont_t = 0
cont_l = 0
def new_temp():
    globals()["cont_t"] += 1
    return 't'+str(cont_t)
def new_label():
    globals()["cont_l"] += 1
    return 'L'+str(cont_l)

# Definición de la gramática
def p_start(t):
    '''start : expresion'''
    out_label = new_label()
    print('********** OUTPUT **********')
    if (t[1].LV != '' and t[1].LF != '' ):
        print(t[1].c3d+t[1].LV+':\n[TrueStatement]\ngoto '+out_label+'\n'+t[1].LF+':\n[FalseStatement]\n'+out_label+':')
    else:
        print(t[1].c3d)

def p_expresion_or(t):
    '''expresion : expresion OR expresion'''
    t[0] = IntermediateCode('','','','')
    t[0].c3d = t[1].c3d + t[1].LF + ':\n' + t[3].c3d
    t[0].LV = t[1].LV + ',' + t[3].LV
    t[0].LF = t[3].LF 

def p_expresion_and(t):
    '''expresion : expresion AND expresion'''
    t[0] = IntermediateCode('','','','')
    t[0].c3d = t[1].c3d + t[1].LV + ':\n' + t[3].c3d
    t[0].LV = t[3].LV
    t[0].LF = t[1].LF + ',' + t[3].LF

def p_expresion_not(t):
    '''expresion : NOT expresion %prec UMENOS'''
    t[0] = IntermediateCode('','','','')
    t[0].LV = t[2].LF
    t[0].LF = t[2].LV
    t[0].c3d = t[2].c3d
    t[0].tmp = t[2].tmp

def p_expresion_diferente(t):
    '''expresion : expresion DIF expresion'''
    t[0] = IntermediateCode('','','','')
    t[0].LV = new_label()
    t[0].LF = new_label()
    t[0].c3d = t[1].c3d + t[3].c3d + 'if ' + t[1].tmp + '!=' + t[3].tmp  + ' goto '+ t[0].LV + '\n' + 'goto ' + t[0].LF + '\n'

def p_expresion_igual(t):
    '''expresion : expresion IG expresion'''
    t[0] = IntermediateCode('','','','')
    t[0].LV = new_label()
    t[0].LF = new_label()
    t[0].c3d = t[1].c3d + t[3].c3d + 'if ' + t[1].tmp + '==' + t[3].tmp +  ' goto '+ t[0].LV + '\n' + 'goto ' + t[0].LF + '\n'

def p_expresion_mas(t):
    '''expresion : expresion MAS expresion'''
    t[0] = IntermediateCode('','','','')
    t[0].tmp = new_temp()
    t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp + '=' + t[1].tmp + '+' + t[3].tmp+'\n'

def p_expresion_menos(t):
    '''expresion : expresion MENOS expresion'''
    t[0] = IntermediateCode('','','','')
    t[0].tmp = new_temp()
    t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp+'=' + t[1].tmp + '-' + t[3].tmp+'\n'

def p_expresion_por(t):
    '''expresion : expresion POR expresion'''
    t[0] = IntermediateCode('','','','')
    t[0].tmp = new_temp()
    t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp + '=' + t[1].tmp + '*' + t[3].tmp+'\n'

def p_expresion_div(t):
    '''expresion : expresion DIV expresion'''
    t[0] = IntermediateCode('','','','')
    t[0].tmp = new_temp()
    t[0].c3d = t[1].c3d + t[3].c3d + t[0].tmp + '=' + t[1].tmp + '/' + t[3].tmp+'\n'

def p_expresion_par(t):    
    '''expresion : PARIZQ expresion PARDER'''
    t[0] = IntermediateCode(t[2].tmp, t[2].c3d,'','')

def p_expresion_val(t):    
    '''expresion : DECIMAL
                    | ENTERO'''
    t[0] = IntermediateCode(str(t[1]), '','','')

def p_error(t):
    print("Error sintáctico '%s'" % t.value, ' en la linea ',t.lexer.lineno)

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print('********** INPUT **********')
print(input+'\n')
parser.parse(input)
