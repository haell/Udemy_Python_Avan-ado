import re
import sys


def compor_cpf(valor='0'):
    while True:
        try:            
            digitos_calculo_cpf = list()
            digito_validador = list()
            cpf_digitado = list()
            valor_corrigido = re.sub(r'[^0-9]',
                '',
                valor                
                )
            entrada_sequencial =  valor_corrigido == valor_corrigido[0] * len(valor_corrigido)
            if entrada_sequencial:
                print("Você enviou dados sequenciais.")
                sys.exit()
                
            if len(valor_corrigido) == 11 and valor_corrigido.isdigit():
                digitos_calculo_cpf = list(valor_corrigido[:9])
                digito_validador = list(valor_corrigido[9:])
                break
            else:
                print("É necessário digitar alguma coisa!")
                break                
        except ValueError:
            print("ERRO! CPF não pode ser nulo.")
        except Exception:
            print("ERRO! CPF inválido. Digite 11 algarismos inteiros.")        
    
    cpf_digitado.append(digitos_calculo_cpf)
    cpf_digitado.append(digito_validador)
    return cpf_digitado




# confirma o 1° digito conferidor
cpf_digitado =  compor_cpf(input("Digite o CPF: "))
cont_d1 = 10
soma_digitos_1 = 0
for digito in cpf_digitado[0]:
    soma_digitos_1 += int(digito) * cont_d1    
    cont_d1 -= 1
fator_1 = soma_digitos_1 * 10
fator_2 = fator_1 % 11
confirma_digito_1 = fator_2 if fator_2 <= 9 else 0

print(f"Confirma digito 1: {confirma_digito_1}")


# confirma o 2° digito conferidor
cpf_calculado = list(cpf_digitado[0])
cpf_calculado.append(cpf_digitado[1][0])
cont_d2 = 11
soma_digitos_2 = 0
for digito in cpf_calculado:
    soma_digitos_2 += int(digito) * cont_d2
    cont_d2 -= 1
fator_1 = soma_digitos_2 * 10
fator_2 = fator_1 % 11
confirma_digito_2 = fator_2 if fator_2 <= 9 else 0

print(f"Confirma digito 2: {confirma_digito_2}")

digitos_verificadores = list()
digitos_verificadores.append(str(confirma_digito_1))
digitos_verificadores.append(str(confirma_digito_2))


if digitos_verificadores == cpf_digitado[1]:
    print(f"O CPF: ", end='\033[4m')
    for i in cpf_digitado[0]:
        print(f"{i}", end=' ')
    for dv in cpf_digitado[1]:
        print(f"{dv}", end=' ')
    print("\033[m é \033[32mválido!\033[m")
else:
    print(f"O CPF: ", end='\033[4m')
    for i in cpf_digitado[0]:
        print(f"{i}", end=' ')
    for dv in cpf_digitado[1]:
        print(f"{dv}", end=' ')
    print("\033[m é \033[31minvalido!\033[m")
