import ply.lex as lex

literals = ['(',')','>','<','=','+','-','*','/']

tokens = (
    'READ',
    'WHILE',
    'IF',
    'WRITE',
    'VAR',
    'INT'
)

t_ignore = ' \t'

def t_READ(t):
    r'read'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_IF(t):
    r'if'
    return t

def t_WRITE(t):
    r'write'
    return t

def t_VAR(t):
    r'[a-z][a-zA-Z]*'
    return t

def t_INT(t):
    r'\d+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print('Carácter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()