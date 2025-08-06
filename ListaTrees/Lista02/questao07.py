# Verificando a soma de um caminho para um valor

from binarytree import bst

arvore = bst(height=2, is_perfect=True)


def verifica_caminho_valor(no, soma_alvo, soma_atual=0):
    if no is None:
        return False

    # Soma acumulada até o nó atual
    soma_atual += no.value

    # Se for folha, verifica se a soma bate
    if no.left is None and no.right is None:
        return soma_atual == soma_alvo

    # Verifica recursivamente nos dois lados
    return verifica_caminho_valor(no.left, soma_alvo, soma_atual) or verifica_caminho_valor(no.right, soma_alvo, soma_atual)


print(arvore)

print(verifica_caminho_valor(arvore, 14))
