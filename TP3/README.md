# **TPC 3**

### Construir um analisador léxico para a linguagem de query **SPARQL**

---

### **Enunciado**:

Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:

```
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

## Resposta

Utilizando o gerador de analisadores léxicos dado na aula teórica [gen_tokenizer2.py](../TPs/4ªAula/gen_tokenizer2.py), carreguei o gerador com os seguintes tipos de tokens([tokens_par.json](anexos/tokens_par.json)):

```
[
  {
    "id": "SKIP",
    "expreg": "[ \\t]|#.*"
  },
  {
    "id": "INT",
    "expreg": "\\d+"
  },
  {
    "id": "KEYWORD",
    "expreg": "SELECT|AS|WHERE|INSERT|DELETE|PREFIX|FILTER|OPTIONAL|ASK|CONSTRUCT|DESCRIBE|ORDER|BY|ASC|DESC|LIMIT|OFFSET|DISTINCT|REDUCED|UNION|GRAPH|BIND"
  },
  {
    "id": "CA",
    "expreg": "\\{"
  },
  {
    "id": "CF",
    "expreg": "\\}"
  },
  {
    "id": "PA",
    "expreg": "\\("
  },
  {
    "id": "PF",
    "expreg": "\\)"
  },
  {
    "id": "PREFIX",
    "expreg": "[a-zA-Z_][a-zA-Z0-9_]*:[a-z]+"
  },
  {
    "id": "DECPRFX",
    "expreg": "[a-zA-Z_][a-zA-Z0-9_]*:"
  },
  {
    "id": "STRING",
    "expreg": "\\\".*\\\""
  },
  {
    "id": "LINK",
    "expreg": "<.*>"
  },
  {
    "id": "VAR",
    "expreg": "\\?[a-zA-Z_][a-zA-Z0-9_]*"
  },
  {
    "id": "COMP",
    "expreg": ">=|<=|<|>|=="
  },
  {
    "id": "OPERATOR",
    "expreg": "\\*|\\+"
  },
  {
    "id": "ENDLINE",
    "expreg": "\\.$"
  },
  {
    "id": "NEWLINE",
    "expreg": "\\n"
  },
  {
    "id": "ERRO",
    "expreg": "."
  }
]
```

Já com o programa [tokens_SparQL](anexos/tokens_SparQL.py) gerado, corri para um código SPARQL ([teste](anexos/testeShort.txt)):

```
PREFIX schema: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?person ?name ?birthDate
WHERE {
    ?person rdf:type schema:Person .
    ?person schema:name ?name .
    OPTIONAL { ?person schema:birthDate ?birthDate }
}
```

E obtive as seguintes tokens ([resultado](anexos/resulShort.txt)):

```
('KEYWORD', 'PREFIX', 1, (0, 6))
('DECPRFX', 'schema:', 1, (7, 14))
('LINK', '<http://schema.org/>', 1, (15, 35))
('NEWLINE', '\n', 1, (35, 36))
('KEYWORD', 'PREFIX', 2, (0, 6))
('DECPRFX', 'rdf:', 2, (7, 11))
('LINK', '<http://www.w3.org/1999/02/22-rdf-syntax-ns#>', 2, (12, 57))
('NEWLINE', '\n', 2, (57, 58))
('NEWLINE', '\n', 3, (0, 1))
('KEYWORD', 'SELECT', 4, (0, 6))
('VAR', '?person', 4, (7, 14))
('VAR', '?name', 4, (15, 20))
('VAR', '?birthDate', 4, (21, 31))
('NEWLINE', '\n', 4, (31, 32))
('KEYWORD', 'WHERE', 5, (0, 5))
('CA', '{', 5, (6, 7))
('NEWLINE', '\n', 5, (7, 8))
('VAR', '?person', 6, (4, 11))
('PREFIX', 'rdf:type', 6, (12, 20))
('PREFIX', 'schema:Person', 6, (21, 34))
('ENDLINE', '.', 6, (35, 36))
('NEWLINE', '\n', 6, (36, 37))
('VAR', '?person', 7, (4, 11))
('PREFIX', 'schema:name', 7, (12, 23))
('VAR', '?name', 7, (24, 29))
('ENDLINE', '.', 7, (30, 31))
('NEWLINE', '\n', 7, (31, 32))
('KEYWORD', 'OPTIONAL', 8, (4, 12))
('CA', '{', 8, (13, 14))
('VAR', '?person', 8, (15, 22))
('PREFIX', 'schema:birthDate', 8, (23, 39))
('VAR', '?birthDate', 8, (40, 50))
('CF', '}', 8, (51, 52))
('NEWLINE', '\n', 8, (52, 53))
('CF', '}', 9, (0, 1))
```
