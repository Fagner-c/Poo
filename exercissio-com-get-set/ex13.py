class Veiculo():
    def __init__(self, velo_max):
        self.__velo_Max = velo_max
    def get_velo_max(self):
        return self.__velo_Max
carro1 = Veiculo(123)
print(carro1.get_velo_max())