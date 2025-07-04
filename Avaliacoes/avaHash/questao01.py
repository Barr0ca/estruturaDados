ht = {}
def add_pessoa(ht: dict): # adiciona contato
    nome = input('Nome: ')
    telefone = int(input('Telefone: '))
    nome = nome.lower() # nome do contato em minusculo
    print('')
    ht[nome] = telefone # atribuindo telefone ao nome do contato
    print(f'{nome} adicionado.')

def remove_pessoa(ht: dict): # remove pessoa
    if ht == {}: # caso a agenda esteja vazia
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
        for elemento in list(ht): # para cada contato na agenda ele mostra o cotato
            print(f'Nome:{elemento}\nTelefone:{ht[elemento]}')
        print('')

def mostrar_contato(ht: dict): # busca o contato pelo nome inserido
    if ht == {}:
        print('Não há nada aqui.')
        print('')
    else:
        nome = input('Nome: ')
        print('')
        if nome not in ht:
            print('Contato inexistente.')
            print('')
        else:
            print(f'Nome:{nome}\nTelefone:{ht[nome]}')
        print('')

opcao = -1
while opcao != 0:
    print('Agenda telefônica')
    print('Adicionar/Atualiza [1]')
    print('Remover Contato    [2]')
    print('Mostrar Todos      [3]')
    print('Mostrar Contato    [4]')
    print('Sair               [SAIR]')
    opcao = input('Opção:     ')
    opcao = opcao.lower()
    print('')

    if opcao == '1':
        add_pessoa(ht)
    elif opcao == '2':
        remove_pessoa(ht)
    elif opcao == '3':
        mostrar_pessoas(ht)
    elif opcao == '4':
        mostrar_contato(ht)
    elif opcao == 'sair':
        break
    elif opcao != '1' or '2' or '3' or '4' or 'sair':
        print('Opção inválida.')
        print('')