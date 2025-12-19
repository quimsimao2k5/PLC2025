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
    | PRT

EXP : EXP "-" TERM
    | EXP "+" TERM
    | TERM

TERM : TERM MUL FATOR
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
    p[0] = p[1] + '\n' + '\n'.join(p[2])

def p_programIns(p):
    'PROG : INS'
    p[0] = '\n'.join(p[1])

def p_programFim(p):
    'PROG : FIM'
    parser.end = True

def p_INSdVar(p):
    'INS : VAR "=" EXP'
    parser.valores[p[1]]=p[3]
    p[0] = f"Variável {p[1]} declarada com o valor {p[3]}"

def p_INSPRG(p):
    'INS : "?" VAR'
    p[0] = parser.valores[p[2]]

def p_INSEXP(p):
    'INS : "!" EXP'
    p[0]=p[2] + ['pushs "Result: "','writes','writei'] 

def p_INSPRT(p):
    'INS : PRT'
    frase = []
    for l in parser.valores:
        frase.append(f"{l} = {parser.valores[l]}")
    p[0] = '\n'.join(frase)

def p_EXPm(p):
    "EXP : EXP '-' TERM"
    p[0] = p[1] - p[3] + ['sub']

def p_EXPM(p):
    "EXP : EXP '+' TERM"
    p[0] = p[1] + p[3] + ['add']

def p_EXPT(p):
    'EXP : TERM'
    p[0] = p[1]

def p_TERMV(p):
    'TERM : TERM MUL FATOR'
    p[0] = p[1] + p[3] + ['mul']

def p_TERMD(p):
    'TERM : TERM "/" FATOR'
    p[0] = p[1] + p[3] + ['div']

def p_TERMFATOR(p):
    'TERM : FATOR'
    p[0] = p[1]

def p_FATORNUM(p):
    'FATOR : NUM'
    p[0] = [f"pushi {p[1]}"]

def p_FATOREXP(p):
    'FATOR : "(" EXP ")"'
    p[0] = p[2]

def p_FATORVAR(p):
    'FATOR : VAR'
    if p[1] in parser.valores:
        p[0] = parser.valores[p[1]]
    else:
        p_error(p,'var')

def p_FATORCOND(p):
    'FATOR : COND "?" EXP ":" EXP'
    i1,i2 = parser.nLabels, parser.nLabels + 1
    parser.nLabels +=2
    l1,l2 = 'quim'+str(i1),'quim'+str(i2)
    p[0] = p[1] + [f'jz {l1}'] + p[3] + [f'jump {l2}'] + [l1+':'] + p[5] + [l2+':']

def p_CONDCONDJ(p):
    'COND : COND "|" CONJ'
    p[0] = p[1] + p[3] + ["or"]

def p_CONDCONJ(p):
    'COND : CONJ'
    p[0] = p[1]

def p_CONJCONJP(p):
    'CONJ : CONJ "&" COMP'
    p[0] = p[1] + p[2] + ["and"]

def p_CONJCOMP(p):
    'CONJ : COMP'
    p[0] = p[1]

def p_COMPG(p):
    'COMP : EXP ">" EXP'
    p[0] = p[1] + p[3] + ["sup"]

def p_COMPL(p):
    'COMP : EXP "<" EXP'
    p[0] = p[1] + p[3] + ["inf"]

def p_error(p):
    parser.error = True
    msg = "Tá mal amigo"
    raise ValueError(msg)

parser = yacc.yacc()
parser.error = False