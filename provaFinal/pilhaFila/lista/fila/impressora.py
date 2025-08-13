from collections import deque


def ordem_impressora():
    fila_arquivos = deque([])

    opcao = -1
    while opcao != '0':
        print('')
        print('Enviar arquivo    [1]')
        print('Processar arquivo [2]')
        print('Sair              [0]')
        opcao = input('Opção:             ')

        if opcao == '1':
            nome_arq = input(f'\nInforme o nome do arquivo: ')
            qtd_pag = input(f'Informe a quantidade de páginas do arquivo: ')
            arquivo = {nome_arq: qtd_pag}
            fila_arquivos.append(arquivo)
            for key, values in fila_arquivos[0].items():
                print(f'Arquivo {key} adicionado para impressão.')
        elif opcao == '2':
            if len(fila_arquivos) == 0:
                print('\nNão há arquivos para serem processados.')
                continue
            for key, values in fila_arquivos[0].items():
                print(f'\nArquivo {key} impresso.')
            fila_arquivos.popleft()
        else:
            print('\nOpção inválida!')
            continue
