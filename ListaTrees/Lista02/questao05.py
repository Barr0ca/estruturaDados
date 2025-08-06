# Realizando o percurso em nível em uma BST

from binarytree import bst
from collections import deque

arvore = bst(height=2, is_perfect=True)

# Percurso em nível (level-order)


def percurso_no(no):
    if not no:
        return []

    fila = deque([no])
    resultado = []

    while fila:
        no_atual = fila.popleft()  # Remove o primeiro nó da fila
        resultado.append(no_atual.value)

        if no_atual.left:  # Se o nó atual tem filho à esquerda
            fila.append(no_atual.left)
        if no_atual.right:  # Se o nó atual tem filho à direita
            fila.append(no_atual.right)

    return resultado


print(arvore)

print(percurso_no(arvore))
