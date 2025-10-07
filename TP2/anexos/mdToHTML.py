import re

codMD = """
# Processamento de Linguagens e Compiladores

## Introdução ao Markdown

O **Markdown** é uma *linguagem de marcação* leve que permite formatar texto de forma simples e eficiente. Foi criada por ***John Gruber*** em 2004.

### Características Principais

1. Simplicidade de uso
2. Facilidade de leitura
3. Conversão para HTML
4. Amplamente adotado

#### Vantagens do Markdown

O Markdown oferece várias **vantagens importantes**:

1. Sintaxe *intuitiva* e **fácil** de aprender
2. Compatibilidade com diversos editores
3. Ideal para documentação técnica
4. Suporte nativo no GitHub

##### Exemplos de Uso

Podes usar Markdown para:

1. Criar documentação de projetos
2. Escrever artigos para blogs
3. Fazer anotações técnicas
4. Redigir ficheiros README

###### Links e Imagens

Para mais informação, visita o [site oficial](https://daringfireball.net/projects/markdown/).

![Logo Markdown](https://markdown-here.com/img/icon256.png)

## Conclusão

O ***Markdown*** revolucionou a forma como escrevemos *documentação técnica*. A sua **simplicidade** e *versatilidade* tornam-no uma ferramenta **essencial** para qualquer programador.

### Recursos Adicionais

1. Tutorial completo no [GitHub](https://guides.github.com/features/mastering-markdown/)
2. Editor online em [Dillinger](https://dillinger.io/)
3. Especificação CommonMark em [CommonMark](https://commonmark.org/)

![Editor Markdown](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)

**Nota:** Este texto contém *exemplos* de **formatação** ***mista*** para testar todas as funcionalidades.
"""

def headers(match):
    n = len(match.group(1))
    if n>6:
        return match.group(0)
    else:
        return f"<h{n}>{match.group(2)}</h{n}>"
    
def boldORItalic(match,i=False):
    if i:
        match = re.match(r"(\*+)([^*]+)(\1)",match)
    n = len(match.group(1))
    if n == 1: # italico
        return f"<i>{match.group(2)}</i>"
    elif n == 2: #bold
        return f"<b>{match.group(2)}</b>"
    else:
        r = match.group(0)
        r = re.match(r"\*\*(\*+[^*]+\*+)\*\*",r)
        return f"<b>{boldORItalic(r.group(1),True)}</b>"
    

def listasNumeros(match):
    tudo = match.group(0)
    result = ["<ol>"]
    for m in re.finditer(r"(?:\d+. (.+)\n)",tudo):
        result.append(f"<li>{m.group(1)}</li>")
    result.append("</ol>")
    return "\n".join(result)

def link(match):
    return f"<a href=\"{match.group(2)}\">{match.group(1)} </a>"

def imagem(match):
    return f"<img src=\"{match.group(2)}\"alt={match.group(1)} </img>"

def transicao(texto):
    texto = re.sub(r"^(#+) (.*)$",headers,texto,flags=re.MULTILINE)
    texto = re.sub(r"(\*+)([^*]+)(\1)",boldORItalic,texto)
    texto = re.sub(r"!\[([^\]]+)\]\(([^)]+)\)",imagem,texto)
    texto = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",link,texto)
    texto = re.sub(r"(?:\d+. .+\n)+",listasNumeros,texto)
    return texto

print(transicao(codMD))