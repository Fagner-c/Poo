class Estudante():
    def __init__(self, nome, diciplina):
        self.__nome = nome
        self.__diciplina = diciplina
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_diciplina(self):
        return self.__diciplina
    def set_diciplina(self, diciplina):
        self.__diciplina = diciplina