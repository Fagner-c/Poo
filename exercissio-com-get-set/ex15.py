class Curso():
    def __init__(self, nome, duracao):
        self.__nome  = nome
        self.__duracao = duracao
    def get_nome(self):
        return self.__nome
    def get_duracao(self):
        return self.__duracao
    def set_nome(self, nome):
        self.__nome = nome
    def set_duracao(self, duracao):
        self.__nome = duracao