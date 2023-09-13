#class sem atributos
class Televisao:
    def __init__ (self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume += 1
        print('volume aumentado')
    
    def diminuir_volume(self):
        self.volume -= 1
        print('volume diminuindinho')
         
    def alterar_canal(self, canal):
        self.canal = canal
        print('canal alterado')

tv = Televisao()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
tv.alterar_canal(5)
print(f'A tv está no canal {tv.canal}')             # A tv está no canal 5
print(f'A tv está no volume {tv.volume}')           # A tv está no volume 2
