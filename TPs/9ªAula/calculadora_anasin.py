import ply.yacc as yacc
from calculadora_analex import lexer, literals, tokens

def errorJust(p,razao):
    'Por implementar'
    if razao == 'var':
        if p is None:
            return 'variável inesperada: EOF'
        if p[1] not in parser.valores:
            return f'variável {p[1]} nao está registada'
    if p is None:
        return "Erro sintático: EOF"
    return "Erro sintático: verificar linha"

'''
EXP -> 
'''

'''
! e -> valor da expressao
? v -> valor da variavel
v = e -> declarara variavel
* - printa as variaveis todas
'''

def p_INSTdVar(p):
    'INS : VAR "=" EXP'
    parser.valores[p[1]]=p[3]
    p[0] = f"Variável {p[1]} declarada com o valor {p[3]}"

def p_INSTPRG(p):
    'INS : "?" VAR'
    p[0] = parser.valores[p[2]]

def p_INSTEXP(p):
    'INS : "!" EXP'
    p[0]=p[2]

def p_INSTPRT(p):
    'INS : PRT'
    frase = []
    for l in parser.valores:
        frase.append(f"{l} = {parser.valores[l]}")
    p[0] = '\n'.join(frase)

def p_EXPm(p):
    "EXP : EXP '-' TERM"
    p[0] = p[1] - p[3]

def p_EXPM(p):
    "EXP : EXP '+' TERM"
    p[0] = p[1] + p[3]

def p_EXPT(p):
    'EXP : TERM'
    p[0] = p[1]

def p_TERMV(p):
    'TERM : TERM MUL FATOR'
    p[0] = p[1] * p[3]

def p_TERMD(p):
    'TERM : TERM "/" FATOR'
    p[0] = p[1] / p[3]

def p_TERMFATOR(p):
    'TERM : FATOR'
    p[0] = p[1]

def p_FATORNUM(p):
    'FATOR : NUM'
    p[0] = p[1]

def p_FATOREXP(p):
    'FATOR : "(" EXP ")"'
    p[0] = p[2]

def p_FATORVAR(p):
    'FATOR : VAR'
    if p[1] in parser.valores:
        p[0] = parser.valores[p[1]]
    else:
        p_error(p,'var')

def p_error(p,razao=''):
    parser.success = False
    msg = errorJust(p,razao)
    raise ValueError(msg)

parser = yacc.yacc()
parser.valores = {}
parser.success = True