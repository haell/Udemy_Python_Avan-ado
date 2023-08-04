
pessoa1 = {
    'nome' : 'Haell',
    'idade' : 41
}

dados_pessoa = {
    'peso' : 75,
    'altura' : 1.74
}

pessoa_completa = {**pessoa1, **dados_pessoa}


""" for indice, dado in pessoa_completa.items():
    print(f"{indice} = {dado}")
    print('-'*15)
for k in pessoa_completa.keys():
    print(f"{k}") """

def mostro_argumentos_nomeados(*args, **doqeuquiser):
    if len(args) > 0:
        for ind, item in enumerate(args):
            print(f"{ind+1}° não nomeado: {item}")
    for chave, valor in doqeuquiser.items():
        print(f"{chave}: {valor}")

teste1 = 121 % 3.33

# mostro_argumentos_nomeados('bola', 2, teste1, 3, True, (5+2),  **pessoa_completa)

configuracoes = {
    'menu - 1': 1,
    'menu - 2': 2,
    'menu - 3': 3,
    'menu - 4': 4,
    'menu - 5': 5,
}

mostro_argumentos_nomeados(**configuracoes)


