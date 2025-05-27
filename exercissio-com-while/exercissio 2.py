usuarios = [
    {'nome': 'Fagner', 'senha': 'abacate'}, {'nome': 'João', 'senha': 'cid'}
]
valor = False
while True:
    cont = 0
    user = str(input('Informe o nome do usuario: '))
    for usuario in usuarios:
        if user == usuario['nome']:
            senha = str(input('Informe a senha: '))
            if senha ==  usuario['senha']:
                valor =True
                break
            else:
                cont = 0
                print('Senha incorreta!')
                break
        else:
            if cont + 1  == len(usuarios):
                print('Usuario não existe!')
                cont = 0
        cont += 1
    if valor == True:
        break
print('Bem vindo!')