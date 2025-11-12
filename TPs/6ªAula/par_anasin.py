from par_analex import lexer

prox_simb = None

def parserError(simb):
        print('Erro Sintático', simb)

def processa_terminal(tipo):
    global prox_simb
    if tipo == prox_simb.type:
          prox_simb = lexer.token()
    else:
         raise ValueError('Invalid token')

def rec_S():
    global prox_simb
    if prox_simb is None or prox_simb.type == 'PF':
         print('S -> epsilon')
         pass
    elif prox_simb.type == 'PA':
        print('S -> ( S ) S')
        processa_terminal('PA')
        rec_S()
        processa_terminal('PF')
        rec_S()
    else:
         parserError(prox_simb)

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_S()
    if prox_simb is not None:
        parserError(prox_simb)
    print("That's all folks!")

rec_Parser('(()))))')