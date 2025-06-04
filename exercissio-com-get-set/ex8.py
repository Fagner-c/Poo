class Funcionario():
    def __init__(self, salario):
        self.__salario = salario
    def set_salario(self, salario):
        if salario > 0 and isinstance(salario, float) :
            self.__salario = salario
        else:
            print('Valor invalido')
    def get_salario(self):
        return(self.__salario)
fun1 = Funcionario(200.0)
print(fun1.get_salario())
fun1.set_salario(800.0)
print(fun1.get_salario())