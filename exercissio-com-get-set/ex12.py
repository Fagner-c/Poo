class Estudante():
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_matricula(self):
        return self.__matricula
    def set_matricula(self, matricula):
        self.__matricula = matricula
aluno1 = Estudante('jOÃO', '181133529830')
print(f'Aluno: {aluno1.get_nome()} | Matricula: {aluno1.get_matricula()}')
aluno1.set_nome('Lucas')
aluno1.set_matricula('181133528908')
print(f'Aluno: {aluno1.get_nome()} | Matricula: {aluno1.get_matricula()}')