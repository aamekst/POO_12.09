
class Livro:
    def __init__ (self, titulo, autor, qntd_pag):
          self.titulo = titulo
          self.autor = autor
          self.qntd_pag = qntd_pag

    def exibir_livro(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Quantidade de paginas: {self.qntd_pag}')

livro1 = Livro ('dom casmucho', 'Machado de A X', 333)
livro2 = Livro ('Turma do Chico Bento', 'Mauriuciu', 55)
 
livro1.exibir_livro()

livro2.exibir_livro()