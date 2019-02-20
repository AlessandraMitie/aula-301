nome = input('Qual seu nome: ')
idade = int(input('Qual sua idade: '))

if idade >= 18:
    print('Pode entrar ' +nome)
    
elif idade < 11:
    print('Menor de idade, você ainda é criança')

else:
    print('Menor de idade')