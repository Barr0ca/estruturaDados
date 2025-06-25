ht = {}
def add_pessoa(ht: dict):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    nome = nome.lower()
    print('')
    ht[nome] = idade
    print(f'{nome} adicionado.')

def remove_pessoa(ht: dict):
    if ht == {}:
        print('Não há nada aqui.')
        print('')
        return

    nome = input('Informe o nome de quem será removido: ')
    nome = nome.lower()

    if nome not in ht:
        print('Essa pessoa não existe.')
        print('')
    else:
        del ht[nome]
        print(f'{nome} foi removido.')
        print('')
    
def mostrar_pessoas(ht: dict):
    if ht == {}:
        print('Não há nada aqui.')
        print('')
    else:
        for elemento in list(ht):
            print(f'{elemento} com {ht[elemento]} anos.')
        print('')

opcao = -1
while opcao != 0:
    print('Adicionar [1]')
    print('Remover   [2]')
    print('Mostrar   [3]')
    print('Sair      [0]')
    try:
        opcao = int(input('Opção:     '))
        print('')
    except ValueError:
        print('Valor inválido. Por favor, insira um número.')
        print('')
        continue

    if opcao == 1:
        add_pessoa(ht)
    elif opcao == 2:
        remove_pessoa(ht)
    elif opcao == 3:
        mostrar_pessoas(ht)
    elif opcao == 0:
        break