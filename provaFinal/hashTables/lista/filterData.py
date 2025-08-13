def filtro_50(ht: dict):
    filtrados = {}

    for chave, valor in ht.items():
        if valor > 50:
            filtrados[chave] = valor

    return filtrados


produtos = {'Tênis': 200, 'Boné': 20, 'Camisa': 60, 'Pastel': 3}

print(filtro_50(produtos))
