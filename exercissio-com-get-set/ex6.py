class Produto():
    def __init__(self, valor):
        self.__preco = valor
    def get_preco(self):
        return self.__preco
    def set_preco(self, valor):
        if valor > 0:
            self.__preco = valor
produto1 = Produto(2.0)
print(produto1.get_preco())
produto1.set_preco(9.0)
print(produto1.get_preco())