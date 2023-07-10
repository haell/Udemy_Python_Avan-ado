""" x, y, *resto = 1, 2, 3, 4, 5, 6, 7, 8
print(f"x: {x} y: {y} resto:{resto}") """

""" def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_tudo = soma(1, 2, 3, 4, 5, 6)
print(soma_tudo)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
print(numeros)
print(*numeros) """

def par_impar(n):
    if int(n) % 2 == 0:
        return f'{n} é PAR!!!'
    return f'{n} é IMPAR!!!'

numero = input("Digite um número: ")
print(par_impar(numero))

numero = par_impar(input("Digite um número: "))
print(numero)
