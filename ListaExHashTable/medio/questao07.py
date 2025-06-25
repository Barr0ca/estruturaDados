# Invertendo um dicionário (valor:chave) para (chave:valor)

def inverte_hashT(ht: dict):
    for elemento in list(ht):
        aux = ht[elemento]
        del ht[elemento]
        ht[aux] = elemento
    return ht


hashT = {'Ian': 19, 'Maria': 23, 'Paulo': 30}
print(inverte_hashT(hashT))
