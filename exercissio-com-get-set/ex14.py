class Computador():
    def __init__(self, memoria):
        self.__memoria = memoria
    def set_memoria(self, memoria):
        if memoria > 0:
            self.__memoria = memoria
        else:
            print('Valor errado!')