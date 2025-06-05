class Filme():
    def __init__(self, titulo, ano_lancamento):
        self.__nome =titulo
        self.__ano_lancamento = ano_lancamento
    def get_nome(self):
        return self.__nome
    def set_nome(self,titulo):
        self.__nome =titulo
    def get_ano_lancamento(self):
        return self.__ano_lancamento
    def set_ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento