from calculadora_anasin import parser
import sys

print(
'''
! e -> valor da expressao
? v -> valor da variavel
v = e -> declarara variavel
* - printa as variaveis todas
'''
)


while True:
    try:
        print('>> ', end="", flush=True)
        linha = sys.stdin.readline()
        if not linha:
            break
        try:
            result = parser.parse(linha)
        except ValueError as e:
            print(e)
            result = None
        if parser.success:
            print(result)
    except KeyboardInterrupt:
        print("A fechar a calculadora...")
        break