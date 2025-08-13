from collections import deque


def add(fila: deque, item):
    fila.append(item)
    print(f'{item} embarcou.')


def rem(fila: deque):
    if len(fila) <= 0:
        print('Ônibus está vazio.')
    else:
        print(f'{fila.popleft()} desembarcou.')


onibus = deque([])

opcao = -1
while opcao != 0:
    print('')
    print('Embarque                 [1]')
    print('Desembarque              [2]')
    print('Ordem desembarque        [3]')
    print('Sair                     [0]')
    try:
        opcao = int(input('Opção:                    '))
    except (ValueError):
        print('\nOpção inválida.\n')

    if opcao == 1:
        item = input('Quem chega para embarcar: ')
        add(onibus, item)
    elif opcao == 2:
        rem(onibus)
    elif opcao == 3:
        print(onibus)
    elif opcao == 0:
        break
