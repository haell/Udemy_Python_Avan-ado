def saudacao(msg, nome):
    return f'{msg}, {nome}!'

""" saudacao_2 = saudacao
v = saudacao_2('Bom dia')
print(v)
 """
def executa(funcao, *args):
    return funcao(*args)

r = executa(saudacao, 'Bom Dia', 'Haell')
print(r)