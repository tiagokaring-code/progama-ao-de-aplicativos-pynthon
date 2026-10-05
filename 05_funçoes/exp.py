def saudaçao():
    print("ola seja bem vindo")

saudaçao()
#0.2 funçao com paramentros

def saudacao(nome):
    print(f"ola, {nome}")
saudacao("ana")
saudacao("carlos")

def apresentar(nome, idade):
    print(f"nome, {nome}")
    print(f"idade, {idade}")

apresentar("maria", 17)

def soma(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")
soma(10,5)

def somar(numero1, numero2):
    return numero1 + numero2
resultado = somar(10,20)
print(resultado)

def verificaridade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"
resultado = verificaridade(18)
print(resultado)

def saudaçao(nome ="joao"):
    print(f"ola, {nome}")
saudacao("joao")

def calcularmedia(nota1, nota2, nota3):
    rmedia = nota1 + nota2 + nota3/3
    return rmedia
print(calcularmedia(8, 7, 9))

def cadastroproduto():
    nome = input("Qual o seu nome?")
    preco = float(input("Qual o valor do produto?"))
    return nome, preco


def exibirproduto(nome, preco):
    print("\n======Produto======")
    print(f"nome {nome}")
    print(f"preco:  RS{preco}")

    nome, preco = cadastroproduto()
    exibirproduto(nome, preco)