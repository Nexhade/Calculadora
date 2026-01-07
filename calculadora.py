#Projeto de uma calculadora com multiplas funcões

from os import system

system('clear')

print('Calculadora! \n')

print('''1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão com sobra
5 - Disisão com número inteiro
''')

tipo_calc = int(input('Digite o número correspondente a operação que deseja fazer: '))

if tipo_calc == 1:
    system('clear')
    print('Soma!\n')
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    resul = num1 + num2
    escolha = input('\nDeseja adicionar mais um número (S/N): ')
    while escolha.upper() != 'N':
        base = 0
        base = float(input('\nDigite o próximo número: '))
        resul += base
        escolha = input('Deseja adicionar mais um número (S/N): ')
    system('clear')
    print(f'O resulta da sua soma é: {resul}')
    num1, num2, resul = 0, 0, 0 #Deixo as variais setada a 0 pois seram reutilizadas quando o programa for um loop
    escolha = "" #Variavel vazia pois ela será utilizada novamnte quando o programa rodar em loop
elif tipo_calc == 2:
    system('clear')
    print('Subtração!')
