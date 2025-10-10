
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    mo = re.finditer(r'(?P<SKIP>[ \t]|#.*)|(?P<INT>\d+)|(?P<KEYWORD>SELECT|AS|WHERE|INSERT|DELETE|PREFIX|FILTER|OPTIONAL|ASK|CONSTRUCT|DESCRIBE|ORDER|BY|ASC|DESC|LIMIT|OFFSET|DISTINCT|REDUCED|UNION|GRAPH|BIND)|(?P<CA>\{)|(?P<CF>\})|(?P<PA>\()|(?P<PF>\))|(?P<PREFIX>[a-z][a-zA-Z0-9_]*:[a-zA-Z0-9_]+)|(?P<DECPRFX>[a-z][a-zA-Z0-9_]*:)|(?P<STRING>\".*\")|(?P<LINK><.*>)|(?P<VAR>\?[a-z][a-zA-Z0-9_]*)|(?P<COMP>>=|<=|<|>|==)|(?P<OPERATOR>\*|\+)|(?P<ENDLINE>\.$)|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['SKIP']:
            t = ("SKIP", dic['SKIP'], nlinha, m.span())

        elif dic['INT']:
            t = ("INT", dic['INT'], nlinha, m.span())
    
        elif dic['KEYWORD']:
            t = ("KEYWORD", dic['KEYWORD'], nlinha, m.span())
    
        elif dic['CA']:
            t = ("CA", dic['CA'], nlinha, m.span())
    
        elif dic['CF']:
            t = ("CF", dic['CF'], nlinha, m.span())
    
        elif dic['PA']:
            t = ("PA", dic['PA'], nlinha, m.span())
    
        elif dic['PF']:
            t = ("PF", dic['PF'], nlinha, m.span())
    
        elif dic['PREFIX']:
            t = ("PREFIX", dic['PREFIX'], nlinha, m.span())
    
        elif dic['DECPRFX']:
            t = ("DECPRFX", dic['DECPRFX'], nlinha, m.span())
    
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], nlinha, m.span())
    
        elif dic['LINK']:
            t = ("LINK", dic['LINK'], nlinha, m.span())
    
        elif dic['VAR']:
            t = ("VAR", dic['VAR'], nlinha, m.span())
    
        elif dic['COMP']:
            t = ("COMP", dic['COMP'], nlinha, m.span())
    
        elif dic['OPERATOR']:
            t = ("OPERATOR", dic['OPERATOR'], nlinha, m.span())
    
        elif dic['ENDLINE']:
            t = ("ENDLINE", dic['ENDLINE'], nlinha, m.span())
    
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

