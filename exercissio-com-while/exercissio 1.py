from random import choice
from os import system
lista = list(range(1,100))
opc = 's'
while True:
    if opc == 'sim' or opc == 's':
        escolha = choice(lista)
        print(escolha)
        while True:
            try:
                user = int(input('Informe o numero que deseja: '))
                if user == escolha:
                    print('Você ganhou!')
                    system('cls')
                    break
                else:
                    system('cls')
                    print('Numero errado!')
            except:
                system('cls')
                print('Opção invalida, digite só numeros!')
    elif opc == 'n' or opc =='não':
        break
    elif opc != 's' or opc != 'sim':
        print('Opção invalida!')
    opc = str(input('Quer jogar novamente [s/n]: ')).lower()
print('Programa finalizado!')
