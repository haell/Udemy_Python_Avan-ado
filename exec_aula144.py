# dir, hasattr e getattr em Python

string = 'Haell'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o métodos', metodo)