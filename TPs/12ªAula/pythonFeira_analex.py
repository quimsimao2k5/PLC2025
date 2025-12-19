import ply.lex as lex

ident_level = 0

literals = ['(',')','>','<','=','+','-','*','/',':']

tokens = (
    'READ',
    'WHILE',
    'IF',
    'ELSE',
    'WRITE',
    'VAR',
    'INT',
    'RETURN',
    'INDENT',
    'KEEP',
    'DEDENT'
)

t_ignore = ' \t'

def t_RETURN(t):
    'return'
    return t

def t_READ(t):
    r'input'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WRITE(t):
    r'print'
    return t

def t_VAR(t):
    r'[a-z][a-zA-Z]*'
    return t

def t_INT(t):
    r'\d+'
    return t

def t_newline(t):
    r'\n[ \t]*'
    global ident_level
    t.lexer.lineno += len(t.value)
    i = len(t.value) -1

    if i == ident_level:
        t.type = 'KEEP'
        t.value = i
    elif i>ident_level:
        t.type = 'INDENT'
        t.value = i
        ident_level = i
    elif i<ident_level:
        t.type = 'DEDENT'
        t.value = i
        ident_level = i
    if t.type != 'KEEP':
        return t

def t_error(t):
    print('Carácter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()

texto = '''
n = input()
while n>0:
    if n>0:
        print(n)
    else:
        print(0-n)
    n=n-1
return
'''