# Questão 1
pessoas = {'Garrincha': 30, 'Ronaldo': 20, 'Pelé': 40}

# Questão 2

print(f"Idade: {pessoas.get('Pelé')}\n")

# Questão 3
pessoas['Maria'] = 20
del pessoas['Ronaldo']

# Questão 4
if pessoas.get('Maria') is None:
    print('Não existe\n')
else:
    print('Está presente\n')

# Questão 5
for chave, valor in pessoas.items():
    print(f"{chave} têm {valor} anos.")
