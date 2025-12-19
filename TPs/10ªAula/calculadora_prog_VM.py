from calculadora_anasin_VM import parser
import sys

map_vars = {}
n_vars = 0
n_labels = 0

class VarNaoExiste(Exception):
    pass

def variaveis(ast):
    global n_vars
    
    # Se for uma lista de instruções (início)
    if isinstance(ast, list):
        for instrucao in ast:
            variaveis(instrucao)
        return
    
    if isinstance(ast,tuple):
        if ast[0]=='VAR_ATRIB':
            nome = ast[1]
            pos = n_vars
            if nome not in map_vars:
                map_vars[nome] = pos
                n_vars +=1
        elif ast[0]=='VAR_VAL':
            if ast[1] not in map_vars:
                raise VarNaoExiste(f"Men a var {ast[1]} não existe")
        else:
            return

def abreMato(mens):
    for x in map_vars:
        mens.append('pushi 0')

def instrucoes(mens:list,ast:list):
    '''
    Recebe uma lista tipo [('VALEXP', ('ADD', ('NUM', 1), ('NUM', 1)))]
    
    Casos:
    - VAR_ATRIB ✓
    - VAR_VAL 
    - EXP_VAL
    - VAR_PRINT
    - EXP_SUB
    - EXP_ADD
    - EXP_MUL
    - EXP_DIV
    - VAR_CALL
    - EXP_COND
    - EXP_OR
    - EXP_AND
    - GREATER
    - LESS
    - NUM ✓
    '''

    if isinstance(ast,list):
        for ins in ast:
            if ins[0] == 'NUM':
                mens.append(f'pushi {ins[1]}')
            elif ins[0]=='VAR_ATRIB':
                nome = ins[1]
                exp = ins[2]
                instrucoes(mens,exp)
                mens.append(f'storeg {map_vars[nome]}')
            elif ins[0]=='VAR_VAL':
                nome = ins[1]
                mens.append(f'pushg {map_vars[nome]}')
                mens.append('writei')
            elif ins[0]=='VAR_PRINT':
                for m in map_vars:
                    mens.append(f'pushs "{m}:"')
                    mens.append('writes')
                    mens.append(f'pushg {map_vars[m]}')
                    mens.append('writei')
            elif ins[0]=='VAR_CALL':
                mens.append(f'pushg {map_vars[ins[1]]}')
            elif ins[0]=='EXP_VAL':
                instrucoes(mens,ins[1])
                mens.append('pushs "Result: "')
                mens.append('writes')
                mens.append('writei')
                mens.append('writeln')
            elif ins[0]=='EXP_SUB':
                instrucoes(mens,ins[1])
                instrucoes(mens,ins[2])
                mens.append('sub')
            elif ins[0]=='EXP_ADD':
                instrucoes(mens,ins[1])
                instrucoes(mens,ins[2])
                mens.append('add')
            elif ins[0]=='EXP_MUL':
                instrucoes(mens,ins[1])
                instrucoes(mens,ins[2])
                mens.append('mul')
            elif ins[0]=='EXP_DIV':
                instrucoes(mens,ins[1])
                instrucoes(mens,ins[2])
                mens.append('div')
            elif ins[0]=='EXP_COND':
                instrucoes(mens,ins[1])
                i1,i2 = n_labels, n_labels + 1
                n_labels +=2
                l1,l2 = 'quim'+str(i1),'quim'+str(i2)
                mens += instrucoes(mens,ins[1]) + [f'jz {l1}'] + instrucoes(mens,ins[2]) + [f'jump {l2}'] + [l1+':'] + instrucoes(mens,ins[3]) + [l2+':']
            elif ins[0]=='EXP_OR':
                instrucoes(mens,ins[1])
                instrucoes(mens,ins[2])
                mens.append('or')
            elif ins[0]=='EXP_AND':
                instrucoes(mens,ins[1])
                instrucoes(mens,ins[2])
                mens.append('or')
            elif ins[0]=='GREATER':
                instrucoes(mens,ins[1])
                instrucoes(mens,ins[2])
                mens.append('sup')
            elif ins[0]=='LESS':
                instrucoes(mens,ins[1])
                instrucoes(mens,ins[2])
                mens.append('inf')
            else:
                pass
    else:
        if ast[0] == 'NUM':
            mens.append(f'pushi {ast[1]}')
        elif ast[0]=='VAR_ATRIB':
            nome = ast[1]
            exp = ast[2]
            instrucoes(mens,exp)
            mens.append(f'storeg {map_vars[nome]}')
        elif ast[0]=='VAR_VAL':
            nome = ast[1]
            mens.append(f'pushg {map_vars[nome]}')
            mens.append('writei')
        elif ast[0]=='VAR_PRINT':
            for m in map_vars:
                mens.append(f'pushs "{m}:"')
                mens.append('writes')
                mens.append(f'pushg {map_vars[m]}')
                mens.append('writei')
        elif ast[0]=='VAR_CALL':
            mens.append(f'pushg {map_vars[ast[1]]}')
        elif ast[0]=='EXP_VAL':
            instrucoes(mens,ast[1])
            mens.append('pushs "Result: "')
            mens.append('writes')
            mens.append('writei')
            mens.append('writeln')
        elif ast[0]=='EXP_SUB':
            instrucoes(mens,ast[1])
            instrucoes(mens,ast[2])
            mens.append('sub')
        elif ast[0]=='EXP_ADD':
            instrucoes(mens,ast[1])
            instrucoes(mens,ast[2])
            mens.append('add')
        elif ast[0]=='EXP_MUL':
            instrucoes(mens,ast[1])
            instrucoes(mens,ast[2])
            mens.append('mul')
        elif ast[0]=='EXP_DIV':
            instrucoes(mens,ast[1])
            instrucoes(mens,ast[2])
            mens.append('div')
        elif ast[0]=='EXP_COND':
            instrucoes(mens,ast[1])
            i1,i2 = n_labels, n_labels + 1
            n_labels +=2
            l1,l2 = 'quim'+str(i1),'quim'+str(i2)
            mens += instrucoes(mens,ast[1]) + [f'jz {l1}'] + instrucoes(mens,ast[2]) + [f'jump {l2}'] + [l1+':'] + instrucoes(mens,ast[3]) + [l2+':']
        elif ast[0]=='EXP_OR':
            instrucoes(mens,ast[1])
            instrucoes(mens,ast[2])
            mens.append('or')
        elif ast[0]=='EXP_AND':
            instrucoes(mens,ast[1])
            instrucoes(mens,ast[2])
            mens.append('or')
        elif ast[0]=='GREATER':
            instrucoes(mens,ast[1])
            instrucoes(mens,ast[2])
            mens.append('sup')
        elif ast[0]=='LESS':
            instrucoes(mens,ast[1])
            instrucoes(mens,ast[2])
            mens.append('inf')
        else:
            pass

print(
'''
Escreve o teu programa completo.
Quando terminares, pressiona:
- Windows: Ctrl+Z e depois Enter
- Linux/Mac: Ctrl+D
'''
)

print(
'''
! e -> valor da expressao
? v -> valor da variavel
v = e -> declarara variavel
* - printa as variaveis todas
condicional : cond ? a : b
'''
)

try:
    # Lê TUDO o que o utilizador escrever até dar o sinal de fim (EOF)
    texto_completo = sys.stdin.read()
    
    if texto_completo.strip():
        mens = []
        result = parser.parse(texto_completo)
        variaveis(result)
        abreMato(mens)
        assembly = instrucoes(mens,result)
        if not parser.error and result:
            print("\n-------CÓDIGO PARA A VM---------------")
            print('\n'.join(mens))
            with open("calculadora.evm", "w") as f:
                f.write('start\n')
                f.write('\n'.join(mens))
                f.write('\nstop')
            print("--------------------------------------")
            
except ValueError as e:
    print(f"Erro durante o processamento: {e}")
except KeyboardInterrupt:
    print("\nOperação cancelada.")