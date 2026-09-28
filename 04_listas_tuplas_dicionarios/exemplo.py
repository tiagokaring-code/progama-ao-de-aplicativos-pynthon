#listas, tuplas e dicionarios
import notas

#1.listas

#listas sao utilizadas para armazenar varios valores dentro de uma variavel

nomes = ["Ana", "carlos", "joão", "maria"]
print(nomes)

#2. acessando elementos da lista

print(nomes[0])
print(nomes[1])
print(nomes[2])


print(nomes[-1])

nomes[0] = 'pedro'
print(nomes)


nomes.append('lucas')
print(nomes)

nomes.insert(0, 'jonas')
print(nomes)

nomes.remove("carlos")
print(nomes)

nomes.pop(3)
print(nomes)


#6 tamanho da lista

print(len(nomes))

#7. percorrendo uma lista

for nome in nomes:
    print(nome)
#8.verificar se algum elemento existe
if 'joão' in nomes:
    print("joao esta na lista")
else:
    print("joao nao esta na  lista")

#9.lista com diferentes tipos de dados
dados = ["joâo",18, 1.75, True]
print(dados)
#10. lista de

notas =[15, 16, 1.7, 18, 12]
soma = 0

for nota in notas:

    soma += nota

media = soma / len(notas)
print(f"media: {media: .1f}")


#11. tuplas

coordenadas =(10, 20)
print(coordenadas)

#acessando elementos
print(coordenadas[0])
print(coordenadas[1])

#12. dicionarios

aluno ={
    "nome":  "carlos",
    "idade": 17,
    "nota":  8.5

}
print(aluno)

#13. aseceando valores do dicionario
print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

#14. alterando valores
aluno["nota"] = 9.0
print(aluno)