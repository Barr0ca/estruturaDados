# Cria uma hashtable com 3 pessoas

ht = {}
for elementos in range(3):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    ht[nome] = idade
print(ht)
