def mescla(ht_1: dict, ht_2: dict):
    ht_mesclado = ht_1.copy()

    for chave, valor in ht_2.items():
        if chave in ht_mesclado:
            ht_mesclado[chave] += valor
        else:
            ht_mesclado[chave] = valor

    return ht_mesclado


alunos_1 = {'Garrincha': 80, 'Ronaldo': 30, 'Pelé': 40, 'Romário': 40}
alunos_2 = {'Garrincha': 20, 'Ronaldo': 40, 'Pelé': 50, 'Rivaldo': 75}

print(mescla(alunos_1, alunos_2))
