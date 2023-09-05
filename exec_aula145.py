# Generator expression, iterables e iterators em Python
import sys


iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__
lista =  [n for n in range(10)]
generator = (n for n in range(10)) #list comprehention [n for n in range(10)]
#print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

def exibe_g(any):
    while True: 
        try:   
            print(next(any))
        except StopIteration:
            break


exibe_g(generator)