from collections import deque


def add(fila: deque, item):
    fila.append(item)
    print(f'Senha {item} recebida com sucesso.')


def rem(fila: deque):
    if len(fila) <= 0:
        print('Não há senhas a serem atendidas.')
    else:
        print(f'Senha {fila.popleft()} atendida com sucesso.')
        print(
            f"Senhas que faltam a serem atendidas: {' -> '.join(map(str, fila))}")


senhas = deque([])
contador = 0

opcao = -1
while opcao != '0':
    print('Receber senha   [1]')
    print('Atender senha   [2]')
    print('Sair            [0]')
    opcao = input('Opção:           ')

    if opcao == '1':
        contador += 1
        add(senhas, contador)
    elif opcao == '2':
        rem(senhas)
    elif opcao == '0':
        break
    else:
        print('Opção inválida.')
