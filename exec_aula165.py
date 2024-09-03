# Funções decoradoras e decoradores
# Decorar =  Adicionar / Remover / Restringir / Aletarar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.

def inverte_stgring(string):
    return string[::-1]

invertida = inverte_stgring('Haell')
print(invertida)

frase = "testando desempacotamento + 10"

caracteres = [*frase]

def testaletra(crt):
    if crt.isdigit():
        tipo = "número"
    elif crt.isalpha():
        tipo = "letra"
    elif crt.isspace():
        tipo = "espaço"
    else:
        tipo = "outro"  # Outro tipo de caractere (como símbolos)
    return tipo

for x in caracteres:
    print(f"{x} = {testaletra(x)}")