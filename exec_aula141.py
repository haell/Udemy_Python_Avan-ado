# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = { 
    chave.capitalize(): valor.upper() 
    if isinstance(valor, str) else valor 
    for chave, valor 
    in produto.items()
    if chave == 'categoria' # Filtro
    }

print(dc)


lista_exemplo = [
    ('a', 'item 1'),
    ('b', 'item 2'),
    ('c', 'item 3'),
]

""" dc = { 
    chave: valor
    for chave, valor in lista_exemplo
} """

print(dict(lista_exemplo))

s1 = {
    2 ** i for i in range(10)
}

print(s1)
