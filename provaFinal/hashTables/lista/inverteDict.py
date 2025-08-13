def inverte(hash_table: dict):
    hash_table_invertido = {}
    for chave, valor in hash_table.items():
        # "setdefault" vai adicionar os novos valores em lista, impedido casos que existam valores repetidos
        hash_table_invertido.setdefault(valor, []).append(chave)

    return hash_table_invertido


pessoas = {'Garrincha': 30, 'Ronaldo': 20, 'Pelé': 40}

print(inverte(pessoas))
