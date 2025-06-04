class Aluno():
    def __init__(self, autor, titulo):
        self.__autor = autor
        self.__titulo = titulo
    def set_autor(self, autor):
        if isinstance(autor, str) and len(autor) > 0:
            self.__autor = autor
    def get_autor(self):
        return self.__autor
    def set_titulo(self, titulo):
        if isinstance(titulo, str) and len(titulo) > 0:
            self.__titulo = titulo
    def get_titulo(self):
        return self.__titulo
aluno1 = Aluno('Lucas', 'sei la')
print(f'Altor: {aluno1.get_autor()} Titulo: {aluno1.get_titulo()}')
aluno1.set_autor('gustavo')
aluno1.set_titulo('7.8')
print(f'Nome: {aluno1.get_autor()} Titulo: {aluno1.get_titulo()}')