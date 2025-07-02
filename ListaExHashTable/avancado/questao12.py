def anagramas(lista: list):
    ht = {}

    return ht


def verifica_anagrama(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False


palavras = ['amor', 'roma', 'batacae', 'tesoura', 'abacate']
ht = {}
chaves = []
for palavra in palavras:
    if palavra not in ht:
        palavraS = sorted(palavra)
        ht[palavraS] = 1
        chaves.append(palavra)
print(ht, chaves)

# print(anagramas(palavras))
