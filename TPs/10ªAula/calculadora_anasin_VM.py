import ply.yacc as yacc
from calculadora_analex_VM import lexer, literals, tokens

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
PROG : PROG INS 
    | INS
    | FIM

INS : VAR "=" EXP
    | "?" VAR
    | "!" EXP
    | "*"

EXP : EXP "-" TERM
    | EXP "+" TERM
    | TERM

TERM : TERM "*" FATOR
    | TERM "/" FATOR
    | FATOR

FATOR : NUM
    | "(" EXP ")"
    | VAR
    | COND "?" EXP : EXP

COND : COND "|" CONJ
    | CONJ

CONJ : CONJ "&" COMP
    | COMP

COMP : EXP ">" EXP
    | EXP "<" EXP
...
'''

'''
! e -> valor da expressao
? v -> valor da variavel
v = e -> declarara variavel
* - printa as variaveis todas
'''

def p_program(p):
    'PROG : PROG INS'
    p[0] = p[1] + [p[2]]

def p_programIns(p):
    'PROG : INS'
    p[0] = [p[1]]

def p_programFim(p):
    'PROG : FIM'
    parser.end = True

def p_INSdVar(p):
    'INS : VAR "=" EXP'
    p[0] = ('VAR_ATRIB',p[1],p[3])

def p_INSPRG(p):
    'INS : "?" VAR'
    p[0] = ('VAR_VAL',p[2])

def p_INSEXP(p):
    'INS : "!" EXP'
    p[0]=('EXP_VAL',p[2])

def p_INSPRT(p):
    'INS : "*"'
    p[0] = ('VAR_PRINT',p[1])

def p_EXPm(p):
    "EXP : EXP '-' TERM"
    p[0] = ('EXP_SUB',p[1],p[3])

def p_EXPM(p):
    "EXP : EXP '+' TERM"
    p[0] = ('EXP_ADD',p[1],p[3])

def p_EXPT(p):
    'EXP : TERM'
    p[0] = p[1]

def p_TERMV(p):
    'TERM : TERM "*" FATOR'
    p[0] = ('EXP_MUL',p[1],p[3])

def p_TERMD(p):
    'TERM : TERM "/" FATOR'
    p[0] = ('EXP_DIV',p[1],p[3])

def p_TERMFATOR(p):
    'TERM : FATOR'
    p[0] = p[1]

def p_FATORNUM(p):
    'FATOR : NUM'
    p[0] = ('NUM',p[1])

def p_FATOREXP(p):
    'FATOR : "(" EXP ")"'
    p[0] = p[2]

def p_FATORVAR(p):
    'FATOR : VAR'
    p[0] = ('VAR_CALL',p[1])

def p_FATORCOND(p):
    'FATOR : COND "?" EXP ":" EXP'
    p[0] = ('EXP_COND',p[1],p[3],p[5])

def p_CONDCONDJ(p):
    'COND : COND "|" CONJ'
    p[0] = ('EXP_OR',p[1],p[3])

def p_CONDCONJ(p):
    'COND : CONJ'
    p[0] = p[1]

def p_CONJCONJP(p):
    'CONJ : CONJ "&" COMP'
    p[0] = ('EXP_AND',p[1],p[3])

def p_CONJCOMP(p):
    'CONJ : COMP'
    p[0] = p[1]

def p_COMPG(p):
    'COMP : EXP ">" EXP'
    p[0] = ('GREATER',p[1],p[3])

def p_COMPL(p):
    'COMP : EXP "<" EXP'
    p[0] = ('LESS',p[1],p[3])

def p_error(p):
    parser.error = True
    msg = "Tá mal amigo"
    raise ValueError(msg)

parser = yacc.yacc()
parser.error = False
parser.end = False