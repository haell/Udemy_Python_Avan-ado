# (Parte 1) try e except para tratar exceções

# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Tentando dividir por zero!')
except NameError:
    print('Variável não definida')
except (TypeError + IndexError):
    print('TypeError + IndexError')
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUA...')