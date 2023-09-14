# (Parte 2) try e except com else e finally

# a = 18
# b = 0
# c = a / b

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(f'{e.__class__.__name__}: {e}')
except IndexError:
    print('Erro de index')
else:
    print('Sem erros.')
finally:
    print('FECHAR ARQUIVO')