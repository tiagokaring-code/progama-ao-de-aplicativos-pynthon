class celular:
    def __init__(self, marca, modelo, cor, bateria  = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False
    def ligar(self):
        if self.bateria == 0:
            print("sem bateria! coloque para caregar!")
        else:
            self.ligado = True
            print("ligado")
    def desligar(self):
        self.ligado = False
        print("desligado")
        

celular1 = celular("Samsung", "galaxy s21", "preto" )
celular2 = celular("Samsung", "galaxy s21", "preto" )

print(celular1.marca)
print(celular1.modelo)
print(celular2.bateria)
