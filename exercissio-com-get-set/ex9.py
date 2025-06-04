class Casa():
    def __init__(self, endereco, valor):
        self.__endereco = endereco
        self.__valor = valor
    def set_endereco(self, endereco):
        if isinstance(endereco, str) and len(endereco) > 0:
            self.__endereco = endereco
    def get_endereco(self):
        return self.__endereco
    def set_valor(self, valor):
        if isinstance(valor, float):
            self.__valor = valor
    def get_valor(self):
        return self.__valor
aluno1 = Casa('Lucas', 80000.0)
print(f'endereco: {aluno1.get_endereco()} valor: {aluno1.get_valor()}')
aluno1.set_endereco('gustavo')
aluno1.set_valor(7000.80)
print(f'endereco: {aluno1.get_endereco()} valor: {aluno1.get_valor()}')