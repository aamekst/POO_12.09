#classe pessoa

#nome
#idade
#cpf

#falar
#comer
# dormr


#criando classe
class Pessoa: #1 LETRA MAISCULA
    def __init__(self, nome, idade, cpf):   #construtor   #self obrigatorio, referencia ao objeto
        self.nome = nome    #atributos
        self.idade = idade
        self.cpf = cpf

    #metodo  verbo
    def falar(self):
        print(f'A pessoa {self.nome} falou...')
    
    def comer(self):
        print('A pessoa comeu...')

    def dormir(self):
        print(f'RONCO GIGANTESCO DO {self.nome}')

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'Cpf: {self.cpf}')


#criando objeto
pessoa1 = Pessoa('João', 23, '123.456.789-23')#valores do atributo
pessoa2 = Pessoa('Maria', 20, '333.555.666-98')

#ALTERANDO OBJETO
pessoa1.nome = 'João Pedro'
pessoa1.idade = 25

print(pessoa1.nome, pessoa1.idade, pessoa1.cpf) # chamando atributo
pessoa1.dormir() # chamando metodo
pessoa1.falar()
pessoa1.comer()
pessoa1.exibir_dados()