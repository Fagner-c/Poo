from dataclasses import dataclass

#Exercissio 1:
@dataclass
class Carro():
    marca :str
    ano :str
    cor : str
    def valores(self):
        print(f'marca: {self.marca} \nano: {self.ano}\ncor: {self.cor}')
print('='*50, 'Exercissio 1', '='*50)
carro1 = Carro(str(input('Informe a marca do carro: ')), str(input('Informe o ano do carro: ')), str(input('Informe a cor do carro: ')))
carro1.valores()

#Exercissio 2:
@dataclass
class Pessoa():
    nome: str
    sobrenome:str
    idade: str
    emprego:str
    def valores(self):
        print(f'A pessoa se chama {self.nome} {self.sobrenome}, que tem {self.idade} anos e trabalha de {self.emprego}')
print('='*50, 'Exercissio 2', '='*50)
nome = str(input('Informe o nome: '))
sobrenome = str(input('Informe o sobrenome: '))
idade = str(input('Informe a idade: '))
emprego = str(input('Informe o emprego: '))
pessoa1 = Pessoa(nome, sobrenome, idade, emprego)
pessoa1.valores()

#Exercissio 3:
@dataclass
class Conta_Bancaria():
    saldo: float = 1000.0
    def new_saldo(self, op, valor):
        if (op == '1'):
            self.saldo += valor
        elif(op == '2'):
            self.saldo -= valor
        print(f'O seu novo saldo é {self.saldo}')
print('='*50, 'Exercissio 3', '='*50)
print('Selecione: \n[1]Depositar\n[2]Sacar')
op = str(input('Selecione uma opção: '))
valor =float(input('Informe o valor: '))
conta1 = Conta_Bancaria()
conta1.new_saldo(op, valor)