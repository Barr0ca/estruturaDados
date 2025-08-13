def sistema_login():
    logins = {}

    opcao = -1
    while opcao != 0:
        print('Fazer Login    [1]')
        print('Se Cadastrar   [2]')
        print('Sair           [0]')
        try:
            opcao = int(input('Opção: '))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 0:
            print("Saindo...")
            break

        if opcao == 1:
            nome = input('Usuário: ')
            senha = input('Senha: ')
            if nome not in logins:
                print('Usuário não encontrado.')
            elif logins[nome] != senha:
                print('Senha incorreta.')
            else:
                print('Usuário logado com sucesso.')

        elif opcao == 2:
            nome = input('Informe o seu nome de usuário: ')
            senha = input('Informe a sua senha: ')
            if nome in logins:
                print('Usuário já existe.')
            else:
                logins[nome] = senha
                print('Cadastro efetuado.')


sistema_login()
