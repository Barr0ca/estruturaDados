from binarytree import bst
from collections import deque

arvore = bst(height=2, is_perfect=True)

def percurso_no(no):
    if not no:
        return []

    fila = deque([no])
    resultado = []

    while fila:
        no_atual = fila.popleft()
        resultado.append(no_atual.value)

        if no_atual.left:
            fila.append(no_atual.left)
        if no_atual.right:
            fila.append(no_atual.right)
    return resultado


print(arvore)

print(percurso_no(arvore))