class Empresa():
    def __init__(self, nome, numero_funcionario):
        self.__nome = nome
        self.__numero_funcionario = numero_funcionario
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_numero_funcionario(self):
        return self.__numero_funcionario
    def set_numero_funcionario(self, numero_funcionario):
        self.__numero_funcionario = numero_funcionario