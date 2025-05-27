cont = total =0
print('Digite uma sequencia de numeros, se digitar 0 o prograa encerra')
while True:
    try:
        num = int(input(f'Informe o numero {cont}: '))
        total += num
        if num == 0:
            break
        cont += 1
    except ValueError:
        print('Digite só numeros!')
print(f'A soma total dos {cont} é {total}')