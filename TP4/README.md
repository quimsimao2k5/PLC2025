# Máquina de Vending

## Enunciado

---

Pediram-te para construir um programa que simule uma máquina de vending.
A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.

```
stock = [
{"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
...
]
```

Podes persistir essa lista num ficheiro em JSON que é carregado no arranque do programa e é atulizado
quando o programa termina.
A seguir apresenta-se um exemplo de uma interação com a máquina, assim que esta é ligada, para que
possas perceber o tipo de comandos que a máquina aceita (as linhas iniciadas marcadas com `>>`
representam o input do utilizador):

```
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome | quantidade | preço
---------------------------------
A23 água 0.5L 8 0.7
...
>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> SELECIONAR A23
maq: Saldo insufuciente para satisfazer o seu pedido
maq: Saldo = 60c; Pedido = 70c
>> ...
...
maq: Saldo = 74c
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.
maq: Até à próxima
```

O stock encontra-se inicialmente armazenado num ficheiro JSON de nome `"stock.json"` que é carregado
em memória quando o programa arranca. Quando o programa termina, o stock é gravado no mesmo
ficheiro, mantendo assim o estado da aplicação entre interações.
Use a imaginação e criatividade e tente contemplar todos os cenários, por exemplo, produto inexistente ou
stock vazio.
Como extra pode adicionar um comando para adicionar alguns produtos ao stock existente (produtos
novos ou já existentes).

Bom trabalho

## Resposta

Na resolução deste código [Vending](anexos/vending.py) utilizei o módulo `lex` para a geração de tokens.

Defini um analisador léxico, o `dexter = lex.lex()`

---

#### Criei variáveis do analisador:

- `dexter.valor_global` - Valor inserido na máquina
- `dexter.moedas` - Tipo de moedas que a máquina reconhece.

---

#### Defini os seguintes estados para o analisador:

- `moedas` - Estado após receber o sinal MOEDA, indicando que está pronto a acumular dinheiro no `lexer.valor_global`;

- `selec` - Estados após receber o sinal SELECIONAR, esperando um código de um produto.

Defini este estados como **exclusivos**, porque durante estes acontecimentos, quero que apenas reconheça só o que ele deve receber nesses estados, e não aceite tokens gerais. Se não fossem exclusivos aceitariam por exemplo `MOEDA LISTAR` ou `MOEDA SAIR`, e a máquina não pode aceitar esses comandos. Portanto para cada um desses estado tive de criar um `t_'estado'_ignore` porque ele não "herda" o ignore geral.

#### Tokens:

1. `LIST`:
   - **Exp**: 'LISTAR'
   - **Ação**: Imprime o stock no momento
2. `SELEC`:
   - **Exp**: 'SELECIONAR'
   - **Ação**: Inicia o estado `selec`
   1. `COD`:
      - **Exp**: '[A-Z]\d{2}'
      - **Ação**: Verifica se o produto existe, se este tem quantidade e se foi inserido saldo suficiente para comprar o produto, regista a venda e imprime a mensagem de venda. No final volta ao estado `INITIAL`
3. `INS`:
   - **Exp**: 'MOEDA'
   - **Ação**: Inicia o estado `moeda`
   1. `MOEDA`:
      - **Exp**: '2e|1e|50c|20c|10c|5c|2c|1c'
      - **Ação**: Soma o valor da moeda no `dexter.valor_global`
   2. `VIRG`:
      - **Exp**: ','
      - **Ação**: Não faz nada, continua.
   3. `PONTO`:
      - **Exp**: '\\.'
      - **Ação**: Imprime o valor total armazenado na máquina, em `dexter.valor_global`. Por fim volta ao estado `INITIAL`
4. `EXIT`:
   - **Exp**: 'SAIR'
   - **Ação**: Imprime as moedas que deve devolver, e salva os dados do stock no momento.

#### Opções Extra a implementar:

Criar uma opção para carregar a máquina com produtos...
