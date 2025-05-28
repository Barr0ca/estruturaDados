# Pilha

# from random import randint
# pilha = []

# for i in range(10):
#     pilha.append(randint(0, 100))
#     print(pilha)

# for c in range(len(pilha)):
#     print(pilha.pop())

# Problema: Inverter a string "abelha"
pilha = []
palavra = 'abelha'
print(palavra)

for i in range(len(palavra)):
    pilha.append(palavra[i])

print(pilha)

nova_palavra = ''

for a in range(len(pilha)):
    nova_palavra += pilha.pop()

print(nova_palavra)