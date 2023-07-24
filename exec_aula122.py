""" import copy


d1 = {
    'c1': 1,
    'c2': 2,
    'li': [1, 2, 3],
}

d2 = d1.copy()

d2['c1'] = 1000
d2['li'][1] = 9999

d3 = copy.deepcopy(d1)

print(f'd1: {d1}')
print(f'd2: {d2}')
print(f'd3: {d3}') """
from time import sleep
from rich import print
from os import system
perguntas = [{
    'pergunta': 'Quanto é 2+2? ',
    'opcoes': ['1', '2', '3', '4'],
    'resposta': '4',
},
{
    'pergunta': 'Quanto é 5*5? ',
    'opcoes': ['25', '55', '10', '51'],
    'resposta': '25',
},
{
    'pergunta': 'Quanto é 10 / 2? ',
    'opcoes': ['4', '5', '2', '1'],
    'resposta': '5',
},]


def programa():
    certas = 0
    erradas = 0
    for pergunta in perguntas:
        system('cls')
        print(pergunta['pergunta'])
        print('Opções:')
        for indice, opcao in enumerate(pergunta['opcoes']):
            print(f'{indice+1})  {opcao}')
        while True:
            resposta = input("Escolha uma das opções: ")    
            if resposta in pergunta['opcoes']:
                if resposta == pergunta['resposta']:
                    print(f"[bold green] Acertou[/bold green]")
                    certas += 1
                    sleep(1)
                    break            
                else:
                    print(f"[bold red] Errou!!![/bold red]")
                    erradas += 1
                    sleep(1)
                    break
            else:
                print("Opção inválida!")


    print(f"De {len(perguntas)} você certou {certas} e errou {erradas}")



if __name__ == '__main__':
    programa()
