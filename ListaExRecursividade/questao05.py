# Função que retorna uma string invertida

def inverteString(nome):
    if len(nome) == 0:
        return nome
    return nome[-1] + inverteString(nome[:-1])

print(inverteString('batata'))