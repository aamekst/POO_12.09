class Triangulo:
    def __init__ (self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c


    def calcular_perimetro(self):
        soma = (self.lado_a + self.lado_b + self.lado_c)
        print(f'Perimetro igual a: {soma}')
    # ou dessa forma: return self.lado_a + self.lado_b + self.lado_

lista = []
for a in range(2):
    print('---------------------------------------------')
    lado_a = int(input('Insira o valor do lado a: '))
    lado_b = int(input('Insira o valor do lado b: '))
    lado_c = int(input('Insira o valor do lado c: '))
    triangulo1 = Triangulo(lado_a, lado_b, lado_c)
    lista.append (triangulo1)

for t in lista:
     t.calcular_perimetro()

