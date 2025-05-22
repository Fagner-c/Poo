class Pessoa:
    def __init__(self, nome, sobrenome, idade,cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
    def informacaoSaida(self):
        print(f'O nome é  {self.nome} {self.sobrenome} que tem {self.idade} e mora em {self.cidade}')
pes1 = Pessoa(str(input(f'Informe o nome da pessoa: ')), str(input(f'Informe o sobrenome da pessoa: ')), int(input(f'Informe a idade da pessoa: ')), str(input(f'Informe o nome da cidade da pessoa: ')))
pes2 = Pessoa(str(input(f'Informe o nome da pessoa: ')), str(input(f'Informe o sobrenome da pessoa: ')), int(input(f'Informe a idade da pessoa: ')), str(input(f'Informe o nome da cidade da pessoa: ')))
pes3 = Pessoa(str(input(f'Informe o nome da pessoa: ')), str(input(f'Informe o sobrenome da pessoa: ')), int(input(f'Informe a idade da pessoa: ')), str(input(f'Informe o nome da cidade da pessoa: ')))
pes1.informacaoSaida()
pes2.informacaoSaida()
pes3.informacaoSaida()