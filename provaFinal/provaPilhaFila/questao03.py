pilha = []

while True:
    print("\nDigite uma palavra (ou 1 para desfazer, 2 para mostrar, 0 para sair):")
    entrada = input()

    if entrada == "0":
        break
    elif entrada == "1":
        if pilha:
            removido = pilha.pop()
            print(f"Palavra removida: {removido}")
        else:
            print("Nada para desfazer.")
    elif entrada == "2":
        print("Texto atual:", " ".join(pilha))
    else:
        pilha.append(entrada)
