from collections import deque


def add(fila: deque, item: tuple):
    fila.append(item)
    print(f'Tarefa: {item[0]} recebida.')


def rem(fila: deque[tuple[str, int]]):
    if len(fila) <= 0:
        print('Você está sem tarefas para fazer.')
    else:
        nome, tempo = fila.popleft()
        print(f"Tarefa {nome} realizada em {tempo} minuto(s).")


tarefas = deque([])

opcao = -1
while opcao != 0:
    print('Escrever tarefa  [1]')
    print('Realizar tarefa  [2]')
    print('Sair             [0]')
    try:
        opcao = int(input('Opção:      '))
    except (ValueError):
        print('\nOpção inválida.\n')

    if opcao == 1:
        nome = input('Nome tarefa: ')
        tempo = input('Tempo (min):')
        tarefa = (nome, tempo)
        add(tarefas, tarefa)
    elif opcao == 2:
        rem(tarefas)
    elif opcao == 0:
        break
