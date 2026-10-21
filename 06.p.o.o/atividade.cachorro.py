class cachorro:
    def __init__(self, nome, raca, idade):
        self.raca = raca
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: au au!")
    def mostrar_info(self):
        print(f"nome: {self.nome}, idade: {self.idade}, raca: {self.raca}")


c1 = cachorro("rex", "pastor alemao", 2)
c2 = cachorro("pipo", "xauxau", 4)

c1.latir()
c1.mostrar_info()

c2.latir()
c2.mostrar_info()

print("\n--- mudando idade")
c1.idade = 3
c1.mostrar_info()


 