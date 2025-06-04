class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome) > 0:
            self.__nome = nome
        else:
            print('nome invalido!')
pesso1 = Pessoa('Rodrigo')
print(pesso1.get_nome())
new_nome = str(input('Informe o novo nome: '))
pesso1.set_nome(new_nome)
print(pesso1.get_nome())