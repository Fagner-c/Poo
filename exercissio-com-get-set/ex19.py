class Cidade():
    def __init__(self, nome, populacao):
        self.__nome = nome
        self.__populacao = populacao
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_populacao(self):
        return self.__populacao
    def set_populacao(self, populacao):
        self.__populacao = populacao