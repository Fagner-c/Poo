class Aluno():
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = nota
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome) > 0:
            self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_nota(self, nota):
        if isinstance(nota, float):
            self.__nota = nota
    def get_nota(self):
        return self.__nota
aluno1 = Aluno('Lucas', 8.0)
print(f'Nome: {aluno1.get_nome()} Nota: {aluno1.get_nota()}')
aluno1.set_nome('gustavo')
aluno1.set_nota(7.8)
print(f'Nome: {aluno1.get_nome()} Nota: {aluno1.get_nota()}')