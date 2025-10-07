# **TPC 3**

### Converter código MD para HTML

---

### **Enunciado**:

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

#### Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: `# Exemplo`

Out: `<h1>Exemplo</h1>`

#### Bold: pedaços de texto entre "\*\*":

In: `Este é um **exemplo** ...`

Out: `Este é um <b>exemplo</b> ...`

#### Itálico: pedaços de texto entre "\*":

In: `Este é um *exemplo* ...`

Out: `Este é um <i>exemplo</i> ...`

#### Lista numerada:

In:

```
1. Primeiro item
2. Segundo item
3. Terceiro item
```

Out:

```
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

#### Link: [texto](endereço URL)

In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`

Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

#### Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: `![imagem dum coelho](http://www.coellho.com) ...`

Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`

---

# Resposta

Para resolver este problema, fiz um código [mdToHTML.py](anexos/mdToHTML.py) que usa o método `sub`, da bibiolteca `re` das expressões regulares, para cada uma das modificações do enunciado.

No total o problema foi composto pelas funções `headers`, `boldORItalic`, `listasNumeros`, `link`e `imagem` que depois operei-as através da substituição das respetivas sintaxes, dentro da função `transicao`.

## Exemplo

Para este código MD:

```
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
```

Para a qual a função `transicao` deu o seguinte resultado:

```
<h1>Processamento de Linguagens e Compiladores</h1>

<h2>Introdução ao Markdown</h2>

O <b>Markdown</b> é uma <i>linguagem de marcação</i> leve que permite formatar texto de forma simples e eficiente. Foi criada por <b><i>John Gruber</i></b> em 2004.

<h3>Características Principais</h3>

<ol>
<li>Simplicidade de uso</li>
<li>Facilidade de leitura</li>
<li>Conversão para HTML</li>
<li>Amplamente adotado</li>
</ol>
<h4>Vantagens do Markdown</h4>

O Markdown oferece várias <b>vantagens importantes</b>:

<ol>
<li>Sintaxe <i>intuitiva</i> e <b>fácil</b> de aprender</li>
<li>Compatibilidade com diversos editores</li>
<li>Ideal para documentação técnica</li>
<li>Suporte nativo no GitHub</li>
</ol>
<h5>Exemplos de Uso</h5>

Podes usar Markdown para:

<ol>
<li>Criar documentação de projetos</li>
<li>Escrever artigos para blogs</li>
<li>Fazer anotações técnicas</li>
<li>Redigir ficheiros README</li>
</ol>
<h6>Links e Imagens</h6>

Para mais informação, visita o <a href="https://daringfireball.net/projects/markdown/">site oficial </a>.

<img src="https://markdown-here.com/img/icon256.png"alt=Logo Markdown </img>

<h2>Conclusão</h2>

O <b><i>Markdown</i></b> revolucionou a forma como escrevemos <i>documentação técnica</i>. A sua <b>simplicidade</b> e <i>versatilidade</i> tornam-no uma ferramenta <b>essencial</b> para qualquer programador.

<h3>Recursos Adicionais</h3>

<ol>
<li>Tutorial completo no <a href="https://guides.github.com/features/mastering-markdown/">GitHub </a></li>
<li>Editor online em <a href="https://dillinger.io/">Dillinger </a></li>
<li>Especificação CommonMark em <a href="https://commonmark.org/">CommonMark </a></li>
</ol>
<img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg"alt=Editor Markdown </img>

<b>Nota:</b> Este texto contém <i>exemplos</i> de <b>formatação</b> <b><i>mista</i></b> para testar todas as funcionalidades.
```
