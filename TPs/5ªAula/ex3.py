import ply.lex as lex

sql_teste = """
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER
);

INSERT INTO users (name, age) VALUES ('Alice', 30);

SELECT name FROM users WHERE age > 25;
"""

#3.1
tokens = (
    'CREATE',
    'TABLE',
    'INTEGER',
    'PRIMARY',
    'KEY',
    'TEXT',
    'INSERT',
    'INTO',
    'VALUES',
    'SELECT',
    'FROM',
    'WHERE',
    'VAR',
    'INT',
    'MAIOR',
    'PA',
    'PF',
    'PV',
    'STR',
    'VIRG'
)

t_ignore = ' \t'
t_PA = r'\('
t_PF = r'\)'
t_PV = r';'
t_VIRG = r','
t_STR = r'\'.*\''
t_MAIOR = '>'

def t_newline(t):
    r'\n'
    lexer.lineno+=1

def t_CREATE(t):
    r'CREATE'
    return t

def t_KEY(t):
    r'KEY'
    return t

def t_TABLE(t):
    r'TABLE'
    return t

def t_INTEGER(t):
    r'INTEGER'
    return t

def t_PRIMARY(t):
    r'PRIMARY'
    return t

def t_TEXT(t):
    r'TEXT'
    return t

def t_INSERT(t):
    r'INSERT'
    return t

def t_INTO(t):
    r'INTO'
    return t

def t_VALUES(t):
    r'VALUES'
    return t

def t_SELECT(t):
    r'SELECT'
    return t

def t_FROM(t):
    r'FROM'
    return t

def t_WHERE(t):
    r'WHERE'
    return t

def t_VAR(t):
    r'[a-z][a-zA-Z_]+'
    return t

def t_INT(t):
    r'\d+'
    t.value=int(t.value)
    return t

def t_ANY_error(t): # regra válida para todos os estados
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input(sql_teste)

ocorr = {
    "id" : [],
    "string":[],
    "int" : []
}

for token in lexer:
    if token.type == 'VAR' and token.value not in ocorr['id']:
        ocorr['id'].append(token.value)
    elif token.type == 'INT':
        ocorr['int'].append(token.value)
    elif token.type == 'STR':
        ocorr['string'].append(token.value)

print(ocorr)