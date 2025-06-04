class Celular:
    def __init__(self, marca):
        self.__marca = marca
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        if isinstance(marca, str) and len(marca) > 0:
            self.__marca =marca
        else:
            print('marca INVALIDO!')
c1 = Celular('Android')
print(c1.get_marca())
c1.set_marca('Sei lá')
print(c1.get_marca())