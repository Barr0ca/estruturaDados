indice = {}

while True:
    comando = input("Comando (ADD/DEL/TEL/LIST/SAIR): ").strip().upper()
    if comando == "SAIR":
        break
    elif comando.startswith("ADD "):
        _, palavra, pagina = comando.split()
        pagina = int(pagina)
        palavra = palavra.lower()
        if palavra not in indice:
            indice[palavra] = []
        indice[palavra].append(pagina)
        print(f"Palavra '{palavra}' adicionada na página {pagina}.")
    elif comando.startswith("DEL "):
        _, palavra = comando.split()
        palavra = palavra.lower()
        if palavra in indice:
            del indice[palavra]
            print(f"Palavra '{palavra}' removida.")
        else:
            print("Palavra não encontrada.")
    elif comando.startswith("TEL "):
        _, palavra = comando.split()
        palavra = palavra.lower()
        if palavra in indice:
            print(f"{palavra}: páginas {indice[palavra]}")
        else:
            print("Palavra não encontrada.")
    elif comando == "LIST":
        for palavra, paginas in indice.items():
            print(f"{palavra}: páginas {paginas}")
    else:
        print("Comando inválido.")
