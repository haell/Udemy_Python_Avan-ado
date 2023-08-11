from rich.table import Table
from rich.console import Console
#print(list(range(10)))

""" lista = []
for n in range(10):
    lista.append(n)

print(f"Lista 1: {lista}")


lista = [
    n*2
    for n in range(10)
    ]

print(f"Lista 2: {lista}") """



console = Console()

minha_lista = ['a', 'b', 'c', 'd', 5, 'f', 'g', 'h', 'i']

nova_lista = [
    i.upper() 
    if isinstance(i, str) else i
    for i in minha_lista
    ]

print(nova_lista) 

""" # Criar uma instância da tabela
tabela = Table(title="Tabela 3x3")

# Adicionar cabeçalhos das colunas
tabela.add_column("Coluna 1")
tabela.add_column("Coluna 2")
tabela.add_column("Coluna 3")

# Distribuir elementos da lista na tabela
for i in range(0, len(minha_lista), 3):
    tabela.add_row(str(minha_lista[i]), str(minha_lista[i+1]), str(minha_lista[i+2]))

# Exibir a tabela no console
console.print(tabela)
 """