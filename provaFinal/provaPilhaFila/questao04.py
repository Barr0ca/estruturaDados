from collections import deque

fila_tarefas = deque()

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Mostrar próxima tarefa")
    print("3 - Executar tarefa")
    print("0 - Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome da tarefa: ")
        prioridade = input("Prioridade (baixa/média/alta): ")
        fila_tarefas.append({"nome": nome, "prioridade": prioridade})
        print(f"Tarefa '{nome}' adicionada.")
    elif opcao == "2":
        if fila_tarefas:
            t = fila_tarefas[0]
            print(
                f"Próxima tarefa: {t['nome']} (Prioridade: {t['prioridade']})")
        else:
            print("Nenhuma tarefa na fila.")
    elif opcao == "3":
        if fila_tarefas:
            t = fila_tarefas.popleft()
            print(f"Tarefa '{t['nome']}' executada.")
        else:
            print("Nenhuma tarefa para executar.")
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
