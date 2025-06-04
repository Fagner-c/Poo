class Animal():
    def __init__(self, idade):
        self.__idade = idade
    def get_idade(self):
        return self.__idade
    def set_idade(self, idade):
        if idade > 0 and isinstance(idade,  int):
            self.__idade = idade
        else:
            print('Valor invalido!')
animal1 = Animal(2)
print(animal1.get_idade())
animal1.set_idade(9)
print(animal1.get_idade())