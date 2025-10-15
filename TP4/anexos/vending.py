import json
import ply.lex as lex
import sys
from math import modf
import datetime as time
from pathlib import Path

here = Path(__file__).resolve().parent
stock_path = here / "stock.json"
with stock_path.open("r", encoding="utf-8") as f:
    stock = json.load(f)

def existeId(id):
    return id in [prod["cod"] for prod in stock]
    
def getProduto(id):
    r = [prod["nome"] for prod in stock if prod["cod"]==id]
    return r[0] if r else None
    
def temDinheiro(id):
    val = [prod["preco"] for prod in stock if prod["cod"]==id]
    if not val:
        return (False, None)
    preco = float(val[0])
    return (dexter.valor_global >= preco, preco)
    
def temQuantidade(id):
    prodLi = [prod.get("quant", 0) for prod in stock if prod["cod"]==id]
    if not prodLi:
        return False
    qProd = int(prodLi[0])
    return qProd if qProd > 0 else False
    
def vendeProd(id):
    for p in stock:
        if p["cod"] == id:
            p["quant"] = max(0, p.get("quant",0) - 1)
    return

def arranjaTroco(val):
    moeda = {}
    while val>0:
        val = round(float(val),2)
        for m in dexter.moedas:
            if val>=m:
                if m not in moeda:
                    moeda[m]=0
                moeda[m]+=1
                val-=m
                break
    result = ""
    for m in dexter.moedas:
        if m in moeda:
            if m>=1:
                result += f" {moeda[m]}x {m}e,"
            else:
                result += f" {moeda[m]}x {int(m*100)}c,"
    result = result[:-1]
    result += "."
    return result


def print_stock(items):
    # headings
    headers = ("Cod", "Nome", "Quant", "Preço", "Valor")
    # compute formatted rows and column widths
    rows = []
    for it in items:
        cod = it.get("cod", "")
        nome = it.get("nome", "")
        quant = int(it.get("quant", 0))
        preco = float(it.get("preco", 0.0))
        valor = quant * preco
        rows.append((cod, nome, f"{quant}", f"{preco:.2f}", f"{valor:.2f}"))
    widths = [max(len(h), *(len(r[i]) for r in rows)) for i, h in enumerate(headers)]
    # print header
    hdr = " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    sep = "-+-".join("-" * widths[i] for i in range(len(headers)))
    print(hdr)
    print(sep)
    # print rows
    for r in rows:
        print(" | ".join(r[i].ljust(widths[i]) if i in (0,1) else r[i].rjust(widths[i]) for i in range(len(headers))))
    # totals
    total_qty = sum(int(it.get("quant",0)) for it in items)
    total_val = sum(int(it.get("quant",0)) * float(it.get("preco",0.0)) for it in items)
    print(sep)
    print(f"{'TOTAL'.ljust(widths[0]+widths[1]+3)} {str(total_qty).rjust(widths[2])} | {total_val:.2f}".rjust(widths[2]+widths[3]+widths[4]+6))

states = (
    ('moeda','exclusive'),
    ('selec','exclusive')
)

tokens = (
    'LIST', #ta
    'SELC', #ta
    'COD', #ta
    'INS', #ta
    'CARR',
    'MOEDA', #ta
    'VIRG', #ta
    'PONT', #ta
    'EXIT'
)

t_ignore = ' \t\n'

t_moeda_ignore = ' \t'
t_selec_ignore = ' \t'

def t_LIST(t):
    r'LISTAR'
    print_stock(stock)
    return t

def t_SELC(t):
    r"SELECIONAR"
    t.dexter.begin('selec')
    return t

def t_selec_COD(t):
    r'[A-Z]\d{2}'
    prod_id = t.value
    nomeProd = getProduto(prod_id)
    exist = existeId(prod_id)
    qnt = temQuantidade(prod_id)
    din_ok, preco = temDinheiro(prod_id)
    if exist and qnt and din_ok:
        dexter.valor_global -= preco
        vendeProd(prod_id)
        print(f"maq: Pode retirar o produto dispensado: {nomeProd}")
    elif not exist:
        print("Código inválido")
    elif not qnt:
        print(f"maq: Sem stock de {nomeProd}")
    elif not din_ok:
        print(f"maq: Saldo insuficiente: {dexter.valor_global:.2f}€. Precisa de {preco:.2f}€.")
    else:
        print("maq: Ocorreu um problema, volte mais tarde. Obrigado!")
    t.dexter.begin('INITIAL')
    return None

def t_INS(t):
    r'MOEDA'
    t.dexter.begin('moeda')
    return t

def t_moeda_MOEDA(t):
    r'2e|1e|50c|20c|10c|5c|2c|1c'
    val = t.value
    if val[-1] == 'e':
        dexter.valor_global += int(val[0])
    elif val[-1] == 'c':
        dexter.valor_global += (float(val[:-1])/100)
    return t

def t_moeda_VIRG(t):
    r','
    return t

def t_moeda_PONTO(t):
    r'\.'
    f,w=modf(dexter.valor_global)
    print(f"maq: Saldo = {int(w)}e {int(round(f*100,2))}c")
    t.dexter.begin('INITIAL')

def t_EXIT(t):
    r'SAIR'
    print(f"Pode retirar o seu troco: {arranjaTroco(dexter.valor_global)}")
    print("Até à próxima")
    with stock_path.open("w", encoding="utf-8") as fw:
        json.dump(stock, fw, ensure_ascii=False, indent=2)
    return t

def t_ANY_error(t): # regra válida para todos os estados
    print(f"Carácter ilegal: {t.value[0]}")
    t.dexter.skip(1)

dexter = lex.lex()
dexter.valor_global = 0.0
dexter.moedas = [2,1,0.5,0.2,0.1,0.05,0.02,0.01]

stop = False
print(f"maq: {time.datetime.now()}, Stock carregado, Estado atualizado.")
print("maq: Bom dia. Estou disponível para atender o seu pedido.")
if sys.stdin.isatty():
    # modo interativo: usa input() com prompt ">> "
    while True:
        try:
            linha = input(">> ").strip()
        except EOFError:
            break
        if not linha:
            continue
        dexter.input(linha)
        while True:
            tok = dexter.token()
            if not tok:
                break
            if tok.type == 'EXIT':
                stop = True
                break
        dexter.begin('INITIAL')
        if stop:
            break
else:
    # modo não-interativo (piped/file): não mostrar prompt, apenas processar linhas
    for linha in sys.stdin:
        linha = linha.strip()
        if not linha:
            continue
        dexter.input(linha)
        while True:
            tok = dexter.token()
            if not tok:
                break
            if tok.type == 'EXIT':
                stop = True
                break
        dexter.begin('INITIAL')
        if stop:
            break