agenda = {}


def add_contato():
    nome = input("Nome: ").strip().lower()
    telefone = input("Telefone: ").strip()
    agenda[nome] = telefone
    print(f"{nome} adicionado/atualizado.")


def remover_contato():
    nome = input("Nome para remover: ").strip().lower()
    if nome in agenda:
        del agenda[nome]
        print(f"{nome} removido.")
    else:
        print("Contato inexistente.")


def mostrar_todos():
    if not agenda:
        print("Agenda vazia.")
        return
    for nome, tel in agenda.items():
        print(f"{nome}: {tel}")


def mostrar_contato():
    nome = input("Nome do contato: ").strip().lower()
    if nome in agenda:
        print(f"{nome}: {agenda[nome]}")
    else:
        print("Contato inexistente.")


# Menu
while True:
    print("\n1 - Adicionar/Atualizar contato")
    print("2 - Remover contato")
    print("3 - Mostrar todos")
    print("4 - Mostrar contato")
    print("0 - Sair")
    opcao = input("Opção: ").strip()
    if opcao == "1":
        add_contato()
    elif opcao == "2":
        remover_contato()
    elif opcao == "3":
        mostrar_todos()
    elif opcao == "4":
        mostrar_contato()
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
