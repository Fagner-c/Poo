class ContaBancaria():
    def __init__(self, saldo):
        self.__saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.new_saldo = self.__saldo + valor
            self.set_saldo()
    def sacar(self, valor):
        if valor > 0:
            self.new_saldo = self.__saldo - valor
            self.set_saldo()
        else:
            print('Valor invalido!')
    def set_saldo(self):
        if self.new_saldo >= 0:
            self.__saldo = self.new_saldo
            self.new_saldo = 0
    def get_saldo(self):
        return self.__saldo
pessoa1 = ContaBancaria(1000.0)
pessoa1.sacar(200.0)
print(pessoa1.get_saldo())
pessoa1.depositar(600.0)
print(pessoa1.get_saldo())