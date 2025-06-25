# Imprime a idade de uma pessoa da hashtable

ht = {}
for elementos in range(3):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    nome = nome.lower()
    print('')
    ht[nome] = idade

print(f'Temos {list(ht)}.\nVocê gostaria de saber a idade de quem?')
opcao = input('')
opcao = opcao.lower()
while True:
    if opcao.lower() not in ht:
        print('Nome inválido.')
        break
    else:
        print(f'A idade de {opcao} é {ht[opcao]}.')
        break