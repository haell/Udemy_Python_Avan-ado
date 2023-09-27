# Adiando execução de funções

""" def soma(x):
    return x + 5

def multiplica(y):
    return 10 * y

def criar_funcao(funcao, *args):
    return funcao(*args)

soma_com_cinco = criar_funcao(soma, 2)
multiplica_por_dez = criar_funcao(multiplica, 7)

print(soma_com_cinco, multiplica_por_dez) """


def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    def executa(y):
        return funcao(x, y)
    return executa

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(18), multiplica_por_dez(11))