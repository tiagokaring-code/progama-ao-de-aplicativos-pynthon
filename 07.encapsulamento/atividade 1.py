class personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    @property
    def vida(self):
        return self.vida

    def receber_dano(self, valor):
        if valor > 0:
            self.vida -= valor
            if self.vida < 0:
                self.vida = 0

    def curar(self, valor):
        if valor > 0:
            self.vida += valor
            if self.vida >100:
                self.vida = 100
    def status(self):
        print(f"[{self.nome}] vida: {self.vida}/100")

    def atacar(self):
        return 10


class gurreiro(personagem):
    def __init__(self, nome, forca = 15):
        super().__init__(nome)
        self.forca = forca

    def atacar(self):
        return 10 + self.forca

class mago(personagem):
    def __init__(self, nome, mana = 50):
        super().__init__(nome)
        self.mana = mana

    def ver_mana(self):
        print(f"[{self.nome}] mana: {self.mana}")

    def atacar(self):
        if self.mana >= 10:
            self.mana -= 10
            return 25
        else:
            print(f"{self.nome} está sem mana suficiente!")
            return 5


if __name__ == '__main__':
    print("\nteste da parte 1 encapsulamento")
    p1 = personagem("heroi generico")
    p1.status()

    p1.receber_dano(30)
    p1.status()

    p1.receber_dano(-20)
    p1.status()

    p1.curar(50)
    p1.status()

    try:
        p1.vida = 200
    except AttributeError as e:
        print(f"Erro capturado com sucesso ao tentar alterar a vida: {e}")

    print