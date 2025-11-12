import ply.lex as lex

tokens=('PA','PF')

t_PA = r'\('
t_PF = r'\)'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = r' \t'

def t_error(t):
    print(f'Carater desconhecido: {t.value}, Linha: {t.lexer.lineno}')
    t.lexer.skip(1)

lexer = lex.lex()

#p1: Par = '(' s ')' s 
#p2:        | epsilon

# First (p1) = First('(' s ')' s) = {'('}
# First (p2) = First(epsilon) = {epsilon} -> Follow(s) = {')',epsilon}

