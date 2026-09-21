#listas, tuplas e dicionarios

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