nota = 6
if nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperaçao')
else:
    print('Reprovado')

#condicionais e opradores logicos
#and -> todas as condiçoes devem ser verdadeiras
#or -> pelo menos uma coondiçao de ser verdadeira
#not -> inverte o resultado

idade = 20
ingreso = True

if idade >= 18 and ingreso:
    print("entrada permitida")
else:
    print("entrada nao permitida")

#3. estrutura de repetiçao while
contador = 1

while contador <= 5:
    print(contador)
    contador += 1

#4. estrutura de repetiçao fo

for numero in range(1,6):
    print(numero)

#5. percorendo uma lista
nomes =["ana","carlos","joao","maria"]

for nome in nomes:
    print(nome)

#6. break, continue, pass
for numero in range(1,11):
    if numero == 6:
        break
        print(numero)
