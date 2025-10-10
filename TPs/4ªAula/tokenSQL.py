
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    mo = re.finditer(r'(?P<keyword>(?:SELECT|FROM|WHERE|INSERT|INTO|VALUES))|(?P<maior>>)|(?P<nomesVariaveis>\w+)|(?P<inteiro>\d+)|(?P<SKIP> \t)|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['keyword']:
            t = ("keyword", dic['keyword'], nlinha, m.span())

        elif dic['maior']:
            t = ("maior", dic['maior'], nlinha, m.span())
    
        elif dic['nomesVariaveis']:
            t = ("nomesVariaveis", dic['nomesVariaveis'], nlinha, m.span())
    
        elif dic['inteiro']:
            t = ("inteiro", dic['inteiro'], nlinha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], nlinha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], nlinha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], nlinha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), nlinha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

nlinha = 1
for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok) 
    nlinha += 1   

