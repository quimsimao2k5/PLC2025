from pythonFeira_analex import lexer,literals,tokens
import ply.yacc as yacc

'''
Program : Program Ins
        | Ins

Ins : "(" READ VAR ")"
    | "(" "=" VAR Exp ")"
    | "(" IF Comp Ins ")"
    | "(" WRITE VAR ")"
    | "(" WHILE Comp Ins ")"

Exp : Exp "-" Term
    | Exp "+" Term
    | Term

Term : Term "*" Fator
    | Term "/" Fator
    | Fator

Fator : INT
    | "(" Exp ")"
    | VAR

Cond : Exp ">" Exp 
    | Exp "<" Exp
'''

# def p_GRAM(p):
#     '''
# Program : LIns
# LIns : LIns Ins
# LIns : Ins
# Ins : "(" READ VAR ")"
# Ins : "(" "=" VAR Exp ")"
# Ins : "(" IF "(" Comp ")" Bloco ")"
# Ins : "(" WRITE VAR ")"
# Ins : "(" WHILE "(" Comp ")" Bloco ")"
# Bloco : Ins
# Bloco : "(" LIns ")"
# Exp : "-" Exp Term
# Exp : "+" Exp Term
# Exp : Term
# Term : "*" Term Fator
# Term : "/" Term Fator
# Term : Fator
# Fator : INT
# Fator : "(" Exp ")"
# Fator : VAR
# Comp : ">" Exp Exp 
# Comp : "<" Exp Exp
# '''

def p_prog(p):
    'Program : LIns RETURN'
    p[0] = p[1]

def p_lins(p):
    'LIns : LIns Ins'
    p[0] = p[1] + [p[2]]

def p_lins1(p):
    'LIns : Ins'
    p[0] = [p[1]]

def p_ins(p):
    'Ins : Var "=" READ "(" ")"'
    p[0] = {'tipo':'READ','var':p[1]}

def p_ins1(p):
    'Ins : Var "=" Exp'
    p[0] = {'tipo':'DECL','var':p[1],'val':p[3]}

def p_ins2(p):
    'Ins : IF Comp ":" INDENT Ins DEDENT ELSE ":" INDENT Ins DEDENT'
    p[0] = {'tipo':'IF','comp':p[2],'true':p[5],'false':p[10]}

def p_ins3(p):
    'Ins : WRITE "(" Exp ")"'
    p[0] = {'tipo':'WRITE','var':p[3]}

def p_ins4(p):
    'Ins : WHILE Comp ":" INDENT Bloco DEDENT'
    p[0] = {'tipo':'WHILE','comp':p[2],'do':p[5]}

def p_exp(p):
    'Exp : Exp "-" Term'
    p[0] = {'tipo':'SUB','first':p[1],'second':p[3]}

def p_exp1(p):
    'Exp : Exp "+" Term'
    p[0] = {'tipo':'ADD','first':p[1],'second':p[3]}

def p_exp2(p):
    'Exp : Term'
    p[0] = p[1]

def p_term(p):
    'Term : Term "*" Fator'
    p[0] = {'tipo':'MUL','first':p[1],'second':p[3]}

def p_term1(p):
    'Term : Term "/" Fator'
    p[0] = {'tipo':'DIV','first':p[1],'second':p[3]}

def p_term2(p):
    'Term : Fator'
    p[0] = p[1]

def p_fator(p):
    'Fator : INT'
    p[0] = {'tipo':'INT','val':p[1]}

def p_fator1(p):
    'Fator : "(" Exp ")"'
    p[0] = p[2]

def p_fator2(p):
    'Fator : Var'
    p[0] = p[1]

def p_var(p):
    'Var : VAR'
    p[0] = {'tipo':'VAR','val':p[1]}

def p_comp(p):
    'Comp : Exp ">" Exp '
    p[0] = {'tipo':'>','first':p[1],'second':p[3]}

def p_comp2(p):
    'Comp : Exp "<" Exp'
    p[0] = {'tipo':'<','first':p[1],'second':p[3]}

def p_error(p):
    msg = "Tá mal amigo"
    parser.error = True
    raise ValueError(msg)

parser = yacc.yacc()
parser.error = False


texto = '''
(read a)
(= f 1)
(while (> a 1)
    (
        (= f (* f a))
        (= a (- a 1))
    )
)
(write f)
'''