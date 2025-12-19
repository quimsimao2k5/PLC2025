from pythonFeira_anasin import parser
import sys
import webbrowser
import pyperclip

map_vars = {}
n_vars = 0
n_labels = 0

class VarNaoExiste(Exception):
    pass

def variaveis(ast):
    global n_vars
    if isinstance(ast,list):
        for ins in ast:
            variaveis(ins)
    if isinstance(ast,dict):
        if ast['tipo'] == 'VAR':
            if ast['val'] not in map_vars:
                raise VarNaoExiste(f'Variável {ast["val"]} inexistente!')
        elif ast['tipo'] == 'READ' or ast['tipo'] == 'WRITE' or ast['tipo'] == 'DECL':
            if ast['var']['val'] not in map_vars:
                map_vars[ast['var']['val']] = n_vars
                n_vars +=1

def abre_mato(mens):
    for x in range(len(map_vars)):
        mens.append('pushi 0')

def gera_codigo(mens,ast):
    global n_labels
    if isinstance(ast,list):
        for ins in ast:
            gera_codigo(mens,ins)
    elif isinstance(ast,dict):
        if ast['tipo'] == 'INT':
            mens.append(f'pushi {ast['val']}')
        elif ast['tipo'] == 'VAR':
            mens.append(f'pushg {map_vars[ast['val']]}')
        elif ast['tipo'] == 'READ':
            mens.append('read')
            mens.append('atoi')
            mens.append(f'storeg {map_vars[ast['var']['val']]}')
        elif ast['tipo'] == 'WRITE':
            gera_codigo(mens,ast['var'])
            mens.append('writei')
        elif ast['tipo'] == 'DECL':
            gera_codigo(mens,ast['val'])
            mens.append(f'storeg {map_vars[ast['var']['val']]}')
        elif ast['tipo'] == 'ADD':
            gera_codigo(mens,ast['first'])
            gera_codigo(mens,ast['second'])
            mens.append('add')
        elif ast['tipo'] == 'SUB':
            gera_codigo(mens,ast['first'])
            gera_codigo(mens,ast['second'])
            mens.append('sub')
        elif ast['tipo'] == 'DIV':
            gera_codigo(mens,ast['first'])
            gera_codigo(mens,ast['second'])
            mens.append('div')
        elif ast['tipo'] == 'MUL':
            gera_codigo(mens,ast['first'])
            gera_codigo(mens,ast['second'])
            mens.append('mul')
        elif ast['tipo'] == '>':
            gera_codigo(mens,ast['first'])
            gera_codigo(mens,ast['second'])
            mens.append('sup')
        elif ast['tipo'] == '<':
            gera_codigo(mens,ast['first'])
            gera_codigo(mens,ast['second'])
            mens.append('inf')
        elif ast['tipo'] == 'IF':
            gera_codigo(mens,ast['comp'])
            i1,i2 = n_labels, n_labels + 1
            n_labels +=2
            l1,l2 = 'quim'+str(i1),'quim'+str(i2)
            mens.append(f'jz {l1}')
            gera_codigo(mens,ast['true'])
            mens.append('jump '+l2)
            mens.append(l1 + ':')
            gera_codigo(mens,ast['false'])
            mens.append(l2+':')
        elif ast['tipo'] == 'WHILE':
            i1,i2 = n_labels, n_labels + 1
            n_labels +=2
            l1,l2 = 'quim'+str(i1),'quim'+str(i2)
            mens.append(l1 + ':')
            gera_codigo(mens,ast['comp'])
            mens.append(f'jz {l2}')
            gera_codigo(mens,ast['do'])
            mens.append('jump '+l1)
            mens.append(l2 + ':')
        else:
            mens.append('Nao implementado')


try:
    # Lê TUDO o que o utilizador escrever até dar o sinal de fim (EOF)
    texto_completo = sys.stdin.read()
    
    if texto_completo.strip():
        mens = []
        result = parser.parse(texto_completo)
        variaveis(result)
        abre_mato(mens)
        assembly = gera_codigo(mens,result)
        if not parser.error and result:
            print("\n-------CÓDIGO PARA A VM---------------")
            print('\n'.join(mens))
            with open("sexppp.evm", "w") as f:
                f.write('start\n')
                f.write('\n'.join(mens))
                f.write('\nstop')
            print("--------------------------------------")
            
except ValueError as e:
    print(f"Erro durante o processamento: {e}")
except KeyboardInterrupt:
    print("\nOperação cancelada.")