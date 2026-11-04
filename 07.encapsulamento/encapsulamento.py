class gerente(funcionario):
    super().__init__(nome, salario)
    self.equipe = equipe

    def bonus(self):
        return self.salario * 0.20 + self.equipe * 100


class estagiario(funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso
    def bonus(self):
        return 200


print("\n =====poliomorfismo=====")
