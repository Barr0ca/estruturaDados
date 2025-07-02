def funcao_hash(chave, ht: list):
    return sum(ord(c) for c in str(chave)) % len(ht)

def inserir(chave, valor, ht: list):
    indice = funcao_hash(chave, ht)
    ht[indice] = [chave, valor]

def busca(chave, ht: list):
    indice = funcao_hash(chave, ht)
    par = ht[indice]
    if par and par[0] == chave:
        return par[1]
    else:
        return None

# Criação da tabela hash
hashT = [None] * 10

# Inserção dos dados
inserir(20, 'Ian', hashT)
inserir(30, 'Iago', hashT)
inserir(32, 'Filho', hashT)

# Busca
print(busca(20, hashT))     
print(busca(30, hashT))     
print(busca(999, hashT))    