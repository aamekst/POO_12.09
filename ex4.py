class Funcionario:
    def __init__ (self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self):
        sal_novo = ((percentual * self.salario)/100)+ self.salario
        print(f'O seu aumento de salario foi: {sal_novo}')


nome = input('Digite seu nome: ')
salario = float(input('Digite seu salario: '))
percentual =int(input('digite o percentual de aumento: '))

func = Funcionario(nome, salario)

func.aumentar_salario()