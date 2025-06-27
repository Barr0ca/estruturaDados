# Filtra chaves maiores que 50 em uma hashtable

def filtra_chaves_50(ht: dict):
    hashT_filtrado = {}
    for produto in list(ht):
        if ht[produto] > 50:
            aux = ht[produto]
            hashT_filtrado[produto] = aux
    return hashT_filtrado

ht_produtos = {'Chinelo': 15.50, 'Tenis': 100.00, 'Bota': 79.99, 'Camisa': 50.00, 'Casaco': 53.00, 'Corta Vento': 120.50, 'Regata': 21.00, 'Bone': 10.00}

print(filtra_chaves_50(ht_produtos))