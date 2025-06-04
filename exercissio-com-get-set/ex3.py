class Carro:
    def __init__(self, modelo):
        self.__modelo = modelo
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        if isinstance(modelo, str) and len(modelo) > 0:
            self.__modelo =modelo
        else:
            print('MODELO INVALIDO!')
carro1 = Carro('Celta')
print(carro1.get_modelo())
carro1.set_modelo('Sei lá')
print(carro1.get_modelo())