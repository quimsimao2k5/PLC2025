import ply.lex as lex

literals = ('+','-','*','/','(',')','!','?','=','<','>',':','|','&')

tokens = ('NUM','PRT','VAR','FIM')

t_ignore = '\t '

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = int(t.value)
    return t

def t_FIM(t):
    r'FIM'
    return t

def t_VAR(t):
    r'[a-zA-Z]+'
    return t

def t_error(t):
    print('Carácter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


lexer = lex.lex()

linha = '4*2'

def printTokens(data):
    lexer.input(data)
    for token in lexer:
        print(token)
