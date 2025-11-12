from ExpAritanalex import lexer
import sys

prox_simb = ('ERRO',0,0)
valor = 0

def processa_terminal(tipo):
    global prox_simb
    if tipo == prox_simb.type:
          prox_simb = lexer.token()
    else:
         raise ValueError('Invalid token')    

def parserError(simb):
        print('Erro Sintático', simb)
        raise ValueError('Invalid token')

def rec_exp():
    global prox_simb
    rec_term()
    rec_exp1()

def rec_exp1():
    global prox_simb
    if prox_simb is not None and prox_simb.type == '+':
        print('A processar o sinal +')
        processa_terminal('+')
        rec_term()
        rec_exp1()
    elif prox_simb is not None and prox_simb.type == '-':
        print('A processar o sinal -')
        processa_terminal('-')
        rec_term()
        rec_exp1()
    else:
        return
    
def rec_term():
    global prox_simb
    rec_factor()
    rec_term1()

def rec_term1():
    if prox_simb is not None and prox_simb.type == '*':
        print('A processar o sinal *')
        processa_terminal('*')
        rec_factor()
        rec_term1()
    elif prox_simb is not None and prox_simb.type == '/':
        print('A processar o sinal /')
        processa_terminal('/')
        rec_factor()
        rec_term1()
    else:
        return
    
def rec_factor():
    global prox_simb
    if prox_simb is not None and prox_simb.type == '(':
        print('A processar (')
        processa_terminal('(')
        print('A processar Exp dentro de ()')
        rec_exp()
        print('A processar )')
        processa_terminal(')')
    elif prox_simb is not None and prox_simb.type == 'NUM':
        print('A processar NUM')
        processa_terminal('NUM')
    else:
        print('Caracter inválido: ',prox_simb)
        parserError(prox_simb)

def rec_parser(data):
    global prox_simb
    global valor
    lexer.input(data)
    prox_simb = lexer.token()
    print('Analisando a expressao')
    rec_exp()
    print('Acabou a análise sintática com sucesso')

def printTokens(data):
    lexer.input(data)
    for token in lexer:
        print(token)


while True:
    try:
        print('Introduza uma expressão aritmética: ', end="", flush=True)
        linha = sys.stdin.readline()
        if not linha:
            break
        rec_parser(linha)
    except KeyboardInterrupt:
        print("Fim do input")
        break