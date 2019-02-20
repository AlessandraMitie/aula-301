# -*- coding: utf-8 -*-

valor1 = int(input('digite o valor 1: '))
valor2 = int(input('digite o valor 2: '))
resultado = valor1 + valor2

if resultado >= 10 and resultado <= 12:
    print('valor está entre 10 e 12')

elif resultado == 13:
    print('opa opa')

else:
    print('não fizemos nenhum calc desse valor')

print(resultado)