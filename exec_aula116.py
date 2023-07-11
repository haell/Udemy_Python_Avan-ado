# Clousure e funções que retornam outras funções

def criar_sasudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_sasudacao('Bom dia!')
s2 = criar_sasudacao('Boa noite!')
print(s1('Haell'))
print(s2('Liz'))