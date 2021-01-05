#Aula 07.3 - Métodos, Funções e Clases

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        print("Botão 'Power' foi apertado! ")
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    
    def aumenta_canal(self):
        if self.ligada:
            print("Aumentando canal!")
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            print("Diminuindo canal!")
            self.canal -= 1

if __name__ == '__main__':
    televisao = Televisao()
    televisao.aumenta_canal()
    print("Televisao está ligada: {}".format(televisao.ligada))
    print("Canal: {}".format(televisao.canal))
    televisao.power()
    televisao.aumenta_canal()
    print("Televisao está ligada: {}".format(televisao.ligada))
    print("Canal: {}".format(televisao.canal))
    televisao.diminui_canal()
    print("Televisao está ligada: {}".format(televisao.ligada))
    print("Canal: {}".format(televisao.canal))
    