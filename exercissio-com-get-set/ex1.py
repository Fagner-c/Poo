class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
pesso1 = Pessoa('Rodrigo')
print(pesso1.get_nome())