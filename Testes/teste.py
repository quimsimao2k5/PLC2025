import re

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sample Form Page</title>
</head>
<body>
<header id="header">
<h1 id="header-title">Contact Us</h1>
</header>
<div id="form-container">
<form id="contact-form">
<div class="form-group" id="name-group">
<label for="name" id="name-label">Name:</label>
<input type="text" id="name" name="name">
</div>
<div class="form-group" id="email-group">
<label for="email" id="email-label">Email:</label>
<input type="email" id="email" name="email">
</div>
<div class="form-group" id="message-group">
<label for="message" id="message-label">Message:</label>
<textarea id="message" name="message" rows="4"></textarea>
</div>
<button type="submit" id="submit-btn">Submit</button>
</form>
</div>
<footer id="footer">
<p id="footer-text">&copy; 2024 Sample Form Page</p>
</footer>
</body>
</html>
"""
r = sorted(re.findall(r'id\s*=\s*\"([^\" \t]+)\"', html))

print(r)

g = True

abre = set(re.findall(r'<([a-z]+)[^>]*>',html))
for i in re.findall(r'</([a-z]+)>',html):
    if i not in abre:
        print(i,": Não abriu")
        g=False
print("ta tudo") if g == True else print("deu merda")

nomes = """Josefina Maria Carvalho Ramos
João Rui Carvalho
José Carlos Leite Ramalho
Pedro Rangel Henriques
Tiago João Fernandes Batista
"""

def check_sigla(txt:str,sigla:str):
    d={}
    r=[]
    sigla = sigla.upper()
    sigla = '.*'.join(list(sigla))
    for i in re.findall(r'^[A-ZÁÉÍÓÚ][a-záãâéíóõú]+(?: +[A-ZÁÉÍÓÚ][a-záãâéíóõú]+)*$',txt,flags=re.MULTILINE):
        d[i] = ''.join(re.findall(r'[A-Z]',i))
        if re.search(sigla,d[i]):
            r.append(i)
    return r

print(check_sigla(nomes,'jcr'))

'''
Pais : Llocais

Llocais : Llocais ';' Local
Llocais : Local

Local : nome Lpint

Lpint : Lpint ',' Pint
Lpint : Pint

Pint : tipo ':' nome ':' preco
'''