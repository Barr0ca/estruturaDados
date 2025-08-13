def calc_media(ht: dict):
    ht_media = {}

    for chave, valor in ht.items():
        ht_media[chave] = (sum(valor)/len(valor))

    return ht_media


alunos = {'Ronaldo': [10, 50, 60, 100], 'Romário': [
    40, 55, 50, 80], 'Cristiano': [70, 80, 70, 90], 'Garrincha': [100, 98, 80, 77]}

print(calc_media(alunos))
