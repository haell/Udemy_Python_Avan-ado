""" x, y, *resto = 1, 2, 3, 4, 5, 6, 7, 8
print(f"x: {x} y: {y} resto:{resto}") """

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_tudo = soma(1, 2, 3, 4, 5, 6)
print(soma_tudo)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
print(numeros)
print(*numeros)