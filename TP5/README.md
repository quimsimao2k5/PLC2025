# Analisador sintático Expressão Aritmética

## Enunciado

Cria um analisador sintático para as expressões aritméticas.

## Resposta

Para esta gramática

`Tokens = (NUM)`
`Literals = (+,-,\*,/,(,))`

Exp -> Term Exp'
Exp' -> PLUS Term Exp'
| SUB Term Exp'
| epsilon

Term -> Factor Term'
Term' -> MUL Factor Term'
| DIV Factor Term'
| epsilon

Factor -> NUM
| LPAR Exp RPAR

Fiz a análise léxica em [analex.py](anexos/ExpAritanalex.py) e a sintática em [anasin.py](anexos/ExpAritAnasin.py).
